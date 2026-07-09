---
title: '【學習筆記】Claude API：Structured Outputs 結構化輸出'
author: Heidi Liu
tags:
  - AI
  - Claude
  - Structured Outputs
categories:
  - 技術學習
  - AI
date: 2026-04-16 17:14:00
---

## Structured outputs 結構化輸出

[Structured outputs（結構化輸出）](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)是 Claude API 提供的功能，用來讓模型輸出符合指定的 JSON schema。透過 **Constrained decoding（約束解碼）**，在「生成過程中」限制模型只能產生合法的 JSON 結構，而不是在輸出後再做檢查。

<!--more-->

換言之，並非在回應生成後才做 JSON 檢查，而是在 token 生成階段就進行的限制：

```
// 一般生成：
  Claude → 任意 token → 任意文字（格式不可預測）

// Constrained decoding：
  Claude → 只允許符合 JSON schema 的 token → 保證有效 JSON
```

因此可以大幅降低以下問題：

- JSON syntax error
- 缺少必要欄位
- 型別錯誤

---

## 兩個核心功能：JSON outputs / Strict tool use

Structured outputs 提供兩種互補功能：

| 功能 | 控制對象 | API 參數 | 用途 |
|------|---------|---------|------|
| **JSON outputs** | Claude 的回應本身 | `output_config.format` | 限制回應為符合 schema 的 JSON |
| **Strict tool use** | Claude 的 tool\_use block | `strict: true` | 限制 tool 呼叫參數符合 input\_schema |

兩者目的都是限制 **Claude 的輸出**，不是驗證 tool 的執行結果（tool 本身仍需由應用程式負責處理與驗證）。當需要「工具 + 結構化最終回應」的情況時也可以同時使用。

### JSON outputs 範例

+ 使用場景：不需要工具，直接讓 Claude 回應結構化資料（JSON），用來做資料提取與分類

```typescript
const response = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [
    { role: "user", content: "Extract: John Smith (john@example.com) wants Enterprise plan" }
  ],
  output_config: {
    format: {
      type: "json_schema",
      schema: {
        type: "object",
        properties: {
          name: { type: "string" },
          email: { type: "string" },
          plan: { type: "string" },
        },
        required: ["name", "email", "plan"],
        additionalProperties: false,
      },
    },
  },
});

// → { "name": "John Smith", "email": "john@example.com", "plan": "Enterprise" }
```

#### 搭配 Zod（TypeScript SDK）

```typescript
import { z } from "zod";
import { zodOutputFormat } from "@anthropic-ai/sdk/helpers/zod";

const ContactSchema = z.object({
  name: z.string(),
  email: z.string(),
  plan: z.string(),
});

const response = await client.messages.parse({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Extract: John (john@example.com) wants Enterprise" }],
  output_config: { format: zodOutputFormat(ContactSchema) },
});

console.log(response.parsed_output.email);
// 自動帶有型別推斷
```

### Strict tool use 範例

+ 使用場景：在 Claude 呼叫工具時，確保產生的 `tool_use` block 參數符合 `input_schema`

```typescript
const response = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
  tools: [{
    name: "get_weather",
    description: "Get current weather for a city",
    strict: true,      // ← 啟用嚴格模式
    input_schema: {
      type: "object",
      properties: {
        location: { type: "string" },
        unit: { type: "string", enum: ["celsius", "fahrenheit"] },
      },
      required: ["location"],
      additionalProperties: false,
    },
  }],
});

// tool_use arguments 保證符合 input_schema
// 不會出現 location: 123 型別錯誤 or 缺少 location 欄位
```

---

## Claude API 的資料流

根據官方文件，一段 Agent Flow 的基本資料流如下：


```
User
↓
Claude    // 模型決定是否呼叫工具
↓
tool_use  // Claude 產生 tool 呼叫（Strict tool use 限制參數）
↓
Tool execution  // 應用程式執行工具
↓
tool_result
↓
Claude    // Claude 產生最終回應（可使用 JSON outputs）
↓
Assistant response
```

在這個流程中，Structured outputs 主要影響兩個階段：

- **JSON outputs**：限制 Claude 的最終回應格式
- **Strict tool use**：限制 `tool_use` block 的參數格式

透過 Structured outputs，能夠讓應用程式可以更安全地解析 Claude 的輸出，避免 JSON 格式錯誤或欄位缺失。

## 在 AI 應用中的角色

如果從 AI 應用系統的角度來看，可以把整體流程放在一個簡化的架構中（此為常見 application pattern，非 Claude 官方定義）：

| Layer | 功能 |
|------|------|
| Model interaction | 與 LLM 溝通（Claude API） |
| Integration | 呼叫外部服務與工具 |
| Presentation | 將結果呈現在 UI |

在這個架構下，Structured outputs 的角色可以理解為：

> 提供一個「可靠的 LLM → application data interface」

也就是讓 LLM 的輸出，從原本難以預測的自然語言，轉變為可以被程式穩定處理的資料格式。

在沒有 structured outputs 的情況下，Claude 的回應可能是：

- 段落文字
- Markdown
- 或每次都是不同格式

這對應用程式來說是難以直接解析的。而透過 Structured outputs 機制：

- JSON outputs → 保證最終輸出結構
- Strict tool use → 保證 tool 呼叫參數正確

資料流會變成：

```
LLM（Claude）
↓
可靠的 JSON / tool arguments
↓
Application code（安全解析與使用）
```


換句話說，Structured outputs 的核心價值，是讓 LLM 從「不可預期的文字生成」變成「可預測的資料接口」，這也是在實作 AI Agent 或 Generative UI 時非常重要的一環。

## 小結

Structured outputs 提供兩個核心能力：

- JSON outputs：控制最終回應格式
- Strict tool use：控制工具呼叫參數

讓 LLM 的輸出可以被穩定地當成資料使用，而不只是自然語言，這也是在實作 AI Agent 與工具整合時的關鍵基礎。

## 參考資料
+ [Structured outputs - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
+ [Tool use with Claude - Claude API Docs
](https://platform.claude.com/docs/en/build-with-claude/tool-use)

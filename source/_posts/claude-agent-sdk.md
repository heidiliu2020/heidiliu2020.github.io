---
title: '【學習筆記】Claude Agent SDK：概觀與 Human-in-the-loop 機制'
author: Heidi Liu
tags:
  - AI
  - Claude
  - Agent SDK
  - Human-in-the-loop
categories:
  - 技術學習
  - AI
date: 2026-04-02 17:27:00
---

![claude](https://hackmd.io/_uploads/HJ6TA0x2bg.png)

最近在研究 AI Agent 技術，調查 Claude Agent SDK 是否能支援 **Human-in-the-loop（人機協作）** 以及 **不同工作階段的 Agent workflow**。

這系列筆記整理了調查過程中的重點，主要參考 [Anthropic 官方文件](https://docs.anthropic.com/en/docs/agents-and-tools/claude-agent-sdk) 和實際的 Demo 實作經驗，方便日後查詢。本篇會先介紹 Claude Agent SDK 的基本概念，以及 Human-in-the-loop 在 Agent 系統中的運作方式。


<!--more-->
---

## Claude Agent SDK 是什麼？

**[Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)** （前身為 Claude Code SDK）是 [Anthropic](https://www.anthropic.com/) 官方提供的 SDK，讓開發者在自己的應用程式中嵌入 Claude 的 Agent 能力。

簡單來說，就是把 Claude Code 的能力包成一個函式庫，讓使用者可以在 Web App、API Server 等場景中使用。

| 項目 | 內容 |
|------|------|
| 套件名稱 | `@anthropic-ai/claude-agent-sdk`（TypeScript）/ `claude-agent-sdk`（Python） |
| 安裝指令 | `npm install @anthropic-ai/claude-agent-sdk` |
| 核心 API | `query()` — 開發者大多只需使用 `query()` |
| 前提條件 | 需要 `ANTHROPIC_API_KEY` |

### SDK vs. Claude Code CLI

這兩者的關係可以這樣理解：

+ CLI 是給「人」用的互動工具
+ SDK 是給「程式」用的函式庫

| 使用場景 | 最佳選擇 |
|----------|----------|
| 互動式開發（終端機 / IDE） | CLI |
| CI/CD 管線 | SDK |
| 自訂應用程式（Web / API） | **SDK** |
| 生產環境自動化 | SDK |

如果想在自己的 Web App 或 API 中整合 Agent 功能，SDK 就是你需要的東西。

### Agent 的基本組成

在 Claude Agent SDK 中，一個 Agent 通常由三個部分組成：

| 元件 | 說明 |
|------|------|
| LLM | Claude 模型負責推理 |
| Tools | Agent 可以呼叫的外部能力 |
| Control Layer | 開發者控制 Agent 行為（例如 HITL） |

SDK 的 `query()` 函式負責協調這三個部分。

## AI Agent 的兩個控制層

在實際設計 AI Agent 系統時，通常需要考慮兩個核心問題：

1. **Agent 能做什麼？（能力控制）**
2. **Agent 什麼時候需要人類介入？（決策控制）**

在 Claude Agent SDK 中，這兩個層面分別由不同機制負責：

| 控制層 | 對應機制 |
|------|------|
| Capability Control | systemPrompt + tools |
| Decision Control | Human-in-the-loop (`canUseTool`) |

本篇會先介紹第二個部分：Human-in-the-loop 的運作方式。

## Human-in-the-loop 人機協作

### 什麼是 HITL？

Human-in-the-loop（HITL）是指 Agent 在執行過程中，**暫停動作、請求人類確認後再繼續**的機制。

為什麼需要這個機制呢？因為 Agent 可能會需要執行一些高風險操作（例如刪除檔案、執行系統指令），這時讓人類在關鍵節點上進行審核，可以避免不當操作。

### 核心機制：`canUseTool` callback

SDK 提供 **一個統一的 callback** 來處理所有的人機互動，流程大致如下：

```
User Prompt
   ↓
Claude Agent 推理
   ↓
Agent 想使用 Tool（例如 write_file("config.json")）
   ↓
SDK 呼叫 canUseTool("Write", {...})
   ↓
應用程式決定
  ✓ Allow  → 繼續執行
  ✗ Deny   → 停止這個動作
  ✎ Modify input → 改參數後執行
   ↓
Tool 根據結果執行
   ↓
Agent 繼續推理
```

重點在於：**所有的人機互動都通過這一個 callback**，包含工具審核和 Agent 提問，不需要分別處理。

### 實作程式碼

```typescript
const result = query({
  prompt: "幫我重構這個專案",
  options: {
    canUseTool: async (toolName, input, { signal, decisionReason }) => {
      // 允許執行
      return { behavior: "allow", updatedInput: input };

      // 拒絕執行
      return { behavior: "deny", message: "使用者拒絕了這個操作" };

      // 修改參數後允許
      return { behavior: "allow", updatedInput: { ...input, path: "/safe/path" } };
    },
  },
});
```

### 兩種觸發情境

#### 情境 A：工具審核（Tool Approval）

Agent 要使用工具時（如寫入檔案），SDK 自動呼叫 `canUseTool` 讓人類審核：

```
Agent 想執行 write_file("utils.go")
    ↓
SDK 呼叫 canUseTool("Write", { file_path: "utils.go", ... })
    ↓
應用程式顯示審核 UI → 使用者選擇 Approve / Deny
    ↓
Agent 根據結果繼續或停止
```

#### 情境 B：AskUserQuestion（Agent 主動提問）

除了工具審核之外，Agent 有時也需要向使用者詢問資訊。

當 Agent 判斷資訊不足時，會呼叫 `AskUserQuestion` 工具向使用者提問。
這個操作 **同樣會觸發 `canUseTool`**，但角色不同，此時應用程式需要將問題顯示給使用者，收集答案後再回傳給 Agent。

```typescript
canUseTool: async (toolName, input) => {
  if (toolName === "AskUserQuestion") {
    // Agent 在提問 → 顯示問題、收集答案
    const answers = await showQuestionUI(input.questions);
    return {
      behavior: "allow",
      updatedInput: { ...input, answers }
    };
  }

  // 其他工具 → 審核是否允許
  const approved = await showApprovalUI(toolName, input);
  if (approved) {
    return { behavior: "allow", updatedInput: input };
  } else {
    return { behavior: "deny", message: "使用者拒絕" };
  }
}
```

用一個具體的例子來說明 `AskUserQuestion` 的流程：

```
Agent 不確定要用哪個測試框架
    ↓
Agent 呼叫 AskUserQuestion({
  questions: [{
    question: "你想用哪個測試框架？",
    options: [
      { label: "Jest",   description: "最常用的 JS 測試框架" },
      { label: "Vitest", description: "較新，與 Vite 整合好" }
    ]
  }]
})
    ↓
SDK 呼叫 canUseTool("AskUserQuestion", { questions: [...] })
    ↓
應用程式顯示問題 UI，使用者選了 "Vitest"
    ↓
回傳 { behavior: "allow", updatedInput: { ...input, answers: { "你想用哪個測試框架？": "Vitest" } } }
    ↓
Agent 收到答案，用 Vitest 繼續開發
```

### 內建權限策略：`permissionMode`

`permissionMode` 是 SDK 內建的預設策略，而 `canUseTool` 則提供更細緻的控制。這種方式適合快速原型或 CLI 工具，如果需要自訂 UI 或更細緻的控制，通常會搭配 `canUseTool` 使用。

如果兩者同時存在，SDK 會先套用 `permissionMode`，再透過 `canUseTool` 讓應用程式做最終決策。

| permissionMode | 行為 |
|----------------|------|
| `"default"` | 標準模式，需要審核 |
| `"plan"` | 規劃模式，唯讀工具自動通過 |
| `"acceptEdits"` | 自動接受檔案編輯 |
| `"bypassPermissions"` | 全部放行（謹慎使用） |

## Claude Agent SDK 在 Web App 中的基本架構

### 系統架構

在實際的 Web 應用中，Claude Agent SDK 通常會部署在後端 API 層，由前端透過 HTTP 請求與 Agent 互動。

以下是一個典型的 Next.js 架構：

```
┌────────────────────────────────────────────┐
│  Next.js Web App                           │
│                                            │
│  ┌──────────┐    POST     ┌─────────────┐  │
│  │ React UI │  ────────→  │ API Route   │  │
│  │ (Chat)   │  ←──SSE───  │ /api/agent  │  │
│  └──────────┘             └──────┬──────┘  │
│                                  │         │
└──────────────────────────────────│─────────┘
                                   │ query()
                            ┌──────▼──────┐
                            │ Claude      │
                            │ Agent SDK   │
                            └──────┬──────┘
                                   │
                            ┌──────▼──────┐
                            │ Claude API  │
                            │ (Anthropic) │
                            └─────────────┘
```

前端負責顯示聊天 UI 與使用者互動，後端 API Route 則負責呼叫 Claude Agent SDK，並將串流結果回傳給前端。當 Agent 需要人類審核或提問時，則透過 `canUseTool` callback 觸發應用程式的 UI。

### 串流回覆與互動流程

實際實作時，Agent 的回覆通常會透過 **串流（streaming）** 的方式傳回前端，例如使用 SSE（Server-Sent Events）或 WebSocket。

當 `canUseTool` 觸發需要使用者回覆的情境（例如 `AskUserQuestion`）時，系統會暫停 Agent 的執行並等待使用者輸入，再繼續推理。

由於 SSE 是單向通信，許多 Web 應用會採用 **SSE + REST** 的雙通道架構：

- SSE：Server → Client 傳送 Agent 回覆
- REST POST：Client → Server 回傳使用者回答

這種串流與互動的通信設計，涉及較多 Web 架構與 Agent session 管理，本文先聚焦於 Agent SDK 與 Human-in-the-loop 的基本概念，相關實作細節將在後續文章中介紹。

---

## 總結

Claude Agent SDK 提供了一個簡單但強大的模型來構建 AI Agent：

- `query()` 負責執行 Agent 推理流程
- Tools 讓 Agent 可以與外部系統互動
- `canUseTool` 提供 Human-in-the-loop 機制，讓人類在關鍵操作前介入

透過這些機制，開發者可以在 **自動化與人工監督之間取得平衡**，建立更安全可控的 AI Agent 系統。

不過在實際的 Web 應用中，為了讓 AI Agent 在自動化與可控性之間取得更好的平衡，還需要進一步設計：

- Agent 回覆的 **串流傳輸（SSE / WebSocket）**
- `AskUserQuestion` 等互動流程的 **session 管理**
- 不同任務階段的 **Agent workflow 設計**

後續文章將會進一步介紹：

- **Agent 串流與互動設計**（SSE / WebSocket / REST 架構）
- **Agent Workflow 設計**（Plan / Execute / Review 模式切換）

## 參考資料

- [Claude Agent SDK 官方文件](https://docs.anthropic.com/en/docs/agents-and-tools/claude-agent-sdk)
- [Anthropic API Reference](https://docs.anthropic.com/en/api)

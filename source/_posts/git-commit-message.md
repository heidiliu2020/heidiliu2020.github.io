title: '【學習筆記】如何撰寫好的 Git Commit Message'
author: Heidi Liu
tags:
  - Git
categories:
  - 技術學習
  - Git
date: 2021-03-06 22:48:00
updated: 2026-07-09 16:01:08
---
## 為什麼 Commit Message 很重要？

Git 在每次 Commit 時，需要寫下 Git Commit Message（提交說明），用來記錄提交版本更動的摘要。

> 任何專案都至少由兩個以上的開發者共同合作開發。
<!--more-->

除了專案開發者，任何專案都會是跟其他開發者、以及未來的自己共同開發維護的。當不同開發者接手專案時，能藉由瀏覽 Commit Message 內容快速進入狀況，瞭解程式異動的原因，如此也利於後續的維護。關於多人協作的分支流程，可參考另一篇[〈Git 版本控制：如何進行多人協作 & 同步分支〉](/git-workflow/)。

### 何謂好的 Commit Message？

一個好的 Git Commit Message 必須兼具 What & Why & How，能幫助開發者瞭解這個提交版本：

1. 做了什麼事情（What）
2. 為什麼要做這件事情（Why）
3. 用什麼方法做到的（How）

## Commit Message 的規範與準則

在團隊之間，撰寫 commit log 的方式應一致，也就是定義風格與內容，可透過遵守現有的慣例來實現。

一個 Commit Message 主要由 Header + Body + Footer 組成：

```text
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

### Message Header: `<type>(<scope>): <subject>`
 - type（必要）：commit 的類別
   - 如：feat, fix, docs, style, refactor, test, chore
 - scope（可選）：commit 影響的範圍
   - 如：資料庫、控制層、模板層等，視專案不同改變
 - subject（必要）：commit 的簡短描述
   - 不超過 50 個字元
   - 結尾不加句號
   - 盡量讓 Commit 單一化，一次只更動一個主題

### Message Body
 * 對本次 Commit 的詳細描述，解釋 What & Why & How
 * 可以分成多行，每一行不超過 72 個字元
 * 說明程式碼變動的項目與原因，還有與先前行為的對比

### Message Footer
 - 填寫任務編號 `issue #1246`
 - BREAKING CHANGE（可略），記錄不兼容的變動，後面是對變動的描述、以及變動原因和遷移方法

## Header：`<type>` 類別規範

type 代表提交 Commit 的類別，以下為使用慣例：

* feat：新增或修改功能（feature）
* fix：修補 bug（bug fix）
* docs：文件（documentation）
* style：格式
  * 不影響程式碼運行的變動，例如：white-space, formatting, missing semi colons
* refactor：重構 
  * 不是新增功能，也非修補 bug 的程式碼變動
* perf：改善效能（improves performance）
* test：增加測試（when adding missing tests）
* chore：maintain
  * 不影響程式碼運行，建構程序或輔助工具的變動，例如修改 config、Grunt Task 任務管理工具
* revert：撤銷回覆先前的 commit
  * 例如：`revert: feat(auth): 新增第三方登入`

### Commit Message 範例

以下舉幾個範例：

```
feat: message 新增信件通知功能
feat(優惠券): 加入搜尋按鈕，調整畫面

fix: 圓餅圖圖例跑版
fix: 意見反應，信件看不到圖片問題

style: 統一換行符號 CRLF to LF

docs: 更新 README 相關資訊
docs: 修正型別註解

chore(submodule): 變更 git url
chore: 調整單元測試環境

refactor(每日通知信件): 重構程式結構
```

## Conventional Commits：業界通用標準

上述格式源自 AngularJS 的 commit 慣例，後來發展成正式的規範 —— [Conventional Commits](https://www.conventionalcommits.org/zh-hant/v1.0.0/)，也是目前業界最通用的標準，格式如下：

```text
<type>[optional scope][!]: <description>

[optional body]

[optional footer(s)]
```

與前面介紹的慣例大致相同，並明確定義了「不兼容變動」的標記方式：

- 在 type 後面加上 `!`，或在 footer 寫 `BREAKING CHANGE:`，表示這個 commit 包含破壞性變更
- 範例：

```text
feat(api)!: 移除 v1 版本的使用者 API

BREAKING CHANGE: 請改用 /v2/users，舊版路徑將回傳 410
```

遵循這套規範的好處，是 commit 紀錄可以直接對應到[語意化版本（SemVer）](https://semver.org/lang/zh-TW/)：

| Commit type | 對應版本號 | 說明 |
| --- | --- | --- |
| `fix:` | PATCH（1.0.**1**） | 修補錯誤 |
| `feat:` | MINOR（1.**1**.0） | 新增功能 |
| `BREAKING CHANGE` / `!` | MAJOR（**2**.0.0） | 不兼容變動 |

## 用工具讓規範真正落地

光靠團隊約定容易鬆散，實務上通常會搭配工具在 commit 當下就把關：

- [commitlint](https://commitlint.js.org/) + [husky](https://typicode.github.io/husky/)：透過 Git Hook 在 commit 時自動檢查訊息格式，不符合規範就直接擋下
- [commitizen](https://github.com/commitizen/cz-cli)：改用 `git cz` 指令，以互動式問答一步步產生符合規範的訊息，適合幫助團隊成員養成習慣
- [semantic-release](https://semantic-release.gitbook.io/semantic-release/)：依據 commit type 自動決定版本號並產生 CHANGELOG —— 這也是遵守規範最實際的回報：發版流程可以完全自動化

## AI 時代的 Commit Message

現在也可以透過 AI 工具（如 [Claude Code](https://claude.com/claude-code)、GitHub Copilot）讀取 diff 自動產生 commit message。實際使用下來的心得是：

- AI 很擅長總結「做了什麼（What）」，產生的格式也能符合 Conventional Commits
- 但「為什麼這樣改（Why）」往往只存在人的腦中 —— 例如「為了修復某個客訴問題」、「因為舊 API 即將淘汰」，這些背景資訊仍需要自己補上
- 建議把 AI 產生的訊息當作草稿，確認 What 並補上 Why 之後再送出，而不是照單全收

> 延伸閱讀：[【學習筆記】Claude Agent SDK：概觀與 Human-in-the-loop 機制](/claude-agent-sdk/)

## 總結

- 好的 Commit Message 要能回答 What、Why、How，格式上遵循 `<type>(<scope>): <subject>` + Body + Footer
- 這套慣例的正式標準是 Conventional Commits，搭配 SemVer 讓版本演進有跡可循
- 透過 commitlint、commitizen、semantic-release 等工具，規範才能真正被執行，而不是停留在文件裡
- AI 可以代筆 commit message，但變動背後的「動機」還是得由人來記錄

## 參考資料

- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/zh-hant/v1.0.0/)
- [Git Commit Message 這樣寫會更好，替專案引入規範與範例](https://wadehuanglearning.blogspot.com/2019/05/commit-commit-commit-why-what-commit.html)
- [撰寫有效的 Git Commit Message](http://blog.fourdesire.com/2018/07/03/%E6%92%B0%E5%AF%AB%E6%9C%89%E6%95%88%E7%9A%84-git-commit-message/)
- [如何寫一個Git Commit Message | louie_lu's blog](https://blog.louie.lu/2017/03/21/%E5%A6%82%E4%BD%95%E5%AF%AB%E4%B8%80%E5%80%8B-git-commit-message/#rules03)
- [AngularJS Git Commit Message Conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#)
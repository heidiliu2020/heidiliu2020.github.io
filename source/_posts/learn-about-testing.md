title: 測試二三事（上）｜還記得你說，要和我寫測試
author: Heidi Liu
tags:
  - JavaScript
  - Testing
categories:
  - 技術學習
  - JavaScript
date: 2022-12-16 14:24:00
---

![upload successful](/images/pasted-2.png)
## 前言

過去在程式導師實驗課程中，整理過這兩篇筆記探討「測試」是怎麼回事：

- [[week 3] 初探 Jest：如何測試程式？](https://heidiliu2020.github.io/javascript-jest/)
- [[week 22] React：用 SPA 架構實作一個部落格（三）- 淺談測試](https://heidiliu2020.github.io/react-test/)

在轉職後的第一家公司，組內曾嘗試在既有專案中撰寫測試，卻因時程緊湊而不了了之。但或許是一聽到測試就浮現「好麻煩⋯⋯」的想法吧？與其花這個時間去寫程式來進行測試，還不如多修幾個 BUG 來得有效益，打從心底想逃避這件事情，只覺得測試是理想，讓這項 TODO 一直被延宕。

<!--more-->

而在求職過程中，時常被問是否有過測試經驗；到了現在第二間公司，寫測試這議題又再次浮現。回想起過去在專案中，時不時發生「改 A 壞 B」 的情況，如果透過測試來事先預期結果，或許就能減少這類錯誤的發生。

於是乎，這篇文章就誕生了ಠ_ಠ 

在實作過程中，試著統整過去所學並且記錄下來，文章大致會分成四個段落，在正式介紹 Cypress 這套測試框架之前，會先在上篇補充測試相關的知識：

- Why we need test?
- What is Testing?
- Why Cypress?
- How to start?

那麼就開始吧！

## Why we need test?

所以說，為何我們需要測試？

誠如前言提到，透過測試我們能夠先預期結果，找出非預期的錯誤情境。在轉體開發過程中，隨著需求日漸複雜化，多人協作開發不易維護，再加上時程壓力，若沒有制定流程規範，實在很難透過手動測試一次到位。

讓自動化測試取代人工測試，除了能降低成本，也有助於快速驗證程式是否能正常運作，並透過測試報告找出問題所在，不至於在茫茫程式海中迷失方向。

總歸而言，測試能夠確保程式碼的可靠性，避免人為錯誤，提升程式碼的質量、重用性與可維護性。

## What is Testing?

說了這麼多，到底怎樣才是測試呢？

從我們最熟悉的人工測試，到寫程式來測試程式，其實都是基於同樣的道理：「測試是藉由程式來模擬現實，比較『預期結果』和『實際結果』是否相同的過程」。

### 自動化測試金字塔 Test Automation Pyramid

簡單來說，測試依規模大致可分成三個層次，構成自動化測試金字塔，如下圖所示：

![](/images/posts/learn-about-testing/L9sS6uH.png)

> [Automation Panda](https://automationpanda.com/2018/08/01/the-testing-pyramid/)

在測試金字塔中，越靠上方所耗費成本越高、執行時間越長；反之，越靠底下所耗費成本低，執行時間越短。

而依照測試方法不同，又可分為黑箱測試與白箱測試：

- 黑箱測試（Black-box Testing）/ 功能測試
    - 以使用者的角度，針對程式的功能面進行測試
    - 應用於整合測試和系統測試
    - 舉例：在表格欄位輸入錯誤的資料格式，檢測系統是否存在漏洞
- 白箱測試（White-box Testing）/ 結構測試
    - 以程式語言的角度，測試內部結構或流程
    - 應用於單元測試
    - 舉例：使用訂單系統，依使用者的情境模擬操作

![](/images/posts/learn-about-testing/ymjyD7I.png)

### 單元測試 Unit Testing

- 以程式碼的最小單位（function、method 等）進行測試，也是自動測試化的基礎
- 驗證單一行為、執行快速、具獨立性
- 常用套件：[Jest](https://jestjs.io/)、[mochajs](https://mochajs.org/) & [chai](https://github.com/chaijs/chai)
- 常見開發模式：TDD & BDD

這裡介紹兩種與單元測試（Unit Test）相關的開發流程：

- **TDD（Test-Deriven Development）測試驅動開發**
    - 先寫測試，後實作功能
    - 專注功能的實現
    - 開發流程會在「單元測試 ⇒ 撰寫能通過測試的程式碼 ⇒ 重構」三者之間循環
- **BDD （Behavior-Deriven Development）行為驅動開發**
    - 為 TDD 的進化版，但會先寫測試規格書，再寫測試，後實作功能
    - 專注系統的行為，較貼近使用者的角度進行測試
    - 使用 `describe()` 和 `it()` 需求為導向的設計語意化
        
![](/images/posts/learn-about-testing/8NgSbPj.png)  

### 整合測試 Integration Testing

- 整合兩個以上的元件（Component）或模組（Module）之間的互動測試
- 使用 Mock Data 模擬 Mock API 回傳內容，檢測 render DOM 是否呈現預期結果
- 常用套件：[TestBed](https://angular.io/api/core/testing/TestBed)、[Testing Library](https://testing-library.com/)、[Enzyme](https://enzymejs.github.io/enzyme/)

為什麼需要整合測試？單元測試都通過不就代表都 OK 了？下圖提供非常好的例子：

![](/images/posts/learn-about-testing/H30Yzer.gif)

> 門鎖 OK、開關門 OK、鎖門？？

根據不同情境所需，有時即使單元測試沒測出問題，一旦跨模組整合就出事了，因此這個階段更重視不同元件或環境之間的整合互動，也更貼近使用者實際行為。

### 端對端測試 End-to-end Testing / E2E Testing

- 會運行一個瀏覽器，藉由模擬使用者操作，將手動測試轉變成程式碼自動執行
- 是對真實系統進行的測試，較費時且維護成本高
- 常用套件：[Cypress、](https://www.cypress.io/)[Nightwatch](https://nightwatchjs.org/)、[Puppeteer](https://github.com/puppeteer/puppeteer)、[Protractor](https://www.protractortest.org/)（[Angular v12 後棄用，不再內建於新專案中](https://github.com/angular/protractor/issues/5502)）

如下所示，為 Cypress 使用範例，能夠看到使用者實際操作頁面的過程：

![](/images/posts/learn-about-testing/GzISa0E.gif)

> [Visual Testing | Cypress Documentation](https://docs.cypress.io/guides/tooling/visual-testing)

## Consolusion

雖說寫測試很重要，但並非寫好寫滿就是最好作法，畢竟需求情境百百種，仍需考慮使用時機與情境，才不會本末導致，花費更多時間維護測試腳本。

透過撰寫測試，~~強迫~~讓開發者寫出容易被測試的程式碼，並在有限的資源中，以有效的測試來確保程式的品質。

然而，這些測試的道理我都懂，但到底該如何開始呢？下篇會繼續探討，如何透過 Cypress 這套工具進行 E2E Testing，並且實際應用到專案中！

## Reference

- [一次搞懂單元測試、整合測試、端對端測試之間的差異 | The Will Will Web](https://blog.miniasp.com/post/2019/02/18/Unit-testing-Integration-testing-e2e-testing)
- [[web] 程式是人寫出來的，測試也是| PJCHENder 未整理筆記](https://pjchender.dev/webdev/web-testing/)
- [Angular 深入淺出三十天：表單與測試系列 - iT 邦幫忙](https://ithelp.ithome.com.tw/users/20090728/ironman/3881)
- [Hahow for Business 如何跑E2E 測試？ - Amo's Blog](https://blog.amowu.com/cypress-on-rails/)

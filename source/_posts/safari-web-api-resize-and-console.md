title: 【學習筆記】關於 iOS 的那些坑之二：Web API、Resize 與消失的 Console
author: Heidi Liu
tags:
  - Front-End
  - iOS
  - Back-End
categories:
  - 技術學習
  - Front-End
date: 2023-05-17 11:45:00
---

![Photo by [Pandhuya Niking](https://unsplash.com/@dispandu?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/rl6aomPDKl8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)](https://images.unsplash.com/photo-1639656333400-ee5240f757a0?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb)

Photo by [Pandhuya Niking](https://unsplash.com/@dispandu?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/rl6aomPDKl8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)


## 前言：iOS 之坑、再次襲來

既上篇的「[【學習筆記】 關於 iOS Safari 的那些坑：禁止選取 & 縮放設定](https://heidiliu2020.github.io/safari-pinch-and-double-tap/)」之後，因為 Web APP 開發需同時支援 Android 和 iOS 裝置，在過程中仍不時被新的隕石砸中，只好再挖新的坑來填補。

<!--more-->

這次要探討的主題比較瑣碎，大致如下：

- Wait!! Do you know where’s my console?
- Resize fires multiple times
- Web API: Fullscreen & Vibration

## Wait!! Do you know where’s my console?

- Reference：[Console.log not displaying on iPad Pro Safari 16.4 when using dev tools on my mac - Stack Overflow](https://stackoverflow.com/questions/75862081/console-log-not-displaying-on-ipad-pro-safari-16-4-when-using-dev-tools-on-my-ma)
- 預期結果：透過開啟 Safari 開發者模式，詳細操作可參考這篇：[[30- 相關工具] 手機遠程測試 - iT 邦幫忙](https://ithelp.ithome.com.tw/articles/10209412)
- 實際操作：裝置升級至 iOS 16.4 版本後，需注意可能發生無法 Debug 的情況，尤其在需要測試行動裝置時，發現 console 畫面無法顯示任何資訊

儘管仍可查看元件樣式，但主控台呈現一片空白：

![](https://hackmd.io/_uploads/BynS2TbSn.png)

> 白天不懂夜的黑，Console 不懂我的悲QQ

### How to resolve?

以下提供幾種解決方案：

- 最土法煉鋼的方法：透過 `console.log` 大法直接印到 webview 上，但若需要動態更新頁面，例如多國語系功能（i18n），則需要抓取 DOM 的 innerHTML 一個一個置換更新，但非常麻煩且耗費效能
    - 因為習慣使用 Angular 框架提供的 NGX-Translate，支援快速切換多國語系功能*，*詳細可參考這篇：[i18n 多國語系- Ngx-Translate - iT 邦幫忙](https://ithelp.ithome.com.tw/articles/10299595)
    - 如果是原生 JavaScript 專案，可參考這份套件 https://github.com/fnando/i18n-js 來實作
- 或建立一個 div 容器在頁面上，把需要的 Debug 資訊放在這裡，像是監聽事件等，這做法同樣是透過更新 DOM 元素
- 或更新 mac 上的 Safari 版本至 16.4，但需注意 Safari 16.4 僅支援 [macOS Big Sur 和 macOS Monterey](https://support.apple.com/zh-tw/HT213671) 較新的 macOS 版本，目前手上的 mac 因為版本較舊還沒嘗試此解法
- 2023.8 將 macOS 更新至 Monterey 12.6.6 版本以後，即可將 Safari 版本升級到 16.4，Console 又回來了，可喜可賀^_^

## Resize fires multiple times

- Reference：
    - [javascript - window.onresize fires twice - Stack Overflow](https://stackoverflow.com/questions/15812618/window-onresize-fires-twice)
    - [Window resize fires twice in Chrome and FireFox, but only one in Safari - Stack Overflow](https://stackoverflow.com/questions/13916485/window-resize-fires-twice-in-chrome-and-firefox-but-only-one-in-safari)
- 預期結果：當畫面進行縮放或旋轉時，預期會觸發一次 resize event 來進行後續動作，像是重新生成 UI 元件到相對或絕對位置
- 實際操作：但在不同瀏覽器上，這段期間卻有可能不只觸發一次 resize，導致畫面更新不如預期，例如萬惡的 Safari 或是熟悉的 Chrome，在實測時是發生在行動裝置的 Chrome 上

### How to resolve?

這時可透過設定 setTimeout，避免短時間內重複觸發 resize event，範例如下：

```jsx
let resizeTimer;
window.addEventListener("resize", (e) => {
  if (resizeTimer) clearTimeout(resizeTimer);  // 判斷是否已發生 resize
  resizeTimer = setTimeout(() => {
    // Do something...
  }, 100);
}, false);
```

## Web API: Fullscreen & Vibration

接著要探討的，是 Web API 提供的全螢幕顯示（Fullscreen）以及控制裝置震動（Vibration）功能。不論是在使用什麼 API 之前，都應該先查詢是否支援所需裝置，否則即使實作完成，到最後才發現原來不支援，反而要花更多時間去找別種工具，因此事前評估尤其重要。

### Fullscreen API 顯示全螢幕

- Reference：
    - [Fullscreen API - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API)
    - [[iOS Safari] Fullscreen API on a non-video element | Apple Developer Forums](https://developer.apple.com/forums/thread/133248)

以下是不同裝置上的瀏覽器對 Fullscreen API 支援度：

![](https://hackmd.io/_uploads/rk2Y3pZSh.png)

可以看到 Safari 雖然在行動裝置僅支援到 iOS 12，在 PC 上還是能支援到 16.4。但需注意的是，不像其他瀏覽器，Fullscreen API 只能套用在 video 元素上，若用在其他像是 div 元素時一概沒有反應，這點真的很不友善。

但如果因為功能需求，必須套用在 div 元素上的話，還是有方法可以繞過這個限制，例如透過 PWA 來實現全螢幕效果，外觀就像 Native APP 一樣。

### What is PWA?

![](https://hackmd.io/_uploads/ByFz66WBh.png)
Ref: https://www.evertop.pl/en/progressive-web-app-pwa/

以下是 MDN 關於 [PWA](https://developer.mozilla.org/zh-TW/docs/Web/Progressive_web_apps) 的介紹：

> **Progressive Web Apps** (PWAs) are web apps that use [service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API), [manifests](https://developer.mozilla.org/en-US/docs/Web/Manifest), and other web-platform features in combination with [progressive enhancement](https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement) to give users an experience on par with native apps.
> 

> 漸進式網路應用程式（PWAs）是透過 [service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)、[manifests](https://developer.mozilla.org/en-US/docs/Web/Manifest) 技術，並以漸進增強策略，建立跨平台 web 應用程式，提供用戶體驗近似於原生程式的功能。
> 

這裡簡單介紹上述提到的 Service Worker 與 Manifest 兩項技術：

- Service Worker：可想像是位於 Web APP 與網路連接之間的代理人，讓網頁擁夠像 Native APP 一樣支援離線和訊息推播功能
- Manifest：藉由設定 manifest.json 檔的參數，可自訂啟動畫面、安裝在主畫面顯示的名稱與 icon 等

透過 PWA 建立的 Web APP，使用者只需將網頁加到主畫面，開啟時就不會顯示網址列，外表就和 Native APP 一樣是全螢幕，能夠有更好的沉浸式體驗。

除此之外，使用 PWA 還有其他好處，像是安裝快速、定義快取、離線瀏覽、可被搜尋等優點，藉此提升使用者體驗。詳細可參考這篇文章：[PWA 實戰經驗分享 - Huli's blog](https://blog.huli.tw/2018/10/13/pwa-in-action/)，有提到如何實作 PWA 以及不同平台可能遇到的問題等等。


### Vibration API 使裝置震動

- Reference：[Vibration API - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Vibration_API)

![](https://hackmd.io/_uploads/S11Rn6WB2.png)

Safari 沒有懸念不支援 Vibration API，但令人感到意外的是 Firefox 也僅支援較低版本。

此外，需注意在 Safari 瀏覽器下呼叫 vibrate() 時，有可能因出現 error 導致無法進行後續動作，最保險的做法還是加上防呆驗證，確定裝置有支援才執行功能。

```jsx
const userAgent = window.navigator.userAgent;
if(!userAgent.includes('iOS') && !userAgent.includes('Mac OS')) navigator.vibrate();
```

## 小記

接續上篇筆記，陸續來回在 Safari 和 Android 裝置進行測試，發現一旦接受「只要遇上 Safari 大多支援度不高」這個事實以後，開發起來就快樂多了，畢竟這也不是工程師煩惱就有用的問題；反而要煩惱不同瀏覽器之間對事件觸發、Web API 支援程度的差異性。

簡言之，該如何從現有的技術去實作近似於目標的功能，先熟悉擁有哪些工具再去談可行性，才是更需要學習的地方。


title: Sass/SCSS 入門：變數、巢狀、混入、繼承
author: Heidi Liu
tags:
  - Front-End
  - CSS
categories:
  - 技術學習
  - Front-End
  - HTML & CSS
description: Sass/SCSS 入門教學：認識 CSS 預處理器解決了哪些問題，整理變數、巢狀結構、混入（mixin）、繼承（extend）等核心語法與編譯方式，並說明 Dart Sass 時代 @use 取代 @import 的寫法，讓 CSS 更好維護。
date: 2021-04-13 21:20:00
updated: 2026-07-13 12:00:00
---
> 2026.07 更新：補充 Dart Sass 與 `@import` 正式棄用的說明——現在請一律使用 `@use` 引入模組，編譯器則使用 npm 的 `sass` 套件（舊的 `node-sass` 已棄用）。本文的變數、巢狀、混入、繼承等語法均不受影響。

其實過去在 Lidemy 課程中，也有提過 CSS 預處理器的觀念：[[week 13] 前端工具之二 - CSS 預處理器、Babel](https://hackmd.io/@Heidi-Liu/note-fe201-sass-and-babel)，因為工作上需要使用，發現自己對語法還是不太熟悉，於是整理了這篇筆記。瞭解這套工具的由來，基本語法的使用，以及如何幫助我們解決前端開發可能遇到的問題。

<!--more-->

## What is CSS 預處理器？

我們所熟知的 CSS，是用來撰寫網頁樣式的語言，但隨著網頁開發複雜度提高，尤其是大型專案，在開發時也面臨許多問題：
+ 全域樣式會互相干擾，不易進行 debug，可維護性差
+ 重複撰寫相同樣式，程式碼不易閱讀

為了解決這些問題，CSS 預處理器（CSS Preprocessor）就誕生了！透過將程式模組化的概念，新增了變數、巢狀結構、混入、繼承等寫法，作為 CSS 語法的擴充，用以改善程式碼的結構與可維護性。

現今較為主流的 CSS 預處理器有下列三種，均賦予 CSS 動態語言的特性：

+ Sass/SCSS：最廣為開發者使用
+ Less：原先是基於 Ruby 開發，後來改用 Node.js 為基底實作
+ Stylus：基於 Node.js 開發

而本篇所探討的 Sass/SCSS，主要包含兩種寫法，分別是：

+ 舊版的 SASS
  + 縮排語法，副檔名 .sass
  + 使用縮排方式編輯巢狀關係

```sass=
.nav 
  background: #eee
  li 
    display: inline-block
```

+ 新版的 SCSS
  + 塊語法，副檔名 .scss
  + 使用大括號區分選擇器，使用分號區分屬性，較貼近原生 CSS

```scss=
.nav {
  background: #eee;
  li {
    display: inline-block;
  }
}
```

將上述範例程式碼，經編譯過的 CSS 寫法如下：

```css=
.nav {
  background: #eee;
}
.nav li {
  display: inline-block;
}
```

需注意不管使用哪種 CSS 預處理器，程式碼都必須先編譯（compiled）成 CSS 的形式，才能讓瀏覽器解讀並呈現出畫面。

> 關於編譯器：Sass 的官方實作是 **Dart Sass**，對應的 npm 套件名稱就叫 `sass`（`npm install sass`）。早年常見的 `node-sass`（LibSass）已於 2020 年宣告棄用，新專案請不要再使用。

## Sass/SCSS 基本語法

> 詳細教程可參考 [Sass 官網](https://sass-lang.com/guide)。

Sass/SCSS 提供的功能主要如下：

* 參數與結構化 CSS
  * Nesting：巢狀語法
  * Variables：變數設定
* 模組化 CSS
  * Import 引入檔案，用來分別進行管理
  * Extend 繼承，處理共同樣式
  * Mixin 混入，打包常用功能，替換局部變數
  * Functions 函式
* 自動化 CSS
  * Condition 條件判斷
  * Loop 跑迴圈：例如使用 `@each` 搭配 array、`@each` 搭配 map、for 迴圈

### 變數 Variables

使用說明：以錢字號 `$` 來宣告變數，通常會寫在程式碼最上方，只要有引用該變數的地方，均可統一修改管理，常用於：按鈕顏色、字型字體大小等。

+ 編譯前 SCSS

```sass=
$font-stack:  Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
```

+ 編譯後 CSS

```css=
body {
  font: 100% Helvetica, sans-serif;
  color: #333;
}
```

### 巢狀結構 Nesting 

使用說明：需注意縮排寫法，可使用 `&` 符號來引用父選擇器，常用於 CSS 元件狀態 `:hover`、`:focus`、`:before`、`:after` 等。

+ 編譯前 SCSS

```sass=
nav {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  li { display: inline-block; }

  a {
    display: block;
    padding: 6px 12px;
    text-decoration: none;
    &:hover {
      color: red;
    }
  }
}
```

+ 編譯後 CSS

```css=
nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
nav li {
  display: inline-block;
}
nav a {
  display: block;
  padding: 6px 12px;
  text-decoration: none;
}
nav a:hover {
  color: red;
}
```

### 混入 Mixins 

使用說明：將經常被重複使用的程式碼獨立撰寫，以 `@mixin` 語法包裝起來，需要時透過 `@include` 引用，即可根據不同參數來設定相似的樣式，常用於 width、height、flex-center 等。

+ 編譯前 SCSS：`@mixin` 可傳入參數

```sass=
// 經常重複使用的樣式
@mixin transform($property) {
  -webkit-transform: $property;
  -ms-transform: $property;
  transform: $property;
}

// 需要套用樣式的程式碼
.box { 
  @include transform(rotate(30deg));
}
.avatar { 
  @include transform(rotate(90deg));
}
```

+ 編譯後 CSS：需注意可能出現大量重複的程式碼

```css=
.box {
  -webkit-transform: rotate(30deg);
  -ms-transform: rotate(30deg);
  transform: rotate(30deg);
}
.avatar {
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
```

### 繼承 Extend/Inheritance

使用說明：當許多選擇器具有相同樣式時，可透過`%` 佔位符號宣告，將所有相同樣式內容合併，再以 `@extend` 來引入使用。

+ 編譯前 SCSS：需注意有被 `@extend` 的 class 才會被編譯成 CSS 程式碼，並且整合到共用樣式

```sass=
/* This CSS will print because %message-shared is extended. */
%message-shared {
  border: 1px solid #ccc;
  padding: 10px;
  color: #333;
}

// This CSS won't print because %equal-heights is never extended.
%equal-heights {
  display: flex;
  flex-wrap: wrap;
}

.message {
  @extend %message-shared;
}

.success {
  @extend %message-shared;
  border-color: green;
}

.error {
  @extend %message-shared;
  border-color: red;
}

.warning {
  @extend %message-shared;
  border-color: yellow;
}
```

+ 編譯後 CSS：使用 `%message-shared` 佔位符號進行宣告的 class，並不會產生實體對象
```css=
/* This CSS will print because %message-shared is extended. */
.message, .success, .error, .warning {
  border: 1px solid #ccc;
  padding: 10px;
  color: #333;
}

.success {
  border-color: green;
}

.error {
  border-color: red;
}

.warning {
  border-color: yellow;
}
```

### 比較：`@mixin` 和 `@extend` 使用時機

使用 `@mixin` 的好處，是減少重複撰寫樣式的時間，卻也可能造成編譯後的 CSS 樣式大量重複，使檔案異常肥大。

這時可以改用有類似效果的 `@extend`，同樣能解決重用問題，搭配 placeholder 佔位選擇器，將目標對象進行合併而非載入。

而 `@mixin` 和 `@extend` 兩者的使用時機與差異，可從下列兩點來思考：
+ 是否需傳遞參數
+ 是否需考慮編譯後 CSS 大小

### 模組 Modules

使用說明：透過 `@import` 或 `@use` 語法，可將 SCSS 以模組化的形式，從其他 SCSS 檔案引入需要的樣式。

> 2026 年注意：撰文當時 `@use` 還未被所有工具支援，但現在情況已反過來——**`@import` 已於 2024 年（Dart Sass 1.80）正式棄用**，使用時會出現警告，並預計在 Dart Sass 3.0 移除。新專案請一律使用 `@use`（搭配 `@forward` 轉出模組），詳見[官方說明](https://sass-lang.com/documentation/breaking-changes/import/)。

+ 編譯前 SCSS：要作為模組載入的 SCSS 檔案，名稱必須帶有底線，例如 `_base.scss`。

```sass=
// ./_base.scss
$font-stack:    Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
```

使用 `@import`：會全部導入樣式，有可能產生命名衝突的狀況：

```sass=
// styles.scss
@import 'base';
```

使用`@use`：代表「參照」，只選擇需要的部分使用，並戴上模組名稱來呼叫，降低衝突的可能性：

```sass=
// styles.scss
@use 'base';

.inverse {
  background-color: base.$primary-color;
  color: white;
}
```

+ 編譯後 CSS

```css=
body {
  font: 100% Helvetica, sans-serif;
  color: #333;
}

.inverse {
  background-color: #333;
  color: white;
}
```


參考資料：
+ [Sass/SCSS 基本語法介紹，搞懂CSS 預處理器](https://tw.alphacamp.co/blog/css-preprocessor-sass-scss)
+ [SASS教學 ＋SCSS：CSS 再進化，掌握語法攻略](https://frankknow.com/sass-tutorial/)
+ [SASS/SCSS 簡介](https://ithelp.ithome.com.tw/articles/10243235)
+ [Sass / SCSS 預處理器 - @entend 繼承樣式與 Placeholder 佔位符選擇器](https://awdr74100.github.io/2020-06-03-scss-extend/)

## 延伸閱讀

- [【學習筆記】CSS 自訂標號圖示、段落縮排效果](/css-list-style/)
- [[week 13] 前端進階 - 如何優化執行 CSS 效能](/css-optimization/)
- [[week 13] 前端工具之二 - CSS 預處理器、Babel](/sass-babel/)

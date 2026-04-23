title: '[week 3] JavaScript：ES6 語法'
author: Heidi Liu
tags:
  - JavaScript
categories:
  - 技術學習
  - JavaScript
date: 2020-07-25 15:41:00
---
> 本篇為 [[JS102] 升級你的 JavaScript 技能：ES6 + npm + Jest](https://lidemy.com/p/js102-javascript-es6-npm) 這門課程的學習筆記。如有錯誤歡迎指正！

```
學習目標：

 理解常用內建函式如何使用
 熟悉程式語法並知道如何解決基礎問題
```

<!--more-->

## What is ECMAScript？

是一種標準和規範，Javascript 這門語言就是遵循 ECMAScript 規範實作。於 2015 年發布 ECMAScript 第六版，因此又稱 ES2015 或 ES6，在 ES6 之前的版本就稱作 ES5。

目前大部分的瀏覽器均支援 ES6，但仍有少數舊型不支援。因此我們可以透過 Babel 轉譯器，將 ES6 代碼轉換為 ES5 代碼，如此就不須擔心支援問題。


## ES6 新語法

### 宣告變數 let 與 const

- ES5：使用 var
- ES6：使用 let 與 const

兩者最大差異在於：
1. 重複宣告：const 用於宣告常數，不會被重新賦值
2. 作用域不同：
    - var：作用於整個函數範圍中（function scope）
    - let 與 const：均為區塊作用域（block scope），如此可避免污染到大括號外的變數

### Template Literals 模板字串符

Template 的意思是樣板。Template Literals 可用於字串拼接。

#### ES5

- 使用單引號（`''`）或雙引號（`""`）
- 缺點：必須用 `+` 或 `,` 來串接字串，且無法換行

#### ES6

- 使用反引號（``）
- 優點：可用於多行字串拼接，也可在反引號中放入 `${變數}`



### Destructuring 解構賦值

- 可以把陣列或物件的資料解開，並擷取成獨立的變數

### Spread Operator 展開運算子

- 使用 `...` 運算子，展開陣列或物件

### Rest Parameters 其餘參數

- 使用 ... 運算子，集合剩餘的元素變成陣列，就可以在不確定陣列長度的情況下，傳入參數。

### Default Parameters 設定參數預設值

- 可以幫參數加入預設值

### 箭頭函式

- Arrow Function，縮寫為 function
- 優點：簡化程式碼，幫助閱讀

### Import & Export 引入與輸出

- 引入與輸出 module，類似 `require` 與 `module.exports` 的用法

### Babel 簡介

- 是一種 JavaScript 轉譯器，可將 ES6 新語法轉換為 ES5 舊語法
- 安裝指令：`npm install babel-loader @babel/core @babel/preset-env --save-dev`

參考資料：
1. [從博物館寄物櫃理解變數儲存模型](https://medium.com/@hulitw/variable-and-frontdesk-a53a0440af3c)
2. [[第五週] JavaScript — ES6 與 Babel](https://medium.com/@miahsuwork/%E7%AC%AC%E5%9B%9B%E9%80%B1-javascript-es6-%E8%88%87-babel-5b5e25450767)
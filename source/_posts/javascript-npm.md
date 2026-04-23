title: '[week 3] JavaScript：認識 Module & NPM 套件庫'
author: Heidi Liu
tags:
  - JavaScript
  - ES6
categories:
  - 技術學習
  - JavaScript
date: 2020-07-25 13:32:00
---
> 本篇為 [[JS102] 升級你的 JavaScript 技能：ES6 + npm + Jest](https://lidemy.com/p/js102-javascript-es6-npm) 這門課程的學習筆記。如有錯誤歡迎指正！

```
學習目標：

 理解常用內建函式如何使用
 熟悉程式語法並知道如何解決基礎問題
```

<!--more-->

---

## 何謂 Modules 模組（模塊）？

在開發過程中，若將各種功能放在一起，程式間可能會互相影響甚至產生 bug，日後也不易進行維護。

因此，我們可以將不同功能視為一個模組（Module），例如：金流、登入、權限、會員等等，再用主程式將所有模組串接起來，透過模組化統一進行管理。

![](https://i.imgur.com/di0LXxg.png)

## Ｍodeule 相關操作

### `require()`：引入模組

以引入 [Node.js 提供的 os](https://nodejs.org/api/os.html#os_os_platform) 這個模組為例：

```js
var os = require('os')      // 引入 'os' 這個模組，變數 os 可隨意命名
console.log(os.platform())
// 印出 win32，代表當前作業系統
```

![](https://i.imgur.com/ubLcpXY.png)

### `module.export`：輸出模組

- 語法：`module.exports = 任何資料型別（例如：數字、陣列、物件等）`

1. 以輸出 `double` 函式為例：

```js
// 建立一個要輸出模組的 myModule.js 檔案

function double(n) {
   return n * 2
}

module.exports = double;
```

```js
// 以 require 指令輸入模組到要使用的 js 檔案

var myModule = require('./myModule')    // 要加路徑，檔案類型 .js 通常會省略
// 不加路徑的話，其實也會自動從 node_modules 資料夾底下去找

console.log(myMoudle)        // 印出 [Function: double]
console.log(myMoudle(6))     // 印出 6
```

2. 也可利用 `exports` 輸出物件：

```js
// 在要輸出模組的 myModule.js 檔案

function double(n) {
   return n * 2
}

let obj = {
  double: double,
  triple: function triple(n) {
      return n * 3
  }
}

module.exports = obj
```

```js
// 以 require 指令輸入模組到要使用的 js 檔案

var myModule = require('./myModule')    

console.log(myModule)
// 印出 { double: [Function: double], triple: [Function: triple] }

console.log(myModule.double(2), myModule.triple(10))
// 印出 4, 30
```

3. 也可用另一個寫法：`exports.double = double`，把 `exports` 本身視為空物件，但這種方法比較少見：

```js
// 在要輸出模組的 myModule.js 檔案

function double(n) {
   return n * 2
}

exports.double = double
exports.triple = function(n) {
  return n * 3
}
```

```js
// 此種輸出方式，myModule 一定會是物件

var myModule = require('./myModule') 

console.log(myModule)
// 印出 { double: [Function: double], triple: [Function] }
console.log(myModule.double(3))
// 印出 6
```

參考資料：

1. [[第三週] Node.js 基礎 — module.exports 和 require](https://medium.com/@miahsuwork/%E7%AC%AC%E4%B8%89%E9%80%B1-node-js-%E5%9F%BA%E7%A4%8E-module-exports-%E5%92%8C-require-2f9f6915d9f0)

---

## NPM 線上套件庫

[NPM](https://www.npmjs.com/) 是 Node Package Manager 的簡稱。是用來管理 Node.js 套件的系統（Library），可以下載別人已經寫好的 Javascript 套件來使用。

> 也可使用由 Facebook 團隊開發的 [Yarn](https://yarnpkg.com/)，同樣能從 npm 安裝套件，優點是速度較快。
> 參考資料：[[Day-5] 用Yarn取代npm加速開發](https://ithelp.ithome.com.tw/articles/10191745)

### 基本指令

#### `npm -v`：查看 npm 版本。

通常在安裝 node.js 時就會一起安裝。

![npm -v](https://i.imgur.com/zZMyERG.png)

#### `npm init`：協助建立 Node.js 專案的描述檔。

也就是產生 package.json 這個檔案。

#### `npm install left-pad`：以 npm 安裝 left-pad 這個套件為例。

![npm install](https://i.imgur.com/4zvy68Z.png)

安裝同時會產生：

1. package-lock.json 檔案：記錄安裝套件的版本和依賴（dependencies）
2. node_modules 資料夾：裡面放安裝的套件

![](https://i.imgur.com/hOnLOZL.png)

package-lock.json 檔案內容如下，可從 `dependencies` 得知專案使用的套件：

![描述檔](https://i.imgur.com/YopHSs7.png)

### 版本控制會忽略 node_modules 資料夾

當安裝許多套件時，檔案會很大。若要將專案上傳到 GitHub 遠端，通常會忽略 node_modules 這個資料夾，也就是不需進行版本控制。

因為已經有 package.json 這個檔案，負責記錄該專案所安裝的套件。若從遠端下載專案時，只要再輸入 `npm install` 指令，就可安裝該專案所需套件。

![](https://i.imgur.com/nsRpDni.png)

---

## 設定 npm scripts

`package.json` 檔案中，我們可在 `scripts` 區塊加入各種指令。

### `"key": "要執行的內容＂`

以如何運行 `index.js` 這個專案為例：

`"start": "node index.js"`：代表以 start 為 key，輸入即可在 node 運行 index.js。

> 注意是使用雙引號。

![scripts](https://i.imgur.com/fvF1YuH.png)

### `npm run 'key'`

在終端機輸入 `npm run start` 即可透過 key 來運行該指令：

![npm run start](https://i.imgur.com/K3XhyO3.png)

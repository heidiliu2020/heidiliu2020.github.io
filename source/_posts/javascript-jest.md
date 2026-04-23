title: '[week 3] 初探 Jest：如何測試程式？'
author: Heidi Liu
tags:
  - JavaScript
  - Testing
categories:
  - 技術學習
  - JavaScript
date: 2020-07-25 15:34:00
---
```
學習目標：

 了解為什麼我們需要 unit test
 了解什麼是 unit test
 了解如何寫 unit test
 了解如何測試一個 function
```

<!--more-->

測試程式的作用是「模擬外部如何使用目標程式，驗證目標程式的行為是否符合預期」。

## 利用 `console.log()` 測試

在前面幾個章節，我們通常會使用 console.log()，來測幾個範例確認是否正確。也需要考慮到邊界條件（edge case）來進行測試。

```js
// 以測試 `repeat` 函式為例：

function repeat(str, times) {
  let result = ''
  for (let i = 0; i < times; i += 1) {
    result += str
  }
  return result
}

console.log(repeat('a', 5));          // 印出 aaaaa
console.log(repeat('z!Z!Z!!', 2));    // 印出　z!Z!Z!!z!Z!Z!!
console.log(repeat('', 3));           // 印出空字串
console.log(repeat('abc', 0));        // 印出空字串
```

接著優化測試資料：直接判斷函式執行結果是否正確。

```js
// 優化測試資料：

console.log(repeat('a', 5) === 'aaaaa');
console.log(repeat('z!Z!Z!!', 2) === 'z!Z!Z!!z!Z!Z!!'); 
console.log(repeat('', 3) === ''); 
console.log(repeat('abc', 0) === '');
// 均印出 true
```

這是最簡單的測試方法，但這麼做的缺點是很難「規模化」。我們可以利用別人寫好的框架來便利測試。

## 利用現成的框架 [Jest](https://jestjs.io/) 測試

1. 用 npm 下載 Jest：輸入指令 `npm install -save-dev jest`

![](https://i.imgur.com/P2V2LzG.png)

2. 利用模組將「測試」與「要測試的 Function」分開。

- 在要測試的檔案 index.js 加上：`module.exports = '要輸出的值'`

```js
function repeat(str, times) {
  let result = ''
  for (let i = 0; i < times; i += 1) {
    result += str
  }
  return result
}

module.exports = repeat
```

- 建立 index.test.js 檔案：`touch index.test.js`，習慣用 `test.js` 取名
並在檔案中引用 index.js 輸出的值：`var repeat = require('./引入的檔案')`

```js
// 可輸入 node index.test.js 測試是否引入成功
var repeat = require('./index')

console.log(repeat('a', 5));
// 印出 aaaaa，引入成功
```

- 在 index.test.js 加入 Jest 語法：`test('描述文字', '要做的測試')`

```js
var repeat = require('./index')

test('a 重複 5 次應該要等於', function() {
  expect(repeat('a', 5)).toBe('aaaaa');
})
```

3. 更新 package.json 檔案的 `"scripts"`：加入 `"test": "jest"`

!["test": "jest"](https://i.imgur.com/85bIvDU.png)

4. 如此即可運行 `npm run test` 進行測試，看到 PASS 可知測試有成功：

![test](https://i.imgur.com/KGT6Vht.png)

之所以要用 npm 來跑 jest，而不是直接在終端機輸入 jest 指令，是因為 jest 只安裝在該專案底下，要使用時才會拿出來用。

若只想測特定檔案，可以修改 `"scripts"`：`"test": "jest index.test.js"`，後面加上檔名。

![](https://i.imgur.com/4byHuvz.png)

或是用 `npx jest index.jest.js`，同樣能夠執行測試：

![](https://i.imgur.com/VGCuYis.png)

也可以多跑幾個測式：

```js
var repeat = require('./index')

test('a 重複 5 次應該要等於aaaaa', function() {
  expect(repeat('a', 5)).toBe('aaaaa');
});

test('abc 重複 1 次應該要等於abc', function () {
  expect(repeat('abc', 1)).toBe('abc');
});

test(' "" 重複 10 次應該要等於 ""', function () {
  expect(repeat('', 10)).toBe('');
});
```

![測試結果](https://i.imgur.com/Ief4HX8.png)

也可以把測試項目放在 `describe()` 函式裡，這種寫法會更有結構一點：

```js
// 架構：

`describe('測試 XX', function(){
  test('名稱', function() {
    expect('回傳值').toBe('預期結果');
  })
})`
```

```js
var repeat = require('./index')

describe('測試 repeat', function() {
  test('a 重複 5 次應該要等於aaaaa', function () {
    expect(repeat('a', 5)).toBe('aaaaa');
  });

  test('abc 重複 1 次應該要等於abc', function () {
    expect(repeat('abc', 1)).toBe('abc');
  });

  test(' "" 重複 10 次應該要等於 ""', function () {
    expect(repeat('', 10)).toBe('');
  });
})
```

## Unit test 單元測試

單元測試指的是測試一個工作單元（a unit of work）的行為。上述範例測試單一函式，就是一種單元測試。可用來確認每個 Unit 是否正確，也能夠進行規模化測試。

---

## 補充：如何在 Windows 上執行 Jest 也能有紅綠標籤

方法：把 `package.json` 裡的 `"script"` 中的內容改為 `"test": "jest --colors"`，FAIL 和 PASS 標籤就會是紅綠標籤。

![color](https://i.imgur.com/LaX4cI3.png)

奇怪的是，在 git commit 時都沒有問題，在執行 Jest 時卻出現亂碼。不太確定是不是因為更改 locale 才解決的，總之介面很神奇的變成中文了，可喜可賀。

![UTF-8](https://i.imgur.com/4OCokvV.png)

參考資料：

1. [Colorful output in Bash terminal does not work (--colors option) ](https://github.com/facebook/jest/issues/3877)

---

## 先寫測試再寫程式：TDD

Test-driven Development（測試驅動開發），是一種開發流程，簡言之就是「先寫測試在開發」。相較於傳統的「先開發在寫測試」模式，TDD 有幾項優點：

1. 能確保測試程式的撰寫
2. 從使用方觀點切入，有助於在開發初期釐清程式介面如何設計
3. 便於日後 Debug

## 實作 TDD

可利用 Jest 模組，先建立 `test()` 架構，再來撰寫主要程式碼。步驟可參考：[TDD 開發五步驟，帶你實戰 Test-Driven Development 範例](https://tw.alphacamp.co/blog/tdd-test-driven-development-example)

### 步驟一、選定一個目標功能，來新增測試案例

先寫好測試預期結果，並盡量列出邊界條件。在這個步驟還不會撰寫目標程式內容。這裡用 `reverse` 函式為例：

```js
// 先寫出預期結果：

var reverse = require('./index')

describe('測試 reverse', function() {
  test('123 reverse 要等於 321', function () {
    expect(reverse('123')).toBe('321');
  });

  test('!!! reverse 要等於 !!!', function () {
    expect(reverse('!!!')).toBe('!!!');
  });

  test(' "" reverse 要等於 ""', function () {
    expect(reverse('')).toBe('');
  });
})
```

### 步驟二、執行測試，得到 Failed（紅燈）

因為還沒撰寫目標程式，結果就會是 Failed。此步驟目的是確保測試程式可執行，沒有語法錯誤。

![運行測試](https://i.imgur.com/A38CQ2C.png)

### 步驟三、實作「最低限度」的產品程式

開始寫程式，以能夠通過測試為目標，不求將程式碼優化一步到位。完成到一個階段就可運行 jest 查看是否有錯誤：

```js
//開始寫程式

function reverse(str) {
  let result = ''
  for (let i = str.length - 1; i >= 0; i -= 1) {
    result += str[i]
  }
  return result
}

module.exports = reverse
```

### 步驟四：再次執行測試，得到 Passed（綠燈）

在這個階段，即完成一個可運作且正確的程式版本，包含產品程式和測試程式。

![Passed](https://i.imgur.com/dJHNZ1j.png)

### 步驟五：重構程式

最後是優化「產品程式」和「測試程式」的程式碼，因為測試程式也是專案需維護的一部份。如此即可提升程式的可讀性、可維護性、擴充性。


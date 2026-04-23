title: 【學習筆記】JavaScript 的浮點數計算、平方根
author: Heidi Liu
tags:
  - JavaScript
  - Front-End
categories:
  - 技術學習
  - JavaScript
date: 2024-06-17 11:28:00
---

最近又開始用 [Codewars](https://www.codewars.com/dashboard) 來練習刷題，也嘗試開一個 Repository：[codewars-challenges](https://github.com/heidiliu2020/codewars-challenges) 記錄作答結果，蠻喜歡這種能夠慢慢升級的感覺，答題結束還能參考其他人的解法，才恍然大悟原來還有更簡潔的思路。

發現自己對於一些 JavaScript 函式使用還是不太熟，把之前寫過的筆記重新複習過，本篇主要整理 JS 常見的內建函式，列表如下：

<!--more-->

+ Math.floor(x)：無條件捨去，回傳「小於等於」所給數字的最大整數
+ Bitwise NOT (~)：位元反向運算子（波浪號）
+ Math.ceil(x)：無條件進位，回傳「大於等於」所給數字的最小整數
+ Math.round(x)：四捨五入
+ toFixed(x)：四捨六入五留雙
+ Math.sqrt(x)：返回一個數的平方根
+ Math.abs(x)：返回一個數的絕對值

## [Math.floor(x)](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Math/floor)：無條件捨去，回傳「小於等於」所給數字的最大整數

```javascript=
Math.floor(.95);    // 0
Math.floor(4);      // 4
Math.floor(7.004);  // 7
Math.floor(-0.95);  // -1
Math.floor(-4);     // -4
Math.floor(-7.004); // -8
```

## [Bitwise NOT](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_NOT) (`~`)：位元反向運算子（波浪號）

+ Bitwise NOT（`~`）作用是將數字 `x` 轉換為 `-(x + 1)`
+ Double Bitwise NOT(`~~`)：雙位元元反向運算子（兩個波浪號），對正數的作用類似 `Math.floor(x)` 的無條件捨去，但對負數則結果不同

```javascript=
~10    // -11
~-10   // 9
~10.5  // -11
~-10.5 // 9

~~10    // 10
~~-10   // -10
~~10.5  // 10
~~-10.5 // -10
```

## [Math.ceil(x)](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Math/ceil)：無條件進位，回傳「大於等於」所給數字的最小整數

```javascript=
Math.ceil(.95);     // 1
Math.ceil(4);       // 4
Math.ceil(7.004);   // 8
Math.ceil(-0.95);   // -0
Math.ceil(-7.004);  // -7
```

## [Math.round(x)](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Math/round)：四捨五入

```javascript=
Math.round(20.49);  // 20
Math.round(20.5);   // 21
Math.round(-20.5);  // -20
Math.round(-20.51); // -21
```

## [toFixed(x)](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed)：四捨六入五留雙

+ 以字串返回，精確至「小數點後」的數字，小數部分依指定長度補充零

```javascript=
1.23.toFixed(2);    // '1.23'
1.234.toFixed(2);   // '1.23'
1.235.toFixed(2);   // '1.24'
1.236.toFixed(2);   // '1.24'
1.244.toFixed(2);   // '1.24'
1.245.toFixed(2);   // '1.25'
1.246.toFixed(2);   // '1.25'

(36).toFixed(4)     // '36.0000'
```


## [Math.sqrt(x)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/sqrt)：返回一個數的平方根

```javascript=
Math.sqrt(2);   // 1.4142135623730951
Math.sqrt(4);   // 2
Math.sqrt(-2);  // NaN
Math.sqrt(0);   // 0
```

## [Math.abs(x)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/abs)：返回一個數的絕對值

```javascript=
function difference(a, b) {
  return Math.abs(a - b);
}

difference(3, 5);    // 2
difference(5, 3);    // 2
difference(-5, -3);  // 2
```

## Reference

+ [[JS] JavaScript 運算子（Operator）](https://pjchender.dev/javascript/js-operator/)
+ [JavaScript 四捨五入、無條件捨去、無條件進位](http://www.aua.com.tw/blogger/?Pid=1173)
+ [使用 JavaScript 的數字時的常見錯誤](https://blog.huli.tw/2022/03/14/javascript-number/)

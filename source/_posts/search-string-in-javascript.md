title: 【學習筆記】JavaScript 尋找字串的方法：includes/indexOf/search/match
author: Heidi Liu
tags:
  - JavaScript
  - Front-End
categories:
  - 技術學習
  - JavaScript
date: 2023-02-21 16:33:00
---

![](https://i.imgur.com/nZfxv6r.jpg)
> Photo by <a href="https://unsplash.com/@rocinante_11?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Mick Haupt</a> on <a href="https://unsplash.com/photos/eQ2Z9ay9Wws?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
在處理資料時，查找字串是一種常見的操作，JavaScript 提供不同的方法來搜索字串。其中，最常用的方法包括：search、indexOf、includes 和 match，能夠辨別字串裡是否有想要查找的文字：

- String.prototype.search( )
- String.prototype.indexOf( )
- String.prototype.match()
- String.prototype.includes()

接下來會比較這四種方法的不同之處，以及使用範例。

<!--more-->

---

## [String.prototype.search( )](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/search)：檢測字串是否包含，有的話回傳 index，否則回傳 -1

- 搜索指定字符串，並返回匹配字串第一個字的索引值
- 若找不到，則返回 -1
- 可支援正則表達式

```jsx
search(regexp)
```

> 關於正則表達式的用法，可參考這篇筆記：[【學習筆記】JavaScript：Regex 正則表達式](https://heidiliu2020.github.io/regex/)。

使用範例：

- 字串符匹配

```jsx
let str = "Hello world!";
let position = str.search("world");

console.log(position);   // 6
```

- 正則表達式匹配

```jsx
let str = "Say hello to Hello World!";
let rule1 = str.search(/[A-Z]/);    // 符合大寫字母 A 到 Z
let rule2 = str.search(/Hello/);    // 符合 Hello
let rule3 = str.search(/Hello/i);   // i 代表不區分大小寫

console.log(rule1);  // 0
console.log(rule2);  // 13
console.log(rule3);  // 4
```

## [String.prototype.indexOf()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/indexOf)：檢測字串是否包含，有的話回傳 index，否則回傳 -1

- 搜索指定字符串，並返回匹配字串第一個字的索引值
- 若沒有找到，則返回 -1
- 第二個參數 position 為選填屬性，代表從哪個 index 找起
- 與 search() 方法類似，差別在於 indexOf() 不支援正則表達式

```jsx
indexOf(searchString, position)
```

使用範例：

- 找特定字符的 index

```jsx
let str = "Say hello to hello world!";
let position1 = str.indexOf("hello");
let position2 = str.indexOf("hello", 10);
let position3 = str.indexOf("Hello", 10);
let position4 = str.indexOf("zzz");

console.log(position1);    // 4
console.log(position2);    // 13
console.log(position3);    // -1
console.log(position4);    // -1
```

## [String.prototype.match()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)：尋找並取出內容，有的話以陣列回傳，否則回傳 null

- 搜索指定字符串，並返回一個或多個與指定值匹配的數組
- 若找不到則返回 null
- 支援正則表達式

```jsx
string.match(searchvalue)
string.match(regexp)
```

使用範例：

- 字符串匹配

```jsx
let str = "hello world";
let result1 = str.match("hello");
let result2 = str.match("Hello");

console.log(result1);  // ['hello', index: 0, input: 'hello world', groups: undefined]
console.log(result2);  // null

```

- 正規表達式匹配：需注意要加上 `g` 標誌，才會返回匹配的所有結果

找指定字串：

```jsx
let str = "Say hello to hello World!";
let result1 = str.match(/hello/);
let result2 = str.match(/hello/g);

console.log(result1);  // ['hello', index: 4, input: 'Say hello to hello World!', groups: undefined]
console.log(result2);  // ['hello', 'hello']

```

找大寫字母：

```jsx

const paragraph = 'Hello, I am fine. Thank you.';
const regex = /[A-Z]/;
const globalReg = /[A-Z]/g;

console.log(paragraph.match(regex));      // ['H', index: 0, input: 'Hello, I am fine. Thank you.', groups: undefined]
console.log(paragraph.match(globalReg));  // ["H", "I", "T"]
```

## [String.prototype.includes()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/includes)：判斷字串中是否包含指定字串

- 找到匹配字串返回 true；否則返回 flase
- 不支援正則表達式

```jsx
string.includes(searchvalue, start)
```

使用範例：

```jsx
let str = "Hello world!";
let isPresent1 = str.includes("world");
let isPresent2 = str.includes("zzz");

console.log(isPresent1); // true
console.log(isPresent2); // false
```

## 小結

過去曾整理過陣列遍歷的相關筆記：

- [【學習筆記】JavaScript 的陣列遍歷（ㄧ）：for/for...of/for...in/forEach](https://heidiliu2020.github.io/javascript-for-loop/)
- [【學習筆記】JavaScript 的陣列遍歷（二）：forEach/map/filter/every/some/reduce](https://heidiliu2020.github.io/javascript-native-array/)

專案中時常需要去搜尋特定字串，來達成特定目的。翻找筆記時，才發現自己竟然還沒有整理過這幾個 JavaScript 提供的方法的差異。

也藉由這個機會，又好好重新複習正則表達式的一些觀念，雖然很多時候是需要用到的時候再查就好，但果然原生的底子還是基礎中的基礎。

此外，也體驗了最近正夯的 [ChatGPT](https://openai.com/blog/chatgpt/)，給一段關鍵字寫出來的文章，差不多就完成了八七分架構，只需要再多補充一些觀念，一篇筆記就熱騰騰的誕生了ಠ_ಠ

![](https://i.imgur.com/Fd2VwfC.png)

雖然這項功能方便又快速，結果卻不一定 100% 正確，有時也會出現一些瞎掰的，甚至與事實相差甚遠的回答；因此該如何善用這項工具，辨別結果並實際應用在工作上的開發、測試、寫文件等等，想必是使用者需要學習的課題吧。

## Reference

- [認識 search、indexOf、includes 三種搜尋字串的相關方法 | by Lai | UnaLai | Medium](https://medium.com/unalai/%E8%AA%8D%E8%AD%98-search-indexof-includes-%E4%B8%89%E7%A8%AE%E6%90%9C%E5%B0%8B%E5%AD%97%E4%B8%B2%E7%9A%84%E7%9B%B8%E9%97%9C%E6%96%B9%E6%B3%95-704856176952)
- [<JavaScript>字串的處理方式. 覺得自己每次都忘記字串、物件、陣列的處理方式，決定要來整理這些的用法。 | by 拉拉 | 拉拉的程式筆記 | Medium](https://medium.com/%E6%8B%89%E6%8B%89%E7%9A%84%E7%A8%8B%E5%BC%8F%E7%AD%86%E8%A8%98/%E5%AD%97%E4%B8%B2%E7%9A%84%E8%99%95%E7%90%86%E6%96%B9%E5%BC%8F-793037c1182)
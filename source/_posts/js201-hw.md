title: '[week 16] JavaScript 進階 - 作業練習'
author: Heidi Liu
tags:
  - JavaScript
categories:
  - 技術學習
  - JavaScript
date: 2020-10-25 00:30:00
---
- hw1：Event Loop
- hw2：Event Loop + Scope
- hw3：Hoisting
- hw4：What is this?
<!--more-->

## hw1：Event Loop

在 JavaScript 裡面，一個很重要的概念就是 Event Loop，是 JavaScript 底層在執行程式碼時的運作方式。請你說明以下程式碼會輸出什麼，以及盡可能詳細地解釋原因。

```
console.log(1)
setTimeout(() => {
  console.log(2)
}, 0)
console.log(3)
setTimeout(() => {
  console.log(4)
}, 0)
console.log(5)
```

### 輸出結果

```js
1
3
5
2
4
```

### 執行流程

1. 將 `console.log(1)` 放入 Call Stack 並直接執行，印出 1，執行結束後移除
2. 將 `setTimeout(() => { console.log(2) }, 0)` 放入 Call Stack，透過 Web API，在瀏覽器設定計時器為 0，直到倒數結束，將 `() => { console.log(2) }` 放到 Callback Queue 等待執行，setTimeout 執行結束後從 Call Stack 移除
3. 將 `console.log(3)` 放入 Call Stack 並直接執行，印出 3，執行結束後移除
4. 將 `setTimeout(() => { console.log(4) }, 0)` 放入 Call Stack，透過 Web API，在瀏覽器設定計時器為 0，直到倒數結束，將 `() => { console.log(4) }` 放到 Callback Queue 等待執行，setTimeout 執行結束後從 Call Stack 移除
5. 將 `console.log(5)` 放入 Call Stack 並直接執行，印出 5，執行結束後移除
6. 當 Event Loop 偵測到 call stack 為空時，依序將 Callback Queue 的任務丟到 Call Stack 執行
7. 執行 `() => { console.log(2) }`，再執行 `console.log(2)`，印出 2，執行結束後移除
8. 接著執行 `() => { console.log(4) }`，再執行 `console.log(4)`，印出 4，執行結束後移除

---

## hw2：Event Loop + Scope

請說明以下程式碼會輸出什麼，以及盡可能詳細地解釋原因。

```js
for(var i=0; i<5; i++) {
  console.log('i: ' + i)
  setTimeout(() => {
    console.log(i)
  }, i * 1000)
}
```

### 輸出結果

```js
i: 0
i: 1
i: 2
i: 3
i: 4
5
5
5
5
5
```

### 執行流程

1. 將 for 迴圈放入 Call Stack 並開始執行，宣告變數 i = 0，判斷 i 是否小於 5，是，進入第一圈迴圈
2. 將 `console.log('i: ' + 0)` 放入 Call Stack 並直接執行，印出 i: 0
3. 將 `setTimeout(() => { console.log(0) }, 0 * 1000)` 放入 Call Stack，透過 Web API，在瀏覽器設定計時器為 0 ms，直到倒數結束，將 `() => { console.log(0) }` 放到 Callback Queue 等待執行，setTimeout 執行結束後從 Call Stack 移除
4. 第一圈迴圈結束，將 i + 1
5. i = 1，判斷 i 是否小於 5，是，進入第二圈迴圈
6. 將 `console.log('i: ' + 1)` 放入 Call Stack 並直接執行，印出 i: 1
7. 將 `setTimeout(() => { console.log(i) }, 1 * 1000)` 放入 Call Stack，透過 Web API，在瀏覽器設定計時器為 1000 ms ，直到倒數結束，將 `() => { console.log(i) }` 放到 Callback Queue 等待執行，setTimeout 執行結束後從 Call Stack 移除
8. 第二圈迴圈結束，將 i + 1
9. i = 2，判斷 i 是否小於 5，是，進入第二圈迴圈
10. 將 `console.log('i: ' + 2)` 放入 Call Stack 並直接執行，印出 i: 2
11. 將 `setTimeout(() => { console.log(i) }, 2 * 1000)` 放入 Call Stack，透過 Web API，在瀏覽器設定計時器為 2000 ms ，直到倒數結束，將 `() => { console.log(i) }` 放到 Callback Queue 等待執行，setTimeout 執行結束後從 Call Stack 移除
12. 第二圈迴圈結束，將 i + 1
13. i = 3，判斷 i 是否小於 5，是，進入第三圈迴圈
14. 將 `console.log('i: ' + 3)` 放入 Call Stack 並直接執行，印出 i: 3
15. 將 `setTimeout(() => { console.log(i) }, 3 * 1000)` 放入 Call Stack，透過 Web API，在瀏覽器設定計時器為 3000 ms ，直到倒數結束，將 `() => { console.log(i) }` 放到 Callback Queue 等待執行，setTimeout 執行結束後從 Call Stack 移除
16. 第三圈迴圈結束，將 i + 1
17. i = 4，判斷 i 是否小於 5，是，進入第四圈迴圈
18. 將 `console.log('i: ' + 4)` 放入 Call Stack 並直接執行，印出 i: 4
19. 將 `setTimeout(() => { console.log(i) }, 4 * 1000)` 放入 Call Stack，透過 Web API，在瀏覽器設定計時器為 4000 ms ，直到倒數結束，將 `() => { console.log(i) }` 放到 Callback Queue 等待執行，setTimeout 執行結束後從 Call Stack 移除
20. 第四圈迴圈結束，將 i + 1
21. i = 5，判斷 i 是否小於 5，否，跳出迴圈，執行結束後從 Call Stack 移除
22. 當 Event Loop 偵測到 call stack 為空時，依序將 Callback Queue 的任務丟到 Call Stack 執行
23. 執行第一個 `() => { console.log(i) }`，再執行 `console.log(i)`，在 function 的 EC 中找不到 i，往上一層 EC 找，找到 i = 5，印出 5，執行結束從 Call Stack 移除
24. 執行第二個 `() => { console.log(i) }`，再執行 `console.log(i)`，在 function 的 EC 中找不到 i，往上一層 EC 找，找到 i = 5，印出 5，執行結束從 Call Stack 移除
25. 執行第三個 `() => { console.log(i) }`，再執行 `console.log(i)`，在 function 的 EC 中找不到 i，往上一層 EC 找，找到 i = 5，印出 5，執行結束從 Call Stack 移除
26. 執行第四個 `() => { console.log(i) }`，再執行 `console.log(i)`，在 function 的 EC 中找不到 i，往上一層 EC 找，找到 i = 5，印出 5，執行結束從 Call Stack 移除
27. 執行第五個 `() => { console.log(i) }`，再執行 `console.log(i)`，在 function 的 EC 中找不到 i，往上一層 EC 找，找到 i = 5，印出 5，執行結束從 Call Stack 移除


---

## hw3：Hoisting

請說明以下程式碼會輸出什麼，以及盡可能詳細地解釋原因。

```js
var a = 1
function fn() {
  console.log(a)    // undefined
  var a = 5
  console.log(a)    // 5
  a++　
  var a
  fn2()
  console.log(a)     // 6
  function fn2() {
    console.log(a)     // 20 
    a = 20
    b = 100
  }
}
fn()
console.log(a)     // 1
a = 10
console.log(a)     // 10
console.log(b)     // 100
```

### 輸出結果

```js
undefined
5
6
20
1
10
100
```

### 執行流程

1. 開始執行程式，建立 global EC 並初始化 VO

```js
global EC
  VO {
    fn: function,
    a: undefined
  }
}
```

2. 執行第一行程式碼，宣告變數 a 並賦值為 1

```js
global EC {
  VO {
    fn: function,
    a: 1
  }
}
```

3. 呼叫 fn()，建立 fn EC 並初始化 AO，變數宣告會提升 `var = a`

```js
fn EC {
  AO {
    fn2: function,
    a: undefined
  }
}
```

4. 進入 function fn 並執行 console.log(a)，找到 fn AO 中 a = undefined，印出 undefined
5. 執行 var a = 5，查看 fn EC 是否有 a，找到 a，將 a 賦值為 5

```js
fn EC {
  AO {
    fn2: function,
    a: 5
  }
}
```

6. 執行 console.log(a)，找到 fn AO 中 a = 5，印出 5
7. 執行 a++，查看 fn EC 是否有 a，將 a 賦值為 6

```js
fn EC {
  AO {
    fn2: function,
    a: 6
  }
}
```

8. 已經宣告過變數 a，忽略 `var a` 
9. 呼叫 fn2()，建立 fn EC 並初始化 AO

```js
fn2 EC {
  AO {
    // 沒有進行任何宣告
  }
}
```

10. 進入 function fn2 並執行 console.log(a)，查看 fn2  AO 沒有找到 a；往上一層 fn AO 找，找到 a = 6，印出 6
11. 執行 a = 20，在 fn2 AO 沒有找到 a；往上一層 fn AO 找，找到 a，並賦值 a 為 20

```js
fn EC {
  AO {
    fn2: function,
    a: 20
  }
}
```

12. 執行 b = 100，在 fn2 AO 沒有找到 b；往上一層 fn AO 找，沒有找到 b；再往上一層 global VO 找，沒有找到 b。因為是在非嚴格模式執行程式碼，會在 global VO 宣告變數 b 並賦值為 100

```js
global EC
  VO {
    fn: function,
    a: 1
    b: 100
  }
}
```

13. function fn2 執行結束，移除 fn2 EC，回到 fn EC 執行其餘程式碼
14. 執行 console.log(a)，找到 fn AO 中 a = 20，印出 20
15. function fn 執行結束，移除 fn EC，回到 global EC 執行其餘程式碼
16. 執行 console.log(a)，找到 global VO 中 a = 1，印出 1
17. 執行 a = 10，查看 global EC 是否有 a，找到 a，將 a 賦值為 10

```js
global EC
  VO {
    fn: function,
    a: 10
    b: 100
  }
}
```

18. 執行 console.log(a)，找到 global VO 中 a = 10，印出 10
19. 執行 console.log(b)，找到 global VO 中 b = 100，印出 100

---

## hw4：What is this?

請說明以下程式碼會輸出什麼，以及盡可能詳細地解釋原因。

```js
const obj = {
  value: 1,
  hello: function() {
    console.log(this.value)
  },
  inner: {
    value: 2,
    hello: function() {
      console.log(this.value)
    }
  }
}
  
const obj2 = obj.inner
const hello = obj.inner.hello
obj.inner.hello()    // 2
obj2.hello()    // 2
hello()     // undefined
```

### 輸出結果

```js
2
2
undefined
```

### 執行流程

1. `obj.inner.hello()`

可看成 `.call()` 的形式：`obj.inner.hello.call(obj.inner)`，this 會是傳入的參數，也就是 `obj.inner`，因此 `obj.inner.value` 得到的結果是 2。

2. `obj2.hello()`

和上一題相同，可看成 `.call()` 的形式：`obj2.hello.call(obj2)`，this 就會是 `obj2`，又因 `obj2 = obj.inner`，因此結果同樣會是 2。

3. `hello()`

在不需要的地方呼叫 this 時，this 會被指定為全域物件。依照執行環境不同，其值也會改變，例如在瀏覽器執行會是 Window，在 node.js 執行則是會是 Global。
若是在`'use strict';`（嚴格模式）下執行，this 的值會是 undefined。

## 這週學了一大堆以前搞不懂的東西，你有變得更懂了嗎？請寫下你的心得。

### 這週的學習筆記

- [[week 16] JavaScript 進階 - 關於變數與資料型態](https://hackmd.io/@Heidi-Liu/note-js201-data-type)
- [[week 16] JavaScript 進階 - 初探 Hoisting & Execution Context](https://hackmd.io/@Heidi-Liu/note-js201-hoisting)
- [[week 16] 淺談 JavaScript：同步與非同步 & Callback Function & Event Loop](https://hackmd.io/@Heidi-Liu/note-javascript-callback)
- [[week 16] JavaScript 進階 - 什麼是閉包？探討 Closure & Scope Chain](https://hackmd.io/@Heidi-Liu/note-js201-closure)
- [[week 16] JavaScript 進階 - 物件導向 & Prototype](https://hackmd.io/@Heidi-Liu/note-js201-oop-prototype)
- [[week 16] JavaScript 進階 - What is this？](https://hackmd.io/@Heidi-Liu/note-js201-this)

### 學習心得

這一週的知識量其實蠻大的，從複習 JavaScript 的變數與資料型態，等號賦值與記憶體位置等等，在第二週的課程也有提到相關概念，到了第十六週則是要去瞭解程式背後是如何運作的。

#### Hoisting & Execution Contexts & Variable Object

從理解什麼是 Hoisting（提升），瞭解我們為什麼需要提升，再延伸到運作原理。過程中建立的 Execution Contexts（執行環境）、與之對應的 Variable Object（變數物件）等等，其實涉及到有關 JavaScript 的範圍非常廣。

除了課堂影片提到的內容，自己也上網查了許多有關執行環境、執行堆疊的資料，雖然花費不少時間，卻也藉由瞭解 JavaScript 的編譯與執行過程，從建立到執行階段，加深對整個架構的理解。

#### Event Loop

在閱讀完 [JavaScript 中的同步與非同步（上）：先成為 callback 大師吧！](https://blog.huli.tw/2019/10/04/javascript-async-sync-and-callback/) 這篇文章，原本對 callback 概念薄弱的自己，對同步與非同步又有了新的一層認識。

尤其是才剛接著學完有關 Hoisting 的運作原理，在瞭解什麼是執行環境以後，再回來看 Event Loop 似乎也更能夠理解當中的執行流程。

也想到再次看到 Node.js 是 JavaScript 的 runtime（執行環境）這句話時，會想到 Execution Context 的中文也被翻成執行環境，但其實兩者指的對象不同。前者指的是「執行時系統」（run-time system）；後者指的是 JavaScript 在執行時會建立的環境，又可分為全域與函式執行環境。翻成中文的壞處就是容易撞名混淆，還是讓自己盡量去理解原文的意思。

#### Closure & Scope

在學到 Closure（閉包）時，發現其實花了很多時間在瞭解有關 Scope（作用域）的概念。也是在這一單元瞭解到，原來之前在課程中學到的非同步操作，當中的 callback 其實就和閉包有關，有關 callback 的觀念真的非常重要，也難怪這些觀念會不斷在課程中被提到。

此外也瞭解到，閉包在框架中很常會使用到，透過閉包的方式，就能夠避免汙染全域變數或是記憶體洩漏等問題。

一開始之所以沒辦法很快理解，或許就是沒有把這些觀念融會貫通，都是一個環節接著另一個環節，就和 Scope Chain 一樣，會需要往上一層去找出需要的拼圖。

#### 物件導向 & prototype

其實在學習 JavsScript 之前，一直以為物件導向和 this 是能夠畫上等號的（三個的那種）。直到實際學到物件導向以後，才瞭解到物件導向中有許多觀念，其實和在之前學到的 Hoisting、Closure 有很大的關聯。此外，物件導向其實應用在許多現代的程式語言，以物件導向的方式進行開發。

物件導向程式的寫法，基本上可分為三部分：

1. 定義物件類別（class）。例如：`class Dog`
2. 定義物件類別中的屬性與方法。例如：可使用 `dog.name` 存取屬性，使用 `dog.sayHello()` 存取方法
3. 定義物件之間的行為，也就是主程式

之所以需要物件導向，最重要的目的就是把資料（屬性）與函式（方法）結合在一起，定義出物件模型，這麼做有幾個優點：

- 便於重複使用程式碼
- 能夠隱藏程式內部資訊
- 透過模組化來簡化主程式邏輯

而這些概念，其實也就是先前談到有關物件導向的三大特性，並且三者具有次序性，沒有封裝就不可能有繼承、沒有繼承就不可能有多型：

- 封裝（Encapsulation）：
  - 藉由把程式包成類別，能夠隱藏物件內容
  - 避免程式間互相干擾，也利於後續維護
- 繼承（Inheritance）：
  - 子層能夠繼承使用父層的屬性和方法，並且加以微調
  - 能夠重複使用程式碼
- 多型（Polymorphism）：
  - 父層可透過子層衍伸成多種型態，接著子層可藉由覆寫父層的方法來達到多型
  - 可增加程式架構的彈性與維護性

藉由瞭解什麼是物件導向，為什麼需要物件導向以後，對整體架構似乎又更加清楚一些。過程中也查了許多資料，在碰到新的名詞時總會感到慌張，像是 constructor（建構子）、prototype（原型）、instance（實例）等等，其實只要能夠先瞭解定義是什麼，就不難繼續理解整體架構。

最後，在找相關資料的時候，有在這篇[網誌](https://igouist.github.io/post/2020/07/oo-5-polymorphism/)中，看到使用泡麵的例子來比喻物件導向，因為還蠻喜歡的也記錄在這裡：

1. 由泡麵工廠製作麵和醬包，並包裝在一起，我們可以直接買來享用
2. 我們可以在泡麵中自己加料，或是不用泡的改用炒的
3. 同樣都是泡麵，卻能夠實作出不同的口味

#### What is this？

瞭解到物件導向的相關概念後，接著要理解 this 是什麼就沒那麼困難了。或許是因為在實際學 JacaScript 以前，就預設 this 是很難是高手在用的東西，透過慢慢理解物件導向與 this 的關聯，以及如何判斷 this 的值，似乎也感覺到自己的進化，對於未知的恐懼總是需要克服的。

關於 this 的重點，就是記得 this 的值和程式碼在哪無關，而是和怎麼呼叫有關係。

總結前面提到的觀念，其實 this 大致可分成四種綁定方式：

- 默認綁定

在和物件導向無關的情況下，this 會被指定為全域物件。又依照執行環境不同，其值會是 global 或 window，而在嚴格模式下會是 undefined：

```javascript=
function test() {
  console.log(this);     // Window 
}
test();
```

- 隱式綁定

若在 function 中， this 有被某物件指定為屬性並呼叫，this 就是呼叫 function 的物件。以下方範例來說 this 就是 obj：

```javascript=
function func() {
  console.log(this.a);
}

var obj = {
  a: 4,
  test: func
};

obj.test();  // 4
```

- 顯示綁定

若是透過 `.call()`、`.apply()` 或 `.bind()` 方式指定 this，this 就會是傳入的參數：

```javascript=
var obj = {
  a: 10,
  test: function () {
    console.log(this);
  }
}

obj.test.call(obj)
obj.test.apply(obj)

// 第一種寫法：直接呼叫 function
obj.test.bind(obj)();
// 第二種寫法：先宣告，再呼叫
const bindTest = obj.test.bind(obj);
bindTest();  

// 均印出: { a: 10, test: [Function: test] }
```

- new 綁定

透過建構函式 new 出一個 instance，this 就會是 instance 物件本身：

```javascript=
class Dog {
  constructor(name) {
    this.name = name;
    console.log(this);       // Dog {name: "dog A"}
    console.log(this.name);  // dog A
  }
}

var a = new Dog('dog A');
```

- 例外：箭頭函式中的 this 是看程式碼定義在哪，和怎麼呼叫沒關係。

#### 總結

終於學到傳說中的物件導向，以及面對 JavaScript 中的大魔王 this。還記得在開始程式導師計畫之前，有在 Udemy 買過 JavaScript: Understanding the Weird Parts（中譯：JavaScript 全攻略：克服 JS 的奇怪部分）這堂課，但其實那時候也沒看多少，現在想想當初連基礎都還沒打穩，難怪會不知道自己在聽什麼XD。上網查過資料會發現蠻多類似的標題，不外乎是「你所不知道的 JS」、「其實 JS 跟你想的不一樣」等等，所以 JavaScript 到底是怪在哪？！在學完 JavaScript 基礎之後，還只是理解這個程式語言的皮毛而已。

把這一週的筆記整理完，寫作業的時候也感覺踏實多了，總算是釐清  Event Loop、Hoisting、Closure、物件導向和 this 等相關概念。或許是因為看到新名詞時總會感到害怕，會忍不住去查定義，查為什麼要這樣用，不這樣用又會有什麼影響等等，好像要先完全掌握這些名詞的意義以後，才能在繼續再下一步前進。

但實際上，在嘗試理解的過程中，有很重要的一點，就是「實作」。與其查了一堆定義和文字一翻兩瞪眼，倒不如跟著課程範例操作，實際在程式跑過一遍，知道會有怎樣的結果以後，才能理解文字的意義，然後再去試著自己變化程式碼，看看結果有沒有和自己想的一樣，到最後就差不多能夠自己寫出簡單的範例來了。

硬是要把提升、閉包、物件導向或是一些方法定義背起來，其實也記不久，看過就忘了，想想這其實也是自己的壞習慣，在還沒理解之前會想著乾脆先記起來，但隨著要學習的東西越深越廣，再用這種方法實在不是長久之計，直接來個範例吧！是最近有關學習的體悟，之後也要謹記這件事情。

總之，終於把 JavaScript 進階的相關觀念都 Run 過一遍，大致瞭解背後是如何運作，也把過去一些錯誤的觀念改正，或是終於瞭解為什麼以前想賦值給某個變數時，沒有辦法改動值等等。不過理解觀念是一回事，重要的還是如何實際應用，之後實作時也要來試著運用物件導向的概念去寫程式。

再來要繼續往下一週邁進了，繼續努力！

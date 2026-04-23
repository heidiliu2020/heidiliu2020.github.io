title: '[學習筆記] CSS 自訂標號圖示、段落縮排效果'
author: Heidi Liu
tags:
  - Front-End
  - CSS
categories:
  - 技術學習
  - Front-End
  - HTML & CSS
date: 2021-05-02 11:54:00
---
+ [CSS list-style 列表屬性
](https://www.wibibi.com/info.php?tid=CSS_list-style_%E5%88%97%E8%A1%A8%E5%B1%AC%E6%80%A7)
+ 更多項目標籤寫法參考：[CSS list-style-type](https://www.wibibi.com/info.php?tid=359)

<!--more-->

## CSS 中的標號圖示

在 HTML & CSS 中，想要建立段落標號樣式，可透過下列幾種方法：

+ 第一種：`<span>` 行內標籤
  + 可插入 icon，但用在排序會較不符合語意化

```htmlmixed=
<li><span>(1)</span>這是第一項</li>

<li><mat-icon class="cat"></mat-icon>這是一隻貓</li>
```

+ 第二種：使用 ul（無序）、ol（有序）項目標籤
  + 透過 li::before 自訂標號圖示，同樣可插入 icon

### ul li 或 ol, li 項目標籤

在 HTML 中，可根據是否需呈現排序項目，使用 ol li 標籤；若不需排序，就直接使用 ul li 標籤。

可參考以下範例：

```htmlmixed=
<!-- 無序列 -->
<ul>
　<li>星期一</li>
　<li>星期二</li>
</ul>

<!-- 有序列 -->
<ol>
　<li>星期一</li>
　<li>星期二</li>
</ul>
```

輸出效果如下：

+ 星期一
+ 星期二
1. 星期一
2. 星期二

## CSS list-style 列表屬性

CSS 列表屬性，可用來調整列表的顯示功能，也就是上述提到的 ul li 或 ol li 項目標籤。

以下介紹幾種列表屬性：

+ list-style-type：修改列表開頭符號
+ list-style-image：修改列表開頭小圖示
+ list-style-position：修改列表的顯示位置

### list-style-type 屬性：修改列表開頭顯示符號

我們可透過 `<ul>`, `<ol>` 元素的 type 屬性，改變開頭編號的種類，如以下範例：

```htmlmixed=
<!-- 小寫字母 -->
<ul style="list-style-type:lower-alpha;">
　<li>lower-alpha</li>
　<li>lower-alpha</li>
</ul>

<!-- 羅馬字母 -->
<ul style="list-style-type: lower-roman;">
  <li>lower-roman</li>
  <li>lower-roman</li>
</ul>
```

輸出效果如下：

```
a. lower-alpha
b. lower-alpha

i. lower-roman
ii. lower-roman
```

### list-style-image 屬性：修改列表開頭為小圖示

+ HTML 標籤

```htmlmixed=
<ul>
　<li>開頭符號為圖示的清單</li>
　<li>開頭符號為圖示的清單</li>
</ul>
```

+ CSS 樣式

```css=
ul li {
　list-style-image: url('圖片路徑.svg');
}
```

### list-style-position：修改列表的顯示位置

+ HTML 標籤

```htmlmixed=
<ul class="p1">
　<li>這是在標籤範圍之內顯示</li>
　<li>這是在標籤範圍之內顯示</li>
</ul>

<ul class="p2">
　<li>這是在標籤範圍之外顯示</li>
　<li>這是在標籤範圍之外顯示</li>
</ul>
```

+ CSS 樣式

```css=
/* 項目符號在 li 範圍內 */
ul.p1 {
　list-style-position: inside;
}
/* 項目符號在 li 範圍外（預設值） */
ul.p2 {
　list-style-position: outside;
}
/* 可用來確認 li 項目位置 */
li {
　border: 1px #cccccc solid;
}
```

---

## Custom List Style 自訂標號樣式

假如不想使用 ul, ol 標籤預設樣式，也可透過下列步驟來自訂標號樣式：

+ 在 ol 取消預設樣式，並自訂一個標號變數

```css=
ol {
  list-style: none;
  counter-reset: my-counter;
}
```

+ 在 ol li 使用自訂標號，可透過 text-indent 修改段落縮排：

```css=
ol li {
/*  使用自訂標號  */
  counter-increment: my-counter;
/* 段落首行縮排 */
  text-indent: -1em;
}
```

+ 透過偽元素 `li::before` 使用自訂標號樣式，例如 (1)，即可插入想要的符號．或也可以替換成 url 路徑插入圖示：

```css=
/* 代表在自訂變數前後加上 ( ) */
ol li::before {
  content: "("counter(my-counter) ")";
}
```

完成的 CSS 樣式如下：

```css=
ol {
  list-style: none;
/*  命名自訂標號變數  */
  counter-reset: my-counter;
}
ol li {
/*  使用自訂標號  */
  counter-increment: my-counter;
/* 段落首行縮排 */
  text-indent: -1em;
}
/* 以偽元素自訂標號樣式 */
ol li::before {
  content: "("counter(my-counter) ")";
  color: blue;
  font-weight: bold;
}
```

+ 以下 DEMO 樣式渲染結果：

<iframe height="265" style="width: 100%;" scrolling="no" title="Custom List Style - 自訂標號樣式" src="https://codepen.io/heidiliu2020/embed/PoWXJLv?height=265&theme-id=dark&default-tab=css,result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/heidiliu2020/pen/PoWXJLv'>Custom List Style - 自訂標號樣式</a> by Heidi-Liu
  (<a href='https://codepen.io/heidiliu2020'>@heidiliu2020</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

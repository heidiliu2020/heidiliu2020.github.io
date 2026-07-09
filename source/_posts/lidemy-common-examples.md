title: 常見重點整理 - 命名慣例 & 開發時注意事項
author: Heidi Liu
tags:
  - Lidemy
  - Front-End
  - JavaScript
  - 軟體開發
categories:
  - 技術學習
  - Lidemy
date: 2020-10-02 00:34:00

---

- 參考資料：
https://github.com/Lidemy/mentor-program-4th/blob/master/examples/common.md
<!--more-->

## 什麼是好的 code？

1. 符合命名慣例以及命名一致性
2. 合理的變數名稱

## 三種常見的命名慣例

### 駝峰式命名（Camel case）

- 就像駝峰會一高一低
- 單字之間不空格，而是直接連起來，但是連起來的第一個字要大寫
- 例如：有一個 handle add post 的 function，就會叫做 handleAddPost

駝峰又有分兩種：

1. 小駝峰（lower camel case）：開頭是小寫，就像上面的範例 handleAddPost
2. 大駝峰（upper camel case）：又被稱為 Pascal Case。開頭變成大寫，也就會變成 HandleAddPost

### 蛇型命名（Snake case）

- 蛇就是底線的意思，利用底線來連接單字，然後全部都是小寫
- 同上述範例，會變成：handle_add_post

### 烤肉串命名（Kebab case）

- Kebab 是烤肉串的意思，`-` 符號看起來就像那跟棍子
- 同上述範例，會變成：handle-add-post

認識這三種常見的命名慣例以及名詞之後，接著要來熟悉不同地方的命名慣例。也就是說，不同程式語言或是不同環境，使用的命名慣例也可能會不一樣。

需注意的是，命名慣例雖然沒有強制性，但開發時基本上都會依照這套慣例，避免寫出他人認為不好的 code。

## JavaScript

在 JavaScript 中，不管是 function 或變數，習慣使用 lower camel case，也就是 `handleAddPost`。

在特殊情況下，可以使用大寫駝峰式，例如：

1. XMLHttpRequest
2. Number
3. Set

這些變數可以算是物件導向中的 class，因此習慣以大寫開頭。而 React 中的 也同樣會使用大寫開頭方式命名。

### 常數

- 常數具有不變的特性，通常以 snake case + 全大寫來命名
- 例如：圓周率 PI，就會是 `Math.PI`；或是 client id 會寫成 CLIENT_ID

## 資料庫 table 與欄位

- 資料庫以 snake case 命名為主
- table 名稱的慣例是複數，所以使用者資料會叫做 users
- 欄位名稱同樣是 snake case，以建立時間為例：created_at

## Url

snake case 或 kebab case 這兩種慣例都蠻常見的，可能會長這樣：

1. handle_add_post
2. handle-add-post

## 變數命名

- 大原則：不確定縮寫或簡稱時，就乖乖寫好寫滿
  - 例如：event handler 傳進來的參數 event，常見的簡寫就是 evt 或是 e
- function 通常搭配動詞開頭，get 和 set 就是常見動詞。例如 getGames 或是 getStreams，setName 或是 setTitle

## 程式碼排版

例如統一空兩格，可透過調整編輯器設定，上傳到 GitHub 後要確認過沒有跑版問題。

---

## 資訊安全

1. 程式碼都是公開的：後台管理界面一定要做驗證，才能進行權限管理
2. 不要存著僥倖心態：永遠都預設把你要輸出的東西做編碼（例如：跳脫）以後才輸出，而不是直接輸出，就可以避免掉很多的 XSS 攻擊。

## 前端檢查 vs 後端檢查

前端做資料檢查，只是為了增進使用者體驗，後端做資料檢查才是真的檢查。

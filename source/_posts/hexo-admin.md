title: 【學習筆記】hexo-admin：Hexo 後台管理工具
author: Heidi Liu
tags:
  - Hexo
  - hexo-admin
categories:
  - 技術學習
  - Blog
  - Hexo
date: 2020-12-02 14:08:00
---
![](https://i.imgur.com/T1CHqyf.png)

在上篇[【學習筆記】如何使用 Hexo + GitHub Pages 架設個人網誌](https://heidiliu2020.github.io/2020/11/07/202011-hexo-github/)中，我們學會如何打造簡單的個人網誌後，再來要介紹如何透過 hexo-admin 這個套件，以更直觀的方式在後台管理網誌文章。

<!--more-->

## 為什麼需要 hexo-admin？

在上篇文章介紹到，要在網誌發布文章，必須透過 CLI 介面以 `hexo new` 指令新增文章，再利用 `hexo g -d` 生成並部署。

透過 hexo-admin 這套插件，我們就能透過 GUI 介面進行後台管理，例如編輯原有的 markdown 文件，也可以新增文章或頁面、發布草稿和提供預覽功能等等，在操作上簡化了發布文章的流程。

## 安裝套件

> 詳細可參考文件說明：[jaredly/hexo-admin](https://github.com/jaredly/hexo-admin)

1. 首先進入本地端存放 hexo 專案的資料夾
2. 在終端機輸入安裝指令

```
$ npm install --save hexo-admin
```

## 進入 hexo-admin 後台

安裝完成之後，就可以進入後台管理，步驟如下：

1. 架設本地端伺服器

```
$ hexo server -d
// 或簡化成
$ hexo s
```

看到下方提示就代表運行成功：

![](https://i.imgur.com/zXT8P5C.png)

2. 在瀏覽器輸入 http://localhost:4000 可以預覽發布前的網誌
3. 進入 http://localhost:4000/admin 可進入後台管理，在 Posts 可看到文章列表：

![](https://i.imgur.com/ZGKnhui.png)

在 Pages 可編輯其他頁面：

![](https://i.imgur.com/UWJr7PU.png)

## 新增文章 Publish

1. 點選左上角的 New Post，可輸入該文章的網址名稱，接著打勾或按 Enter：

![](https://i.imgur.com/fMCYDdW.png)

2. 就會進入編輯頁面，可在標題列編輯文章標題，標題下方則是文章網址，左邊區塊可編輯 Markdown 文章內容，右方區塊則是預覽文章

![](https://i.imgur.com/190UBSx.png)

3. 編輯完成後，可點選 Publish 左側的設定，修改發布文章時間、標籤、分類，確認都沒問題後，即可點選 Publish 發布文章

![](https://i.imgur.com/BBUAMBO.png)

4. 回到 http://localhost:4000 即可看到剛才新增的文章

![](https://i.imgur.com/Jezhv4m.png)

### 補充：Read more 功能

在上方編輯模式中，可以看到 `<!--more-->` 這行程式碼，在這行以下的內容就會自動被隱藏，會多一個閱讀全文（Read more）的連結，必須點擊文章才會看到全文。

## 部署到 GitHub

確認文章都沒問題之後，就可以準備部署到 GitHub 上，步驟如下：

1. 在終端機按 Ctrl+C，可停止本地端伺服器

![](https://i.imgur.com/BXhBwiC.png)

2. 輸入下方三個指令進行部署

- hexo clean：清除之前建立的靜態檔案
- hexo generate：建立靜態檔案
- hexo deploy：部署到 Github Pages

也可以簡寫成：

```
$ hexo cl
$ hexo g
$ hexo d
```

這樣就成功透過 hexo-admin 管理後台文章！

## 心得記錄

其實上次在搬運筆記的時候，就已經有使用 hexo-admin 這套工具，卻沒想到過一段時間後，還是會忘記該如何操作，於是乎乾脆寫成一篇文章，之後也可以回來複習。

金魚腦如我，果然還是不能沒有學習筆記XD

參考文章：[[教學] 我的第一篇 Hexo 文章：使用 hexo-admin 後台管理工具](https://ed521.github.io/2019/08/hexo-admin/)
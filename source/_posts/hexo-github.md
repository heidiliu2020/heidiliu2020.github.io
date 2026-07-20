title: 【學習筆記】如何使用 Hexo + GitHub Pages 架設個人網誌
tags:
  - Git
  - Hexo
categories:
  - 技術學習
  - Blog
  - Hexo
author: Heidi Liu
description: 手把手教你用 Hexo + GitHub Pages 免費架設個人部落格：從安裝 Node.js 與 Hexo CLI、建立專案與環境、常用指令介紹，到部署上 GitHub Pages 的完整流程，並補充 GitHub Actions 自動部署選項，新手也能快速上線自己的網誌。
date: 2020-11-07 20:10:00
updated: 2026-07-13 12:00:00
---
![](/images/posts/hexo-github/dOOM0JO.png)

## 前言

> 2026.07 更新：修正過時的版本資訊（Node.js、預設分支 main）、GitHub 認證方式，並補充 GitHub Actions 部署的選項。整體架站流程至今仍適用。

本篇主要介紹如何使用 Hexo 並搭配 GitHub 來快速架設網誌。從介紹什麼是 Hexo 框架，該如何安裝、建立環境，接著介紹一些常用指令，以及如何部署到 GitHub 上。

<!--more-->
文章可分為下列幾個部分：

- 什麼是 Hexo？
- 前置作業
  - 安裝需求
- Hexo 環境建置
- 常用指令
- 部署到 GitHub
  - 建立 GitHub 專案
  - 將檔案發布到 GitHub 

## 什麼是 Hexo？

> 引用[官網介紹](https://github.com/hexojs/hexo)：A fast, simple & powerful blog framework, powered by Node.js.

[Hexo](https://hexo.io/zh-tw/) 其實就是一個基於 Node.js 開發的網誌框架，具有下列幾項特點：
- 編譯速度非常快
- 能夠支援 Markdown 語法解析文章，並透過主題渲染靜態檔案
- 具有豐富的外掛套件
- 支援一鍵部署到 GitHub Pages、Netlify 等支援靜態網頁的空間

## 前置作業

### 安裝需求

在開始安裝 Hexo 之前，必須先在電腦安裝下列工具：

- #### [Node.js](https://nodejs.org/en/)：提供 npm 來安裝所需的套件。選擇安裝 LTS（長期支援）版本即可

> 撰文當時的 LTS 是 14.15.0，現在請直接安裝官網當前的 LTS 版本；Hexo 7 要求 Node.js 14 以上。若不確定電腦上的版本，可在終端機輸入 `node -v` 查看版本號。

![](/images/posts/hexo-github/JEdBf4y.png)

- #### [Git](https://git-scm.com/)：用來將檔案發布到 GitHub Page

> Git 基礎用法可參考：[版本控制 - Git 概念 ＆ 基本指令](https://hackmd.io/@Heidi-Liu/note-git)

![](/images/posts/hexo-github/drhF9RQ.png)

> [補充] [Git 和 GitHub 的差別？](https://hackmd.io/@Heidi-Liu/note-git-and-github)
> Git 是用來版本控制的程式；GitHub 則是提供存放 Git Repository 的服務，讓使用者能在視覺化界面進行管理。

## Hexo 環境建置

完成前置作業後，接著就要來建立 Hexo 環境，步驟如下：

> 若對 CLI 不熟悉，可參考：[Command Line 入門 & 基本指令](https://hackmd.io/@Heidi-Liu/note-cli)

### Step1. 安裝 Hexo

![](/images/posts/hexo-github/3162t1b.png)

開啟 CLI 介面（例如 cmd、git-bash 等終端機），並輸入下列指令安裝 Hexo：

```
$ npm install hexo-cli -g
```

![](/images/posts/hexo-github/20qI9yU.png)

安裝完後，可輸入 `hexo version` 或 `hexo -v` 查看 Hexo 版本，確認是否有安裝成功：

![](/images/posts/hexo-github/PRFQNVz.png)

### Step2. 初始化 Hexo

接著要初始化 Hexo，這裡有兩種做法：

1. 直接輸入下面指令，會自動於所在目錄建立一個新資料夾以操作 Hexo。記得將括號內修改成自己的資料夾名稱，若不指定資料夾名稱，則會直接初始化當前目錄：

```
$ hexo init <資料夾名稱>
```
![](/images/posts/hexo-github/tPOIIKP.png)

2. 也可以先建立好資料夾，並在該資料夾輸入上述指令，同樣能進行初始化。可使用 cd 指令來切換路徑：

```
$ cd <資料夾名稱 or 資料夾路徑>
```

![](/images/posts/hexo-github/t1vVcEC.png)

### Step3. 在資料夾安裝所需檔案

確認 CLI 上的路徑是在資料夾中，接著執行下列指令，安裝所需的 npm 套件：

```
$ npm install
```

>也可以直接在資料夾目錄輸入 cmd，按下 enter 後就會在這個路徑開啟終端機。

安裝完成後，進入資料夾會看到下方這些檔案和資料夾：

```
.
├── _config.yml
├── package.json
├── scaffolds
├── source
|   ├── _drafts
|   └── _posts
└── themes
```

#### _config.yml

- 有關網站配置的檔案，可修改各種配置設定。例如：網站標題、網站的網址、使用主題名稱等等
- 詳細內容可以參考[官方文件](https://hexo.io/zh-tw/docs/configuration)

#### package.json

記錄所有載入的應用程式資料，也就是專案中需要的所有模組。

#### scaffolds 模板

- 當我們建立新文章時，Hexo 會根據 scaffolds 中的模板建立相對應的檔案
- 資料夾中有三種預設[佈局](https://hexo.io/zh-tw/docs/writing.html)：post、page 和 draft，分別對應：要發布的文章、頁面、草稿

#### themes 主題

- 用來存放主題的資料夾
- Hexo 會根據主題來解析 source 資料夾中的檔案並產生靜態頁面。預設主題為 [landscape](https://github.com/hexojs/hexo-theme-landscape)

#### source 資源

- 用來存放原始檔案的地方，例如 Markdown 檔、圖片、各種頁面（分頁、關於等）
- 通常資料夾命名開頭會加上底線 `_`，例如 `_imgs`
- 以 `_` 開頭的檔案、資料夾或隱藏檔案會被忽略，除了 `_posts` 資料夾以外
- Markdown 檔和 HTML 檔會被解析，並放到 public 資料夾，而其他檔案則會被拷貝過去

#### source & public & .deploy_git 的差別

- 執行 `$ hexo generate` 之後，會將 source 文件夾中的 Markdown 檔和 HTML 檔進行解析，再結合主題進行渲染，生成我們看到的靜態網站
- 執行 `$ hexo deploy` 之後，則會將 public 文件夾中的內容部署到 GitHub，並生成 .deploy_git 資料夾，因此內容與 public 幾乎相同
- 這三者的關係可想成：

```
source -> public -> .deploy_git
```

---

## 常用指令

接著介紹一些 Hexo 常會用到的相關指令語法，更多詳細指令可參考[官方文件](https://hexo.io/zh-tw/docs/commands)。

### new 新增文章

```
$ hexo new [layout] <title>
```

- 如果沒有設定 layout，則會使用 _config.yml 中的 default_layout 來設定
- 如果標題有包含空格，需使用引號括住：``"title"``
- 接著可直接到 `/source/_posts/title.md` 中編輯文章內容

> 若是對 Markdown 相關語法不熟悉，可參考這篇筆記：[Markdown 格式介紹](https://hackmd.io/@Heidi-Liu/note-markdown)

### clean 清除靜態檔案與快取

```
$ hexo clean
```

在每次儲存修正後的檔案之前，會建議先輸入此指令，清除快取檔案 （db.json）和已產生的靜態檔案（public）。

### generate 產生靜態檔案

```
$ hexo generate
```

可簡寫成 `hexo g`，生成靜態檔案。

### server 啟動伺服器

- 在本地端啟動 Hexo 伺服器，預設路徑為：`http://localhost:4000/`
- 可在自己電腦上預覽設定結果，按 Ctrl + C 即可關閉
> localhost：代表只能從本地瀏覽此網站，無法從外部瀏覽

```
$ hexo server
```

![](/images/posts/hexo-github/JUHZ8Lw.png)

## 部署到 GitHub

### 建立 GitHub 專案

在架設網誌之前，還必須準備一個存放網站的空間，例如架設主機，或是選擇現有的平台，例如 GitHub Pages、Netlify、Vercel 等，本篇以 GitHub 作為範例。

接著可依照下列步驟在 GitHub 新增專案：

#### Step1. 註冊 [GitHub](https://github.com/) 帳號並登入

#### Step2. 點選 New 新增一個 Repository（專案）

![](/images/posts/hexo-github/nDvzP4k.png)

#### Step3. 將專案名稱命名為 `username.github.io`，username 記得改成自己的帳號名稱

![](/images/posts/hexo-github/0i5Fg2R.png)

這樣就成功建立了一個網域：`username.github.io`

### 將檔案發布到 GitHub

#### Step1. 安裝 Git 相關套件

回到 hexo 資料夾，在終端機輸入下列指令安裝部署所需套件：

```
$ npm install hexo-deployer-git --save
```

#### Step2. 修改 _config.yml 檔案的 Deployment 設定

接著是修改 _config.yml 設定檔中，有關 deploy 的設定。

> 需注意這裡指的 _config.yml 檔案是根目錄的，而不是 themes 主題中的。

```
deploy:
  type: git
  repo: https://github.com/username/username.github.io.git
  branch: main
```

- type：選擇部屬模式，這裡填 git
- repo：GitHub repository 的連結，記得將 username 修改成自己的帳號名稱
- branch：選擇分支。GitHub 新建 repo 的預設分支已從 `master` 改為 `main`，這裡要填 GitHub Pages 設定的來源分支（可在 repo 的 Settings → Pages 確認）

![](/images/posts/hexo-github/bVw4OIH.png)

#### Step3. 輸入部署指令

使用下列指令即可部署檔案到網站上，第一次輸入會要求 GitHub 認證：

```
$ hexo deploy
```

> 注意：GitHub 已於 2021 年停用帳號密碼推送，認證需改用 [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)（在密碼欄位貼上 token）或事先設定好 SSH 金鑰（repo 填 `git@github.com:username/username.github.io.git`）。

通常在完成每次修改後，會依序輸入 clean -> generate -> deploy 三行指令，避免更新不完全：

```
$ hexo cl    // 清除之前建立的靜態檔案
$ hexo g     // 建立靜態頁面
$ hexo d     // 部署至 GitHub
```

或是合併第二、三行指令：`hexo g -d` 即可在產生靜態頁面後立刻部署。

> 補充：除了本篇介紹的 `hexo-deployer-git` 一鍵部署，Hexo 官方文件現在也提供透過 GitHub Actions 在 push 後自動建置部署的做法，適合不想在本機執行 deploy 指令的人，可參考[官方教學](https://hexo.io/docs/github-pages)。

這樣就完成部署網誌到 GitHub 了！可在個人頁面 `https://username.github.io` 確認是否有發布成功，預設畫面如下：

![](/images/posts/hexo-github/X0cAUy6.png)

---

## 結語

當初之所以會對 Hexo 產生興趣，是因為在課程第十四週時，學到該如何購買個人主機和網域來部署，主要是部署動態網頁為主，例如 [todolist](http://heidiliu.tw/todolist/) 和 [board](http://heidiliu.tw/board/)。

本來也想要嘗試放看看 Markdown 檔案，卻沒想到瀏覽器並不支援，會導致部分內容變成亂碼等等。上網查該如何解決，就找到許多和 Hexo + GitHub 架設網誌有關的文章，能夠快速架設並且支援解析 Markdown 檔案，想著之後一定也要來挑戰看看！

實際在使用 Hexo 框架時，真的比想像中還要方便許多！除了能夠快速套用主題或外掛，也能自訂修改想要的樣式，能夠玩出許多變化。目前[網站 Demo](https://heidiliu2020.github.io/) 還很陽春，之後會繼續摸索有哪些功能，預計下一篇會整裡有關更換主題等設定，同時也慢慢豐富自己的網誌。

參考資料：
- [架設 Hexo+GitHub](https://hsiangfeng.github.io/hexo/20190411/932826160/)
- [基於Hexo的matery主題搭建博客並深度優化](https://segmentfault.com/a/1190000021923137)

## 延伸閱讀

- [【學習筆記】如何更換 Hexo 主題 & 自訂樣式](/hexo-theme/)
- [【學習筆記】hexo-admin：Hexo 後台管理工具](/hexo-admin/)
- [[week 1] 版本控制 - Git 進階指令 & GitHub](/git-github/)

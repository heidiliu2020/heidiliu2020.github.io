title: 【學習筆記】如何使用 Docusaurus & React 快速架設靜態網站
author: Heidi Liu
tags:
  - React
  - Blog
categories:
  - 技術學習
  - Blog
  - Docusaurus
date: 2022-12-19 10:13:00
---
![](https://i.imgur.com/7UpoFaC.jpg)

## 前言

這是繼 HackMD 和 Hexo 之後，找到的下一個據點，打從第一眼看到 docs 版面配置，就在心底讚嘆：「這不就是我一直想做的功能嗎！」

能夠快速把過去所學的知識打包起來，並以有效率的方式整理，適用於內容驅動型的網站，並且內建支援夜間模式轉換功能。此外，使用的還是快被自己遺忘 React.js 語法，簡直一石多鳥，相見恨晚。

於是乎，這篇筆記就誕生了。

<!--more-->

主要會介紹如何使用 Docusaurus 搭配 React 快速架設個人網站。文章可分為下列幾個部分：

+ 前言
+ 什麼是 Docusaurus？
  + 為什麼選擇 Docusaurus？
+ 環境建置
+ 專案架構
  + Docusaurus 設定檔
  + 建立模板頁面
  + 支援 TypeScript 語法

## 什麼是 Docusaurus？

![](https://i.imgur.com/BNVL8zg.png)

> Document（文件）+ saurus（恐龍）= Docusaurus
> 一直覺得這名字很難記，透過拆字希望能幫助記憶:3

[Docusaurus](https://docusaurus.io/docs) 是由 [Facebook 推出](https://opensource.fb.com/)的開源靜態網站生成工具，以 React 技術構建，提供快速建置以文檔內容為核心的網站。

### 為什麼選擇 Docusaurus？

![](https://i.imgur.com/UuV6bh4.png)

開頭有提到 Docusaurus 幾項特點，再參照官網說明後整理如下：

+ 支援 Markdown 擴充格式 [MDX](https://mdxjs.com/)
+ 可在文檔中編寫 [JSX](https://zh-hant.reactjs.org/docs/introducing-jsx.html) 語法，並渲染為 React 的 component
+ 支援 i18n，可使用 [Crowdin](https://crowdin.com/) 將文檔翻譯成 70 多種語言
+ 文檔版本控制
+ [algolia](https://www.algolia.com/) 搜索功能
+ 實際應用範例：[Create React App](https://create-react-app.dev/)、[React Native](https://reactnative.dev/)、[Gulp](https://gulpjs.com/) 等，更多可參考[官網列表](https://docusaurus.io/zh-CN/showcase)

## 環境建置

> 詳細教學可參考[官網連結](https://tutorial.docusaurus.io/docs/intro)。

步驟如下：

1. 初始化專案

```
$ npx @docusaurus/init@latest init my-website classic
$ npx docusaurus --version
```

2. 切換路徑至剛才建立好的專案底下

```
$ cd my-blog
```

3. 運行專案 

```
$ npm run start
```

4. 即可在 `http://localhost:3000/` 看到專案預設頁面如下，自動建立了首頁和 Tutorial、Blog 兩個文檔頁面： 

![](https://i.imgur.com/4Ypjr15.png)

5. 在部署前，需將網站資料打包到 `/build` 資料夾中，即可在 GitHub 等平台部署靜態網頁

```
$ npm run build
```

## 專案架構

以下是官網提供的範例架構：

```
my-website         // 根目錄
├── blog           // 部落格文章
│   ├── 2019-05-28-hola.md
│   ├── 2019-05-29-hello-world.md
│   └── 2020-05-30-welcome.md
├── docs           // 文檔
│   ├── doc1.md
│   ├── doc2.md
│   ├── doc3.md
│   └── mdx.md
├── src
│   ├── css        // 樣式管理
│   │   └── custom.css
│   └── pages      // 頁面管理
│       ├── styles.module.css
│       └── index.js
├── static        // 放置靜態檔案
│   └── img
├── docusaurus.config.js  // 專案配置
├── package.json
├── README.md
├── sidebars.js           // docs 側邊欄配置
└── yarn.lock
```

+ blog
  + 預設名稱：blog-examples-from-docusaurus)
  + 路由：`/blog`
  + 存放 blog markdown 檔，也就是部落格文章
  + 文檔名稱需符合 `yyyy-mm-dd-file-name.md`
+ docs
  + 預設名稱：docs-examples-from-docusaurus
  + 路由：`/docs`
  + 存放 markdown 文檔
+ src
  + css
    + custom.css 用來自定義樣式
  + pages
    + 預設的 index.js 包含 Home Component
    + 可用來新增頁面和對應路由，參考[官網教學](https://docusaurus.io/docs/creating-pages)
+ static
  + 存放靜態資源，例如圖片檔
+ docusaurus.config.js
  + 網站配置設定檔
  + 等同於 Docusaurus v1 中的 siteConfig.js 檔
+ sidebars.js
  + 自定義 docs 側邊欄

接著開啟剛才建置完成的專案目錄，docs 資料夾內的文檔對應頁面如下：

![](https://i.imgur.com/Rkpmx9z.png)

### Docusaurus 網站相關配置

其中 [docusaurus.config.js](https://docusaurus.io/docs/docusaurus.config.js) 這個檔案，主要用來設定框架配置：

#### Required fields 必要配置

+ 網站名稱、連結、根目錄

```javascript=
module.exports = {
  title: 'Docusaurus',
  url: 'https://docusaurus.io',
  baseUrl: '/',
};
```

#### Optional fields 自選配置

+ 網站圖示、網站標語

```javascript=
module.exports = {
  favicon: '/img/favicon.ico',
  tagline:
    'Docusaurus makes it easy to maintain Open Source documentation websites.',
};
```

+ i18n 多國語系

```javascript=
module.exports = {
  i18n: {
    defaultLocale: 'zh-TW',     // 預設語系
    locales: ['en', 'zh-TW'],   // 語系配置
    localeConfigs: {
      en: {
        label: 'English',
        direction: 'ltr',       // 閱讀方向為左到右
      },
      'zh-TW': {
        label: '繁體中文（台灣）',
        direction: 'ltr',
      },
    },
  },
};
```

+ GitHub 用戶、專案、主機名稱，用於專案部署

```javascript=
module.exports = {
  // Docusaurus' organization is facebook
  organizationName: 'facebook',
  projectName: 'docusaurus',
 githubHost: 'github.com',
};
```

+ 自定義主題外觀：例如 navbar、footer

```javascript=
module.exports = {
  themeConfig: {              // 自定義主題配置
    hideableSidebar: false,   // 側邊欄可否收起展開
    colorMode: {              // 深淺色配置
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
      switchConfig: {
        darkIcon: '🌙',
        lightIcon: '\u2600',
        // React inline style object
        // see https://reactjs.org/docs/dom-elements.html#style
        darkIconStyle: {
          marginLeft: '2px',
        },
        lightIconStyle: {
          marginLeft: '1px',
        },
      },
    },
    navbar: {                 // 導覽列
      title: 'Site Title',    // 網站標題
      logo: {
        alt: 'Site Logo',
        src: 'img/logo.svg',
      },
      items: [                // 導覽列 => docs, blog...等
        {
          to: 'docs/docusaurus.config.js',
          activeBasePath: 'docs',
          label: 'docusaurus.config.js',
          position: 'left',
        },
        // ... other links
      ],
    },
    footer: {               // 底部區塊配置
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Docs',
              to: 'docs/doc1',
            },
          ],
        },
        // ... other links
      ],
      logo: {
        alt: 'Facebook Open Source Logo',
        src: 'https://docusaurus.io/img/oss_logo.png',
      },
      copyright: `Copyright © ${new Date().getFullYear()} Facebook, Inc.`, // You can also put own HTML here
    },
  },
};
```

+ plugins 插件

```javascript=
module.exports = {
  plugins: [],
};
```

+ themes 主題

```javascript=
module.exports = {
  themes: [
    // 互動式程式碼編輯器
    require.resolve('@docusaurus/theme-live-codeblock'),
    // 搜尋功能
    require.resolve('@docusaurus/theme-search-algolia'),
    // 程式碼高亮顯示
    require.resolve('@docusaurus/theme-classic'),
  ],
};
```

+ customFields：因 Docusaurus 不允許 `docusaurus.config.js` 檔案中存在未知欄位，可在此區塊自定義欄位

```javascript=
module.exports = {
  customFields: {
    admin: 'endi',
    superman: 'lol',
  },
};
```

+ scripts：`<script>` 經過編譯後會插入 HTML 的 `<head>`

```javascript=
module.exports = {
  scripts: [
    // String format.
    'https://docusaurus.io/script.js',
    // Object format.
    {
      src:
        'https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.0/clipboard.min.js',
      async: true,    // 是否同步
    },
  ],
};
```



### 建立模板頁面

![](https://i.imgur.com/7vcwgeU.png)

```
---
id: intro
title: 啦啦啦
---

這是我的 *新文件内容
```

markdown 內容
將你的文檔以 .md 文件的形式添加到 /docs 文件夾中，並確保每個文件都有正確的 header
最簡單的標題如下
id 是連結名稱，例如 docs/intro.html
title 是瀏覽器頁面的標題

### 支援 TypeScript 語法

+ 在初始化專案的語法最後，加上 `--typescript`：

```
npx @docusaurus/init@latest init my-website classic --typescript
```

+ 接著安裝 typescript 需要的相關套件：

```
npm install --save-dev typescript @docusaurus/module-type-aliases @types/react @types/react-router-dom @types/react-helmet @tsconfig/docusaurus
```

+ 在位於根目錄的 tsconfig.json 檔案中，新增以下內容：

```typescript=
{
  "extends": "@tsconfig/docusaurus/tsconfig.json",
  "include": ["src/"]
}
```

## 部署

> 詳細可參考[官網教學](https://docusaurus.io/zh-CN/docs/deployment#deploying-to-github-pages)。

過去在部署 Hexo Blog 時，就曾寫過關於[如何將專案部署到 GitHub](https://hackmd.io/@Heidi-Liu/note-hexo-github#%E9%83%A8%E7%BD%B2%E5%88%B0-GitHub) 的筆記，這次嘗試在 Vercel 或 Netlify 平台進行部署，以及透過設定 DNS 紀錄，達成自動轉址功能，搜尋相關設定網路上其實也有不少大神分享，因此就不再作贅述。

最後，這是架設好的 [docusaurus2 個人網站](https://heidiliu-wiki.netlify.app/)，沒想到很久前一直卡關的 DNS 設定，這次竟然蠻順利就達成目的了！之後會陸續把過去寫的學習筆記整理過，再彙整到小恐龍上，期許自己能夠循序漸進，每天都比昨天的自己更進步一些。

## 參考資料

+ [Docusaurus 2 介紹與使用](https://eddychang.me/docusaurus-v2-intro)
+ [10 大靜態網站生成工具](https://www.gushiciku.cn/pl/p3Dp/zh-tw)
+ [基于 React 的 CMS 框架对比：Docusaurus vs. Gatsby](https://charlesfeng.cn/gatsby-vs-docusaurus/)
+ [Docusaurus 配置 GitHub Action 自动发布](https://blog.alanwei.com/blog/2021/03/21/docusaurus-github-deploy/)
+ [[部落格改版學DevOps][08]netlify 超佛心的靜態網站hosting服務 - 不只做hosting還有更多](https://blog.alantsai.net/posts/2018/07/migrate-blog-to-ssg-demo-devops-8-netlify-free-static-site-hosting-service#WizKMOutline_1530449275854491)

[![hackmd-github-sync-badge](https://hackmd.io/xM0LI_7bSdSf8wGNiAbqcQ/badge)](https://hackmd.io/xM0LI_7bSdSf8wGNiAbqcQ)
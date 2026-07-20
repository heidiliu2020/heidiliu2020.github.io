title: 【學習筆記】女巫攻擊 vs. 日蝕攻擊 vs. DDoS 攻擊
author: Heidi Liu
tags:
  - Security
categories:
  - 技術學習
  - Security
date: 2022-11-29 17:25:00
---
![](/images/posts/information-security-about-p2p/dOrGjQy.png)

### 從 P2P 網路說起

<!--more-->

我們所熟悉的傳統網站架構，是把所有資源都放在同一台伺服器（Server），當使用者（Client）有需要時再向伺服器發出請求。一旦單一伺服器停擺，就有可能造成整個服務中斷的問題。

![](/images/posts/information-security-about-p2p/OycTetl.png)

- 圖片來源： [https://commons.wikimedia.org/w/index.php?curid=2551745](https://commons.wikimedia.org/w/index.php?curid=2551745)

而 **Peer to Peer（P2P）網路**，則是網路區塊的所有人均負責儲存全部或部分的資料。除了向其他IP 位址發出請求外，本身也負責處理收到的請求，同時扮演 Client 和 Server 的角色，透過「去中心化」，避免資料被中心化機構所掌控或修改，進而確保資訊安全。

![](/images/posts/information-security-about-p2p/cRfMTpC.png)

- 圖片來源：[https://commons.wikimedia.org/w/index.php?curid=2551723](https://commons.wikimedia.org/w/index.php?curid=2551723)

然而 P2P 網路也同樣淺藏著風險，十年前橫行一時的 [Foxy](https://zh.wikipedia.org/wiki/Foxy)、[BitComet](https://zh.wikipedia.org/zh-tw/BitComet) 等軟體就是基於 P2P 技術來下載資源，但前者除了電腦容易中毒，也會大量消耗網路和硬體資源。

接下來介紹幾種常見的 P2P 網路攻擊，均為攻擊者透過攻擊「節點」擾亂網路，差別在於最終攻擊目標和方式的不同：

### **女巫攻擊（Sybil Attack）**

- 方式：是指單一攻擊者透過偽造多重身份以假冒惡意節點，藉此向其他正常節點提供大量不正確的資訊，從而控制網絡取得利益
- 目的：破壞網路協議的信譽體系

### **日蝕攻擊（Eclipse Attack）**

- 方式：確保目標的所有連接都建立在攻擊者所控制的節點上
- 目的：透過攻擊手段使受害者連接的節點被攻擊者所控制，進而操控受害者節點的通信

### DDoS（Distributed Denial of Service）= 分布式拒絕服務攻擊

- 方式：攻擊者透過控制不同位置的多台機器，並利用這些機器對受害者實施攻擊
- 目的：透過大量占用網絡中的節點資源，使這些節點無法提供正常服務，進而影響到整個區塊鏈網絡的運行

### 小結

這陣子時常聽聞幣圈的新聞，藉此科普一些和網路攻擊相關的小知識。其實除了上述這些，還有很多聽起來很酷專有名詞，像是這篇[《Day21|P2P網路(2)：共識─拜占庭將軍問題》](https://ithelp.ithome.com.tw/articles/10216159) 和提到吸血鬼攻擊的[《SushiSwap 槓上 Uniswap，你知道最新的「吸血鬼挖礦攻擊」嗎？》](https://abmedia.io/sushiswap-vampire-mining-alpha-tractor)，瞭解到因應這些網路攻擊，該如何制定規則去防止攻擊者達成目的等等。

### 參考資料

- [從0開始架構區塊鏈 系列](https://ithelp.ithome.com.tw/users/20119982/ironman/2255)
- [科普 | 日蝕攻擊、DDoS攻擊](https://www.panewslab.com/zh_hk/articledetails/D41204717.html)
- [新手科普| 什麼是「交易延展性攻擊、粉塵攻擊和女巫攻擊」](https://www.blocktempo.com/analysis-on-the-current-attack-means-malleability-sybil-and-dust/)
- [日食攻擊、女巫攻擊、吸血鬼攻擊都是什麼？](https://www.panewslab.com/zh_hk/articledetails/D29262700.html)


title: '【學習筆記】Golang 入門：環境建置與開發工具'
author: Heidi Liu
tags:
  - Back-End
  - golang
categories:
  - 技術學習
  - Back-End
  - golang
date: 2026-04-01 15:27:00
---

公司目前在架構規劃中，App API 層傾向使用 Go 語言，相較於 [Rust](https://rust-lang.tw/book-tw/)學習曲線較高，Go 在高並發處理和資料串流中繼上同樣有優勢，語法也比較直覺，如果本來就有 TypeScript 背景，上手門檻相對較低。

這系列筆記預計以 [《Golang 打造 Web 應用程式》](https://willh.gitbook.io/build-web-application-with-golang-zhtw) 搭配 [《GOを早く学ぶ：完全チュートリアル》](https://www.youtube.com/watch?v=8uiZC0l4Ajw) 入門影片，一邊實作一邊整理重點，當作日後查詢用的學習筆記。

<!--more-->
---

## Why Go？

[Golang（Go Language）](https://go.dev/)是 Google 在 2009 年推出的[開源程式語言](https://github.com/golang/go)，設計目標很單純：**語法簡潔、高效能、高並發、好維護**。目前廣泛應用在後端服務、雲端平台、DevOps 工具（如 Docker、Kubernetes）等領域。

從語言特性來看，Go 具有：

- **Statically Typed / Strongly Typed**：靜態、強型別語言，編譯期就會進行型別檢查
- **Compiled & Fast Compile Time**：編譯型語言，編譯速度快，可以直接產生可執行的二進位檔，部署流程單純
- **Built-in Concurrency**：內建並發模型，透過 Goroutines（Go 例程）和 Channels，容易寫出高並發的網路服務
- **Simplicity**：語言設計簡潔，整個語言只有 25 個關鍵字，搭配官方工具鏈（`go build`、`go test`、`gofmt` 等）就能完成大部分開發流程
- **Garbage Collection**：內建垃圾回收機制（GC），不必手動管理記憶體，在效能與開發效率之間取得良好平衡

## Install Go

[Go 官網](https://go.dev/doc/install)提供標準安裝套件，支援 Linux、 Mac、Windows 系統，。下載對應平台的安裝檔並安裝完成後，可以在終端機（Terminal）輸入指令確認是否安裝成功：

```
$ go version

// 看到 go version go1.xx.x darwin/arm64 代表安裝完成
```

## 建立第一個程式：Hello, Go

環境建置完成後，先撰寫一個最簡單的「Hello World」程式，確認整體開發流程沒有問題。

1. 建立專案資料夾

```
$ mkdir hello-go
$ cd hello-go
```

2. 在資料夾內建立 `main.go` 檔案，內容如下：


```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, Go!")
}
```

3. 直接執行程式（不用先編譯成檔案）：

```
$ go run main.go

// Hello, Go!
```

如果能順利印出 `Hello, Go!` 即可確認：

* Go 安裝正確
* 環境變數與路徑設定無誤
* 編譯與執行流程均可正常運作

## Go Modules 與 GOPATH

在較新的 Go 版本（1.13 之後），預設採用 Go Modules 模式進行相依套件管理。實務上代表：

專案不再強制需要放在 GOPATH 底下。
每個專案資料夾會有一個 go.mod 檔案，用來描述模組名稱與相依套件。
在專案資料夾中執行以下指令，即可初始化一個 Module：


```
$ go mod init example.com/hello
```

此指令會建立 go.mod 檔案，之後在該資料夾內執行 go run、go build 等指令時，Go 會依照 Module 模式來管理相依套件。

GOPATH 則是較早期的工作目錄概念，目前主要用途包括：

+ 作為共用工具與套件快取的儲存位置
+ 偶爾在錯誤訊息或文件中仍會看到相關說明

若想查看目前環境的 GOPATH 設定，可以使用：

```
$ go env GOPATH
```

對入門階段而言，了解「一般專案直接使用 Module 模式即可，不必刻意依附在 GOPATH 之下」大致就足夠，細節可以在實際開發過程中再逐步補充。

## 常用 Go 指令

開始撰寫程式後，會經常使用到以下幾個 Go 指令：

+ `go run main.go`：直接編譯並執行指定的 `.go` 檔，適合開發中快速測試
+ `go build`：在目前資料夾下編譯專案，產生可執行檔（但不會自動執行）

例如：

```go
$ go build
$ ./hello-go
```

+ `go test`：執行以 `_test.go` 結尾的測試檔，是撰寫單元測試與自動化測試時的重要工具
+ `go fmt` / `gofmt`：依照官方格式自動排版程式碼。多數編輯器可以設定為在檔案儲存時自動執行，因此日常開發很少需要手動下指令
+ `go mod tidy`：清理與整理 `go.mod` / `go.sum`，清理與整理 go.mod、go.sum，移除未使用的套件並補上缺少的相依，讓相依關係保持一致

## 開發工具：編輯器與外掛

在開發體驗上，建議的工具組合如下：

+ VS Code + Go 擴充套件
    + 提供程式碼自動補完、定義跳轉、型別資訊顯示等功能
    + 可設定為在檔案儲存時自動執行 gofmt / goimports，統一程式碼風格與 import 排序
    + 內建除錯（Debug）整合，搭配 dlv（Delve）即可進行斷點除錯
+ Go 官方工具鏈（隨 Go 一併安裝）
    + gofmt：程式碼格式化工具
    + goimports：在格式化同時自動新增或移除 import。多半由編輯器在背景自動呼叫
    + go tool 系列：涵蓋 Profiler、Benchmark 等進階功能，有需要時可以再進一步深入。

若已經習慣使用 JetBrains 系列產品，也可以考慮專門的 Go IDE（例如 GoLand）；不過在入門階段，使用 VS Code 搭配官方擴充套件，通常已足以應付多數開發情境。

本篇先將「環境建置」與「基本開發工具」整理過一遍，確認本機環境可以順利撰寫並執行簡單的 Go 程式。下一步，便可以開始嘗試實作實際的 Web 應用程式，例如：

* 使用標準庫 `net/http` 實作最基礎的 HTTP Server
* 建立一個簡單的 RESTful API
* 逐步加入 Router、Middleware、設定管理（Config）等結構


## 參考資料

* [Golang 打造 Web 應用程式](https://willh.gitbook.io/build-web-application-with-golang-zhtw) 
* [GOを早く学ぶ：完全チュートリアル](https://www.youtube.com/watch?v=8uiZC0l4Ajw) 

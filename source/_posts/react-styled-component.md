title: '[week 21] React 基礎：style & 如何撰寫 CSS'
author: Heidi Liu
tags:
  - Front-End
  - CSS
  - React
categories:
  - 技術學習
  - Front-End
  - React
date: 2020-11-30 00:50:00
---
> 本篇為 [[FE302] React 基礎 - hooks 版本](https://lidemy.com/p/fe302-react-hooks) 這門課程的學習筆記。如有錯誤歡迎指正！
<!--more-->
---

## React 中的 style

在 React 中有很多種方式可以寫 CSS，主要又可分為下列三種：

### 一、inline-style 行內樣式

直接在 HTML 標籤內加入 style 屬性，例如 `style={}`，但需注意下列幾點：

- inline style 裡面放的是 object
- 只能傳入該元素支援的 inline style
- 而不能傳入偽元素或 hover
- 因為是 JavaScript 程式碼，需改為駝峰式命名

```javascript=
function Title({ size }) {
  if (size === 'XL') {
    return <h1>hello!</h1>
  }
  return(
    // 兩個大括號包住: JavaScript 程式碼 + 以物件形式
    <h2 style={{
      color: 'blue',
      // 需改為駝峰式命名
      textAlign: 'center'
    }}>hello!</h2>
  )
}
```

顯示結果：

![](/images/posts/react-styled-component/QGFGRwV.png)

### 二、使用 webpack 打包

在標籤加上 className 屬性（因為 class 是保留字），會被瀏覽器渲染成 css 中的 class，再透過 webpack 打包來引入該 css 檔案：

```javascript=
// 透過 webpack 來引入 css
import './App.css';

function App() {
  return (
    <div className="App">
      <Title />
    </div>
  );
}
```

然後編輯 App.css 檔案：

```css=
.App {
  text-align: center;
  background: yellowgreen;
}
```

顯示結果：

![](/images/posts/react-styled-component/nBoFnXg.png)

### 三、使用 styled-components 套件

styled-components 是一個 library，也是目前的主流作法。用了 styled-components 套件之後，基本上就不需再直接寫 App.css 等檔案，之後會以此方法進行介紹。

首先安裝 [styled-components](https://styled-components.com/) 套件，然後運行程式：

```
$ npm install --save styled-components
$ npm run start
```

css 是透過標籤模板的寫法，在也就是在 "`" 反引號裡面寫入 css 樣式：

```css
style.p`<css code>`
```

修改 App.js 檔案，直接在 style 後面接元素名稱，並在反引號中寫入 css 程式碼：

```javascript=
// 引入 styled-components 套件
import styled from 'styled-components';
 
const Description = styled.p`
  color: red;
  padding: 20px;
  bottom: 1px solid #000;
`

function App() {
  return (
    <div className="App">
      <Title />
      <Description>  // => 編譯後會變成 <p>
        這是副標題
      </Description>
    </div>
  );
}
```

可以想成 Description 就是有 style.p 的 component，而 React 會動態隨機產生 className，並加入設定好的 class：

![](/images/posts/react-styled-component/634Pzhw.png)

### 以切出簡單的 TodoItem 為例

根據上述範例，其實就是在 styled 後面寫 css 程式碼，因此也可寫成 Sass 語法：

```javascript=
const TodoItemWrapper = styled.div`
  max-width: 80%;
  margin: 5px auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 16px;
  border: 1px solid #eee;
`
const TodoContent = styled.div`
  color: #000;
`

// 不用傳入任何東西，但仍需在最後加上反引號
const TodoButtonWrapper = styled.div``

const Button = styled.button`
  padding: 4px;
  color: #232332;
  // 也可使用 Sass 語法
  &:hover {
    color: red;
  }
  & + & {
    margin-left: 4px;
  }
`

function App() {
  return (
    <div className="App">
      <TodoItemWrapper>
        <TodoContent>This is Todo</TodoContent>
        <TodoButtonWrapper>
          <Button>未完成</Button>
          <Button>刪除</Button>
        </TodoButtonWrapper>
      </TodoItemWrapper>
    </div>
  );
}
```

結果如下：

![](/images/posts/react-styled-component/NTDXvq3.png)

通常會把模板 TodoItem 獨立寫成 component，改寫後如下：

```javascript=
function TodoItem ({ size, content }) {
  return (
    <TodoItemWrapper>
      <TodoContent size={size}>{content}</TodoContent>
      <TodoButtonWrapper>
        <Button>未完成</Button>
        <Button>刪除</Button>
      </TodoButtonWrapper>
    </TodoItemWrapper>
  );
}

function App() {
  const titleSize = "M"
  return (
    <div className="App">
      <TodoItem content={123} />
      <TodoItem content={456} size="XL" />
    </div>
  );
}
```

也可以在 TodoContent 傳入參數 props，傳入參數的程式碼需寫在 `${...}` 裡面，而在括號內的 css 程式碼則要用反引號包住：

```javascript=
const TodoContent = styled.div`
  color: #000;
  font-size: 12px;
  ${props => props.size === 'XL' && `
    font-size: 20px;
  `}
`
```

結果如下：

![](/images/posts/react-styled-component/P06HZye.png)

## styled component 實戰

有關 styled component 套件的詳細功能可參考[官方文件](https://styled-components.com/docs/basics)，接著要舉一些常用語法作為範例。

### 範例一：透過 styled() 繼承樣式

- 如果是對 styled component 進行 restyle，裡面寫的 css 程式碼會蓋過原本的樣式：

```javascript=
// 繼承 Button 這個 styled component
const GreenButton = styled(Button)`
  background: green;
  color: #eee;
`

function TodoItem ({ size, content }) {
  return (
    <TodoItemWrapper>
      <TodoContent size={size}>{content}</TodoContent>
      <TodoButtonWrapper>
        <Button>未完成</Button>
        <GreenButton>刪除</GreenButton>
      </TodoButtonWrapper>
    </TodoItemWrapper>
  );
}
```

- 如果是對一般的 component 進行 restyle，則需要在 component 傳入 className，用來接收 BlackTodoItem 這個 class 屬性：

```javascript=
// 繼承 TodoItem component，需要傳入 className
function TodoItem ({ className, size, content }) {
  return (
    <TodoItemWrapper className={className}>
      <TodoContent size={size}>{content}</TodoContent>
      <TodoButtonWrapper>
        <Button>未完成</Button>
        <GreenButton>刪除</GreenButton>
      </TodoButtonWrapper>
    </TodoItemWrapper>
  );
}
  // 繼承 TodoItem
  const BlackTodoItem = styled(TodoItem)`
    background: #000;
  `

function App() {
  const titleSize = "M"
  return (
    <div className="App">
      <TodoItem content={123} />
      <BlackTodoItem content={456} size="XL" />
    </div>
  );
}
```

![](/images/posts/react-styled-component/teWo6kl.png)

### 範例二：透過 MEDIA QUERY 實作 RWD

像 MEDIA QUERY 這類通用性高的程式碼，可以獨立放在 constants\style.js 檔案，以便重複使用：

```javascript=
export const MEDIA_QUERY_MD = '@media screen and {min-width: 768px}'
export const MEDIA_QUERY_LG = '@media screen and {min-width: 1000px}'
```

接著就可直接在 App.js 引入使用：

```javascript=
import { MEDIA_QUERY_MD, MEDIA_QUERY_LG} from './constants/style';

const Button = styled.button`
  padding: 4px;
  color: #232332;
  font-size: 20px;
  
  ${MEDIA_QUERY_MD} {
    font-size 16px;
  }

  ${MEDIA_QUERY_LG} {
    font-size: 12px;
  }
  
  &:hover {
    color: red;
  }
  & + & {
    margin-left: 4px;
  }
`
```

RWD 結果如下：

![](/images/posts/react-styled-component/OVfi3XR.gif)

### 範例三：使用 Sass 向量變數

透過傳入 Global 參數，我們能使用 Sass 向量變數。

舉例來說，我們可在 index.js 引入 [ThemeProvider](https://styled-components.com/docs/api#themeprovider)：

```javascript=
import { ThemeProvider } from 'styled-components';

// 宣告 theme 變數
const theme = {
  colors: {
    primary_300: '#ff7777',
    primary_400: '#e33e3e',
    primary_500: '#af0505',
  }
}

ReactDOM.render(
  // 包住 App，並自訂 theme 屬性
  <ThemeProvider theme={theme}>
    <App />
  </ThemeProvider>,
  document.getElementById('root')
);
```

這樣就可以在 App.js 中取用這些變數：

```javascript=
const TodoContent = styled.div`
  font-size: 30px;
  color: ${props => props.theme.colors.primary_300};

  ${MEDIA_QUERY_MD} {
    font-size: 20px;
    color: ${props => props.theme.colors.primary_400};
  }

  ${MEDIA_QUERY_LG} {
    font-size: 12px;
    color: ${props => props.theme.colors.primary_500};
  }
`
```

也可以把 TodoItem component 獨立成 TodoItem.js 這個檔案，並且 export ：

```javascript=
export default function TodoItem() {...}
```

並在 App.js 引入：

```javascript=
import TodoItem from './TodoItem'
```

這麼做的好處就是，依照功能切割程式碼，能夠達到模組化，進而提高程式碼可讀性。


參考資料：

- [[筆記] JavaScript ES6 中的模版字符串（template literals）和標籤模版（tagged template）](https://pjchender.blogspot.com/2017/01/javascript-es6-template-literalstagged.html)
- [[第二十一週] React 基礎：如何寫 CSS](https://yakimhsu.com/project/project_w21_05_React_basic_CSS.html)

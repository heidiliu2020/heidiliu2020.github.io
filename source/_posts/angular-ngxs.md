title: Angular 延伸｜ NGXS 狀態管理入門
author: Heidi Liu
tags:
  - Angular
  - Front-End
categories:
  - 技術學習
  - Front-End
  - Angular
date: 2022-08-30 09:54:00
---
本篇主要是認識 NGXS 這套狀態管理工具，瞭解基本概念，以及和 NGRX 使用上的差異。

<!--more-->

## NGXS 簡介

- 用於 Angular 的狀態管理框架（State Management），使用 RxJS 管理程式中的所有狀態
- 通常應用於大型專案，需處理較複雜的狀態管理
- 為單一 Store
    - 優點：可循環調用其他 State 的 Action、統一使用 dispatch  調度 action
    - 缺點：需統一管理所有的 Action、Action 類型不能重複

## 安裝 NGXS

1. 透過 npm 安裝 @ngxs/store 套件

```cpp
npm install @ngxs/store
```

b. 在 `app.module.ts` 引入 `NgxsModule`

```tsx
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgxsModule } from '@ngxs/store';

import { AppComponent } from './app.component';
import { environment } from "src/environments/environment"

({
  declarations: [
								 AppComponent
								],
  imports: [
						BrowserModule, 
            NgxsModule.forRoot([], {                    // 註冊 state
							developmentMode: !environment.production. // 開發模式，可進行額外檢查
						}) 
           ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
```

## NGXS 基本概念

NGXS 包含四個概念，以下是官網介紹：

- Store: Global state container, action dispatcher and selector
- Actions: Class describing the action to take and its associated metadata
- State: Class definition of the state
- Selects: State slice selectors


![upload successful](/images/pasted-1.png)


### 建立 State：定義狀態容器的類

- State 是單純的 class 檔
- 透過 `ng g class <<state file name>>` 指令產生 ts 檔案
    - 例如：`ng g class todos.state`，Class 名稱會是 `TodosState`
- `todos.state.ts`：
    
    ```tsx
    import { Injectable } from '@angular/core';
    import { State } from '@ngxs/store';
    
    export class TodoItem {
      constructor(public content: string) {}
    }
    
    export interface TodosStateModel {
      dataset: TodoItem[];
    }
    
    @State<TodosStateModel>({ // 用來描述 state 狀態，定義資料型別
      name: 'todos',          // state 在 store 的名稱
      defaults: {             // 預設值
        dataset: []
      }
    })
    export class TodosState {}
    ```
    

建立完 state 之後，再到 `app.module.ts`
 的 `NgxsModule.forRoot([])` 引入 State：

```jsx
...
import { TodosState } from './todos.state';

({
  declarations: [AppComponent],
  imports: [
						BrowserModule, 
            NgxsModule.forRoot([TodosState], {  
							developmentMode: !environment.production.
						}) 
           ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
```

### 建立 Actions：要執行的方法

- 可直接在 state class 底下，設定要被執行的 action 方法
- addTodo(StateContenxt<T>, ActionClass? )
    - StateContenxt<T>：取得可操作此 state 的 context 物件，內建幾種方法：
        - getState(): T：取得目前 state 的值
        - setState(val: T)：重新建立 or 重設目前 state 的值
        - patchState(val: part<T>)：更新目前 state 的值
        - dispatch([actions])：觸發一或多個 actions，可傳入陣列
    - ActionClass：取得 action 對應的 Class 實體
- `todos.state.ts`：

```jsx
import { State, Action, StateContext } from '@ngxs/store';

export class TodoItem {
  constructor(public content: string) {}
}

export interface TodosStateModel {
  dataset: TodoItem[];
}

export class ADDTODO {
  payload: TodoItem;
  constructor(name: string) {
    this.payload = new TodoItem(name);
  }
}

@State<TodosStateModel>({
  name: 'todos',
  defaults: {
    dataset: []
  }
})
export class TodosState {
    constructor(
	    private apiService: ApiService     // 可注入 service，如：呼叫 API
		){ }
    
    @Action(ADDTODO)                     // 定義 action 名稱
	 	addTodo({ getState, setState }: StateContext<TodosStateModel>, { payload }: ADDTODO) {
				return this.apiService.todoApi().pipe(  // 呼叫 API
					tap(_ => {
						const state = getState();    // 取得目前 state 值
		        setState({                   // 重新設定 state 值
		          ...state,
		          dataset: [...state.dataset, payload]
		        });
					});
				)
  	}
}
```

### Store：全域 State 的容器

- Store 是 action 的 Dispatcher 和 Selector
- 透過 `store.dispatch(new AddTodo('title'))` 方法，執行對應的 Action 和取得資料
- `app.component.ts`

```jsx
import { Component } from '@angular/core';
import { Store, Select } from '@ngxs/store';
import { Observable } from 'rxjs/Observable';
import { TodoItem } from './todos.state';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  @Select('todos.dataset') todos: Observable<TodoItem[]>;

  constructor(private store: Store) {}
}
```

### Select：從全域 Store 容器中取得特定 State

- `@Select`：如上方範例，可透過 path 訂閱指定 state，其資料型態為 Observable
    - 若不使用 `@Select` 裝飾器，也可改寫成 `store.select()` 語法，如下：

```jsx
export class AppComponent {  
  todos: Observable<TodoItem[]>;

  constructor(private store: Store) {
    this.todos = store.select(state => state.todos.dataset);
  }
}
```

建立一個簡易的 Todo List 模板：

- `app.component.html`

```html
<ul>
  <li *ngFor="let item of todos | async">
    {{ item.content }}
  </li>
</ul>
<input type="text" #todoInput />
<button (click)="addTodo(todoInput)">Add Todo</button>
```

透過 `store.dispatch([actions])` 可執行一至多個 actions，回傳值為 Observable：

- `app.component.ts`

```jsx
addTodo(input) {
  this.store.dispatch(new ADDTODO(input.value)).subscribe(state => {
    console.log('state: ', state);
    input.value = '';
  });
}
```

## 實際應用：Todo List

根據上方程式碼，可參考下方範例：

[https://angular-ivy-tbbm1b.stackblitz.io/](https://angular-ivy-tbbm1b.stackblitz.io/)

總結使用 Ngxs 步驟如下：

1. 建立 State Class
2. 建立 Action Class
3. 將 State Class 引入 NgxsModule
4. 在 Component 透過 `@Select` 訂閱指定狀態
5. 在 Component 透過 `store.dispatch()` 方法執行 action

## NGXS vs [NGRX](https://ngrx.io/)

- 均能夠搭配 Angular 的依賴注入使用
- 均為 CQRS 模式（Command Query Responsibility Segregation）：將模型分為讀取資料和寫入資料的架構模式
- NGXS 使用裝飾器定義 State、Action，隱藏 reducers、effects 概念，並使用 TypeScript 定義類別，有效減少模板文件
- Redux + RxJS + Angular：NGXS 與 NGRX 雖然同樣遵循 Redux 機制，但前者 NGXS 更貼近 RxJS 設計，在處理資料流上能有效減少開發成本

## 延遲載入

- NgxsModule.forRoot([])：在根 module 註冊 state
- NgxsModule.forFeature([])：使用 forFeature 註冊 state，以實現延遲載入（Lazy Loading Modules ）

## 小結

自己在過去專案中並沒有使用過 NGXS 來管理狀態，剛好最近接手的案子有碰到，才趁著機會研究前人撰寫的程式碼邏輯。

和 React 組件分層設計，須仰賴 Redux 狀態管理不同；Angualr 本身內建的 Service 概念，搭配 RxJS 使用，其實就能應對較複雜的狀態管理。再透過引入使用 NGXS ，更能有效簡化程式碼，以便後續維護。

## 參考資料

- **[NGXS: Introduction](https://ngxs.io/)**
- **[[Angular] 第一次體驗NGXS](https://blog.kevinyang.net/2018/03/30/angular-ngxs/)**
- **[ngxs入门- SegmentFault 思否](https://segmentfault.com/a/1190000016513684)**
- **[Angular 真的需要状态管理么？ - 知乎专栏](https://zhuanlan.zhihu.com/p/45121775)**
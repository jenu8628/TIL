### 1. 프로젝트 설치

```bash
$ react-native init --version 0.61.5 testApp
```

방식은 react-native init --version 원하는버전 프로젝트이름

- 버전은 지정해도 되고 안해도 됨



### 2. 화면 시작

```bash
$ npx react-native start
또는
$ npm start
```

그리고 터미널 창을 하나 더 연 뒤

```bash
$ npx react-native run-android //ios경우 run-ios
또는
$ react-native run-andriod
```



# React

## 1. State

> Component에서 렌더링되는  데이터를 담고 유지하는 JavaScript객체이다
>
> State값에 따라 화면에 보여지는 Output이 달라짐
>
> Class컴포넌트 안에서 사용가능하고 함수컴포넌트를 정의했다면 State활용이 불가능!
>
> State는 render함수 바깥에서 정의됨.
>
> vue에서 Script의 data부분과 비슷하게 보임.
>
> But 직접 명령하면 안되는 특성이 있음.(쉽게변경되지 않기 위해)
>
> setState를 이용하여 변경해야함.
>
> 비동기성이다.

```react
// 사용 불가능
const App = () => {
	return {
	}
}

// 사용 가능
class App extends Component {
    render() {
        return {
        }
    }
}
```

### 1. 사용방법

```react
class App extends Component {
  state = {
    sampleText: 'Hello World!!'
  }

  render() {
    return (
      <View style={styles.background}>
        {/* 여기서 this는 react문법이 아닌 JavaScript문법으로 상위스코프를 가르킨다. */}
        <Text> {this.state.sampleText} </Text>
      </View>
    )
  }
};
```

### 2. boolean 활용

```react
class App extends Component {
  state = {
    sampleBoolean: true,
  }
  inputText = () => (
    this.state.sampleBoolean ?
      <Text>sampleBoolean is true</Text>
    :
      <Text>sampleBoolean is false</Text>
  )
  render() {
    return (
      <View style={styles.background}>
        {this.inputText()}
      </View>
    )
  }
};
```

### 3. 변경 방법

- setState를 이용!

- onPress(클릭) 프로퍼티로 changeState라는 함수가 작동
- state의 sampleBoolean값에 따라 sampleText의 문자열이 바뀜

```react
class App extends Component {
  state = {
    sampleText: 'Hello World',
    sampleBoolean: false,
  }
  changeState= () => {
    if (!this.state.sampleBoolean) {
      this.setState({
        sampleText: 'Text Changed!!!',
        sampleBoolean: true
      })
    } else{
      this.setState({
        sampleText: 'Hello World!!!',
        sampleBoolean: false
      })
    }
  }
  render() {
    return (
      <View style={styles.background}>
        <Text onPress={this.changeState}>
          {this.state.sampleText}
        </Text>
      </View>
    )
  }
};
```

### 4. 조심해야 할 부분

- setState를 통해서 state값을 update하는 것을 알았다 하지만
- 비동기성이고, 성능향상을 위해 단일 업데이트를 지원
- setState를 통한 데이터값을 변경할 경우에는 현재버전을 copy한 뒤에 update를 진행
- 이럴 때는 setState의 첫번째 인자로 prevState를 넣어주고 callback함수

```react
class App extends Component {
  state = {
    sampleNum: 1,
  }
  // 잘못된 방법
  onAdd = () => {
    this.setState({
      // setState의 sampleNum을 정의하는 과정에서
      // 기존의 state에 있는 sampleNum을 가지고 연산을 하려 해서 에러가 났음.
      // 에러내용은 sampleNum을 찾을 수 없다.
      sampleNum: sampleNum + 1
    })
  }
  // 내가 찾은 꼼수..?
  onAdd = () => {
    this.setState({
      // sampleNum을 찾을 수 있게 this.state를 이용해봤음.
      sampleNum: this.state.sampleNum + 1
    })
  }
  
  // 정확한 방법
  onAdd = () => {
    this.setState(prevState =>{
      return {
        sampleNum: prevState.sampleNum +1
      }
    })
  }
  

  render() {
    return (
      <View style={styles.background}>
        <Text onPress={this.onAdd}>
          {this.state.sampleNum}
        </Text>
      </View>
    )
  }
};
```



## 2. props

> read only 수정 변경이 불가한 읽기전용 프로퍼티
>
> 부모자식 관계가 형성되어야 의미가 있음.
>
> 부모로부터 자식한테 데이터가 전해지는 일방통행
>
> 자식컴포넌트는 부모로부터 props라는 데이터를 받고 그 값은 자식컴포넌트 내에서 수정 변경되지 않고 그대로 사용됨.
>
> 각 자식컴포넌트에서 부모의 데이터를 받아서 본연의 데이터는 훼손하지 않고 자유롭게 작업을 할 수 있다는 장점

### 1. 부모

```react
/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, { Component } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import PropsChild from './propsChild';

class App extends Component {
  state = {
    sampleText: 'Hello World!!',
    sampleBoolean: false,
  }
  changeState= () => {
    if (!this.state.sampleBoolean) {
      this.setState({
        sampleText: 'Text Changed!!!',
        sampleBoolean: true
      })
    } else{
      this.setState({
        sampleText: 'Hello World!!!',
        sampleBoolean: false
      })
    }
  }

  render() {
    return (
      <View>
        <PropsChild sampleText={this.state.sampleText} changeState={this.changeState} />
      </View>
    )
  }
};


export default App;
```



### 2. 자식

```react
/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

 import React from 'react';
 import { View, Text } from 'react-native';
 
 const PropsChild = (props) => {
     return (
       <View>
         <Text onPress={props.changeState}>
            {props.sampleText}
         </Text>
       </View>
     )
 };
 
 export default PropsChild;
```



#### ※ 소괄호와 중괄호의 차이

> 소괄호를 사용해야 jsx컴포넌트를 return할 수 있음
>
> jsx 는 JavaScriptXml의 약자이고 JavaScript 확장문법임

```react
// return되는 jsx컴포넌트가 없는것 
// jsx컴포넌트 return 불가
exampleFunction= () => {
    
}
// jsx컴포넌트를 return할 수 있음
exampleFunction= () => (

)
// jsx 예시
// 문자열 태그도 아니면서 HTML문법도 아닌 태그로 감싸져서 변수에 할당되는 표현식이라 보면됨.
const example = <tag>hello world</tag>

const Header = () =>(
     <View style={styles.header}>
         <Text>This is header</Text>
     </View>
);
```



## TouchEvent

#### 1. TouchableOpacity

> 터치이벤트 터치하면 살짝 희미해지고 이벤트 발생

```react
import { TouchableOpacity } from 'react-native';

 const Header = (props) =>(
     <TouchableOpacity
        style={styles.header}
        onPress={()=>alert('hello world')}
     >
         <View>
            <Text>{props.name}</Text>
        </View>
     </TouchableOpacity>
     
 );
```



#### 2. TouchableWithoutFeedback

> 터치시 아무런 변화없이 이벤트발생
>
> 주의 : View에 아무런 변화를 일으키지 않기 때문에 style을 하위 태그에 주어야함.

```react
import { TouchableWithoutFeedback } from 'react-native';

 const Header = (props) =>(
     <TouchableWithoutFeedback
        onPress={()=>alert('hello world')}
     >
         <View style={styles.header}>
            <Text>{props.name}</Text>
        </View>
     </TouchableWithoutFeedback>
     
 );
```


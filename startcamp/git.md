# Git

> Git은 분산버전관리시스템이다.

## 준비하기

윈도우에서 Git을 활용하기 위해서 [Git bash](https://git-scm.com/downloads)를 설치합니다.

초기 설치를 완료한 이후에, 계정설정을 진행합니다.

```sh
$ git config --global user.email {이메일주소}
$ git config --global user.name {유저네임}

```

## 로컬 저장소 활용하기

### 1. 저장소 초기화

> 이제부터 이 디렉토리를 Git으로 관리하겠다!(변경이력을 감시하겠다!)

````sh
$ git init
:q
````



- `.git` 디렉토리가 생성되며, 여기에 Git과 관련된 모든 정보가 저장됩니다.
- 초기화를 하고 나면 Git bash에 `(master)`라고 표시가 되는데, 이는 이 디렉토리는 이미 Git이 관리하고 있다는 뜻으로 생각할 수 있습니다.
- 이미 초기화 한 repo에서는 다시 `git init`을 하지 않습니다.

###  2.add

> working directory 작업공간에서 변경된 사항을 이력으로 관리하기 위해서는 반드시 staging area를 거쳐야 한다.

```sh
$ git add {stageing 할 파일}
$ git add . 은 디렉토리에 있는 모든파일 올리기
$ 
```

#### + unstage

```sh
$git restore --staged b.txt.# b.txt는 추가한것을 빼고싶은 파일!
```



### 3. commit

> 이력을 확정 짓는, 즉 기록을 남기는 명령어이다.

```sh
$ git commit -m '커밋 메세지'
```

커밋 기록을 확인하고 싶다면 아래의 명령어를 참고하세요.

```sh
$ git log

# 한줄로 보기
$ git log --oneline
```

커밋 메세지를 수정하려면(제일 마지막 커밋만 수정가능)

```sh
$ git commit --amend

# b.txt를 커밋했는데 c.txt도 같이 커밋하려면
$ git add c.txt

$ git commit --amend
```



### 4. status

> Git을 쓰면서 가장 많으 사용해야 하는 명령어. 현재 상황을 확인할 수 있다.

```sh
$ git status
```



## 원격 저장소 활용하기

여러 서비스 중, Github을 기준으로 설명합니다.

### 1. 준비사항

- github에 회원가입 후, 빈 repo를 만들어 둔다.

### 2. 원격 저장소 등록

- 로컬 저장소와 원격 저장소를 연결하는 일입니다.

```sh
$ git remote add origin {github repo url}
```

- 원격저장소(remote)를 등록할건데, `origin`이라는 이름으로 원격저장소를 등록하겠다.
- 원격 저장소 등록 현황을 확인하려면 아래의 명령어를 참고하세요.

```sh
$ git remote -v
```



### 3.  원격 저장소에 업로드

아래의 명령어를 통해 원격 저장소에  commit된 코드를 업로드 할 수 있습니다.

```sh
$git push origin master
```



### 4. 원격 저장소에서 로컬로 가져우기

github이나 gitlab의 repo주소를 복사해둔 뒤,

```sh
$ git clone {가져오고자 하는  repo url}
```



## 변경사항 자동으로 다운로드 하기

```sh
$git pull origin master
```



### jupyter notebook 다운 및 실행!

```sh
$pip install notebook
$jupyter notebook
```

.git이 있는 폴더에서 마우스 우클릭 -> vs코드 실행 -> .gitignore생성-> .{파일OR폴더명) 실행



```sh
$ ls -a

#파일의 차이점을 설명
$ git diff
```







### Git에 사진 올리기

- git bash(폴더 or 폴더내에서 마우스 우클릭 눌러서) 시작
- git init입력
- git bash를 켰을 때 주소 뒤에 (master)가 붙는다면 git에서 관리하는 것
- master가 붙었을 때 다시 git init 누르지 않기!
- git status(파일 확인)
- git add .(깃에 추가)
- git config --global user. email 이메일@주소(프로그램에 깃 이메일 주소 확인시켜주기)
- git config --global user. name 닉네임정하기
- git commit -m 'initial commit'(이미지 올리기)
- git log(로그 보기)
- [GIT TIL](https://github.com/jenu8628/TIL.git)
- git remote add origin https://github.com/jenu8628/TIL.git (구글과 연동)
- git push origin master (git에 업로드)
- git pull origin master

# <나만 아는 커피 레시피> 프로젝트
## Share your secret recipe

![team logo](https://user-images.githubusercontent.com/87453411/207237871-4d55c769-3ea1-4188-89f7-bbabc7bbef35.jpg)

'돼지바 프라프치노', '아샷추', '크리미 모카라떼'.
이들은 카페 메뉴에는 나와있지 않지만 소수의 사람들만 알고 주문하는 비밀의 레시피 입니다. 저희 팀은 식음료를 사랑하는 사람이라면 누구나 자신만의 커스텀 레시피가 있지 않을까라는 질문에서 이 프로젝트를 시작했습니다.

이 프로젝트는 유저들이 자신의 비밀 레시피를 브랜드 기준으로 등록할 수 있는 등록 기능과 다른 사람들이 등록한 레시피를 한 눈에 볼 수 있는 레시피 리스트 기능을 제공합니다.

https://github.com/99-gen11-w1-team2-fullStackMiniProject


## 팀구성

김준철 
박청우
양희구(팀장)
진환


<hr>

## 기술 스택
 <div align=center> <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <br> <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white"> <br> 


<img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> 

 <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white"> 
 
<img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"> <br> 

<img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"> 

<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> 
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
</div>

| 분류       | 사용                      |
| ---------- | ------------------------- |
| 프론트엔드 | Bootstrap, Jquery         |
| 백엔드     | Flask                     |
| 도구       | Git                       |
| 배포       | AWS EC2                   |
| IDE        | Pycharm, VisualStudioCode |
| 개발언어   | Javascript, Python        |
| 형상관리   | Github, Sourcetree        |
| 문서관리   | Google 공유 드라이브                          |


## 핵심기능

- 좋아요 클릭 시 유저마다 


## 피드백

### 수정 완료
- 회원정보 관련 Form 위치 수정. (피드백: 유저가 회원가입 또는 로그인 시 불편함은 없는지 고려할 것. 중앙정렬이 아니라 왜 우측으로 치우져있는가?)- 
- 최신 글 우선 보여주기 기능. (피드백: 메인 화면 메인 화면에서 게시글 보여줄 때 최신 등록 글 기준 내림차순으로 보여줄 것. 왜 예전 글이 먼저 나오는가?)
- CTA 문구 유저 친화적으로 수정. ‘글 작성’ -> '레시피 자랑하기'
- 좋아요 클릭 시 화면 전체 리로드 방지
- 좋아요 클릭 시 해당 카테고리 리스트로 랜딩 

### 수정 할 것
- DB 테이블 설계. (피드백: article_vote 또는 article 테이블에서 user 테이블 참조 시 user의 닉네임이 아니라 Primary Key인 user id를 기반으로 참조할 것. 추후 유저가 아이디를 바꾸거나 개명하는 경우를 고려하기 위함)
- 브랜드 카테고리 내 음료 카테고리 추가 분기



## 개발 API

| Feature        | Method | URL           |
| -------------- | ------ | ------------- |
| 회원가입       | POST   | /api/signup   |
| 로그인         | POST   | /api/login    |
| 유저 정보 확인 | GET    | /api/nick     |
| 글 작성        | POST   | /posts        |
| 글 목록        | GET    | /posts        |
| 회원 탈퇴      | POST   | /api/withdraw |


## 디렉토리 구조
```
├── README.md
├── app.py
├── static
│   ├── css
│   │   ├── detail.css
│   │   ├── login.css
│   │   ├── main.css
│   │   ├── mypage.css
│   │   ├── reset.css
│   │   └── signup.css
│   ├── images
│   │   ├── mug-hot-solid.svg
│   │   └── png
│   │       ├── ediya-americano.png
│   │       ├── ...
│   │       └── starbucks-latte.png
│   ├── js
│   │   ├── index.js
│   │   ├── login.js
│   │   ├── mypage.js
│   │   ├── signup.js
│   │   └── withdraw.js
│   └── logo.PNG
└── templates
    ├── detail.html
    ├── login.html
    ├── main.html
    ├── mypage.html
    ├── signup.html
    └── withdraw.html

```




## 와이어프레임
![image](https://user-images.githubusercontent.com/87453411/207217178-542b3a31-f085-4bf0-b3d3-18ad48d02365.png)



## ERD

![img_erd](https://user-images.githubusercontent.com/87453411/207220339-ec555d1c-e303-4fe5-8cd7-9b997c49f27c.jpg)


## Reference

프렌차이즈 비밀메뉴 관련
- https://www.joongang.co.kr/article/8595110#home
- https://m.blog.naver.com/shgkdms7777/222445174080
- https://m.blog.naver.com/oogaa107/222029584913


문서 작성
- https://cocoon1787.tistory.com/689
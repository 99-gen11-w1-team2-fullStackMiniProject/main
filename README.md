  
# 프로젝트 ONE SHOT ONE DRINK  

### 나만의 비밀 주문 레시피를 공유하세요  
  
![team logo](https://user-images.githubusercontent.com/87453411/207237871-4d55c769-3ea1-4188-89f7-bbabc7bbef35.jpg)  
  
'돼지바 프라프치노', '아샷추', '크리미 모카라떼'.  
메뉴에는 없지만 일부 사람들만 알고 주문하는 비밀의 레시피 입니다. 저희 팀은 식음료를 사랑하는 사람이라면 누구나 자신만의 커스텀 레시피가 있지 않을까라는 질문에서 이 프로젝트를 시작했습니다.

ONE SHOT ONE DRINK는 유저들이 웹상에서 함께 만들어가는 비밀 주문 레시피 사전입니다. 유저들이 자신의 비밀 레시피를 브랜드 기준으로 기록할 수 있는 기능과 함께 다른 유저들이 기록한 레시피를 한 눈에 모아몰 수 있는 서비스를 제공합니다.    

https://github.com/99-gen11-w1-team2-fullStackMiniProject  

<hr>  

## 목차
[1.팀 소개](#팀)

<hr>  
  
## 팀
항해 99 11기 2주차 풀스택 미니 프로젝트 2조(2022-12-09 ~ 12-13)  
- 멤버: 김준철, 박청우, 양희구(팀장), 진환  
  
  
## 핵심기능
### 토큰 인증 로그인(🔑)
- 기능 : JWT 토근 인증 방식으로 로그인, 회원가입 기능.
- 추가 고민 : signup을 정규표현식으로 구현하려고 시도 

### 라이크 기능(❤️)
- 기능 : 게시글에 유저가 직접 좋아요 누른 라이크 버튼 표시하는 기능

### 상세 페이지(📖)
- 기능 : 레시피 클릭 시 레시피 관련 세부 정보 페이지를 렌더링하는 기능

### Mysql DB(🫙)
- 기능 : AWS 상에 mysql 설치후 mysql-connector-python으로 DB 제어하는 기능 

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
| DB         | Mysql                          |
| 도구       | Git                       |
| 배포       | AWS EC2                   |
| IDE        | Pycharm, VisualStudioCode |
| 개발언어   | Javascript, Python        |
| 형상관리   | Github, Sourcetree        |
| 문서관리   | Google 공유 드라이브      |
  
  
## 피드백  
  
### 반영한 것
- 회원정보 관련 Form 위치 수정. (피드백: 유저가 회원가입 또는 로그인 시 불편함은 없는지 고려할 것. 중앙정렬이 아니라 왜 우측으로 치우져있는가?)-   
- 최신 글 우선 보여주기 기능. (피드백: 메인 화면 메인 화면에서 게시글 보여줄 때 최신 등록 글 기준 내림차순으로 보여줄 것. 왜 예전 글이 먼저 나오는가?)  
- CTA 문구 유저 친화적으로 수정. ‘글 작성’ -> '레시피 자랑하기'  
- 좋아요 클릭 시 화면 전체 리로드 방지  
- 좋아요 클릭 시 해당 카테고리 리스트로 랜딩

### 더 반영하고 싶은 부분
- 브랜드 카테고리 내 음료 종류 세부 카테고리 추가
- DB 테이블 설계. (피드백: article_vote 또는 article 테이블에서 user 테이블 참조 시 user의 닉네임이 아니라 Primary Key인 user id를 기반으로 참조할 것. 추후 유저가 아이디를 바꾸거나 개명하는 경우를 고려하기 위함)
- API restful하게 재설계

  
  
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
    ├── detail.html    ├── login.html    ├── main.html    ├── mypage.html    ├── signup.html    └── withdraw.html  
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

와이어프레임
- https://excalidraw.com/

문서 작성  
- https://cocoon1787.tistory.com/689

디자인 관련
- https://www.brandcrowd.com/
- https://www.miricanvas.com/
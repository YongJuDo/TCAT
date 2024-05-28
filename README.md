# TCAT
## 기획 의도
- 티켓 기록일지는 개인의 문화 경험을 공유하며 공동의 문화생활을 만들어 가는 플랫폼이며,
특별한 순간을 기억하고 공유하는 문화적 공간을 목표로 합니다.

## 프로젝트 개요
- 개인의 문화 경험 및 기록 공유 사이트
- 프로젝트 기간 : 2023.05.22 - 2023.06.16

## 서비스 화면
### 메인화면
  <div>
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/461b24cf-a54e-43ad-912b-ccbb3c550c90">
  </div>

### 회원가입 & 로그인
- 로그인 / 회원가입을 통해 사이트를 이용
  <div>
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/6c75af14-56d5-404b-ae2f-4c4ae17805dc" width="45%">
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/6d05ec12-6793-4baf-b078-799cdcc19a73" width="45%">
  </div>

### 기록 작성 & 이미지 검색 & 기록 보기
- 사용자가 원하는 날짜를 선택 후 기록 작성
- 웹 이미지 검색 버튼을 통해 이미지 첨부 기능
- 캘린더를 클릭하여 사용자가 기록한 기록 확인
  <div>
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/64d64ac3-86e4-4fa4-95a8-43c720175320" width="45%">
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/2e479482-8d71-4d7d-bd83-808fe366cb0a" width="45%">
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/e611ecba-96de-4daf-8017-c47ee5292358">
  </div>

### 캘린더 추가 기능
- 메뉴버튼
  <div>
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/8369f3c0-1862-4dab-9000-fbf717a5c5a5">
  </div>
- 기록 모아보기를 통해 캘린더를 한눈에 확인
- 캘린더 캡처 버튼을 통해 사용자의 캘린더를 캡처
  <div>
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/e66729c4-944d-4b48-aafd-6076c6a37416">
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/a21f4c5e-428e-4b03-b541-0f5defb4df52">
  </div>

### 사용자 캘린더 이동
- 사용자가 서로 팔로우 상태일 경우 달력 아이콘이 활성화
- 클릭하게 되면 다른 사용자의 캘린더를 확인 가능
  <div>
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/9acc660d-607b-4c12-9ad8-daeda6bd7fc9" width="45%">
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/890fdc2a-cca1-4968-b309-d279aff514a8" width="45%">
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/0369a978-db3c-4fc9-a420-d668b18e8772">
  </div>

### 티켓 랭킹 & 챗봇 & 월별 그래프
- 인터파크 실시간 티켓 랭킹 목록 (종합, 스포츠, 전시/행사)
- 챗봇 기능을 통해 관리자에게 문의
- 사용자가 기록한 문화 기록의 월별 그래프 (총 사용액, 총 게시물 수)
  <div>
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/5c191a54-b224-4776-82ee-d4516235169b" width="45%">
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/26757561-94b4-4c4b-b1f7-4ded7e562910" width="45%">
  <img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/ae6a7ff5-a99f-4ff8-9b23-5f4989bde67f">
  </div>


## 모델 설계 - ERD
<img src="https://github.com/YongJuDo/Django_TIL/assets/82207310/712d79d9-a408-46aa-9e84-60ea917b6334">

### 개별 역할 분담
| 이름 | 역할 | 구현 |
| --- | --- | --- |
| 도용주 | 백엔드 | 캘린더 기능 구현, 티켓 랭킹 구현, 캡쳐기능 구현
| 서현석 | 백엔드 | API를 활용한 기능 구현, 그래프 기능 구현, 검색 기능 구현 
| 변지윤 | 프론트엔드 | 기록 생성/수정/상세, 마이페이지, 검색페이지, 작업 
| 전지현 | 프론트엔드 | 회원가입/로그인창 메인페이지 작업, 캐릭터를 활용한 다양한 이미지 생성

### 📋 기술 스택
<img src="https://img.shields.io/badge/git-F05032?style=for-plastic&logo=git&logoColor=white" style="margin-right:5px;"> <img src="https://img.shields.io/badge/github-181717?style=for-plastic&logo=github&logoColor=white" style="margin-right:5px;"> <img src="https://img.shields.io/badge/python-3776AB?style=for-plastic&logo=python&logoColor=white" style="margin-right:5px;"> <img src="https://img.shields.io/badge/django-092E20?style=for-plastic&logo=django&logoColor=white" style="margin-right:5px;"> <img src="https://img.shields.io/badge/html5-E34F26?style=for-plastic&logo=html5&logoColor=white" style="margin-right:5px;"> <img src="https://img.shields.io/badge/css3-1572B6?style=for-plastic&logo=css3&logoColor=white" style="margin-right:5px;"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-plastic&logo=javascript&logoColor=white" style="margin-right:5px;"> <img src="https://img.shields.io/badge/sqlite-003B57?style=for-plastic&logo=sqlite&logoColor=white">
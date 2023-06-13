# 🛒onlineShop

- 장고를 이용해 온라인 쇼핑몰의 다양한 기능 구현
- 실제 쇼핑몰 사이트에서 필수 기능인 장바구니, 쿠폰, 결제, 상세정보 등 구현

------------------------------------

<h2>목차</h2>

[1.프로젝트 소개](#프로젝트-소개)<br><br>
[2.개발 환경](#개발-환경)<br><br>
[3.실행 화면](#실행-화면)<br><br>


<h2>1. 프로젝트 소개</h2>
<p>- <b>User 관점</b>의 회원가입, 로그인, 장바구니, 주문, 쿠폰, 결제 등의 기능과 <b>판매자 관점</b>의 주문 목록, PDF/CSV 변환 다운로드 등의 <br>&nbsp&nbsp기능을 Django로 구현<br>
  - User는 회원과입/로그인을 할 때에 <b>소셜 로그인 NAVER 계정으로 연동 가능</b><br>
- 판매자가 설정한 쿠폰 코드를 입력하면 결제 시 <b>쿠폰 할인 적용</b></p><br>
 
<h5>💡 프로젝트 진행 이유</h5>
> <b>쇼핑몰을 만들고 결제 방법까지 학습한다면 어떤 서비스든지 만들 수 있게 될 것</b>이기 때문에 <b>직접 판매 사이트를 구현해보고자</b> 프로젝트를 진행함

<br><br>

<h2>2. 개발 환경</h2>
<p><h4>Front : <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white" align="center" /> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white" align="center" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white" align="center" /></p>
<p>Back : <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white" align="center" /> <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white" align="center" /></p>
Tool : <img src="https://img.shields.io/badge/PyCharm-000000?style=flat-square&logo=PyCharm&logoColor=white" align="center" /></h4>

<br>

<h2>3. 실행 화면</h2><br>
<h4>메인 화면</h4>
<b>shop/templates/shop/list.html</b><br>

![image](https://github.com/toppingh/onlineShop/assets/98543258/b2fb2734-92ea-4f52-8bfb-e471bdbae017)

<br>

---------------------------------------

<br>
<h4>상세 화면</h4>
<b>shop/templates/shop/detail.html</b><br>

![image](https://github.com/toppingh/onlineShop/assets/98543258/86cad61a-0d51-42c3-bac1-8fe5ad48ffb7)

<br>

------------------------------------------------------

<br>
<h4>장바구니 화면</h4>
<b>cart 앱</b><br>

![image](https://github.com/toppingh/onlineShop/assets/98543258/6a213bb2-2213-41e2-a7a8-327273c429e6)

<br>

--------------------------------------------

<br>
<h4>쿠폰 화면</h4>
<b>coupon 앱</b><br>

![image](https://github.com/toppingh/onlineShop/assets/98543258/5e48ef89-53d8-4ba8-8405-34cbc0eb5c31)

<br>

------------------------------------------

<br>
<h4>주문 화면</h4>
<b>order 앱</b><br>

![image](https://github.com/toppingh/onlineShop/assets/98543258/846e58c2-fb47-4168-bd49-c69d99edf897)

<br>

--------------------------------------------

<br>
<h4>결제 진행 화면</h4><br>
<b>order/templates/order/create.html</b><br>
<b>order/templates/order/created.html</b><br>

![image](https://github.com/toppingh/onlineShop/assets/98543258/a7020735-e623-49dc-b487-d9ae309c9421)

<br>

--------------------------------------------

<br>
<h4>관리자 화면</h4><br>
<b>static_files/admin</b><br>

![image](https://github.com/toppingh/onlineShop/assets/98543258/8e8a0c74-f981-48ba-856b-5de8d570ccf3)



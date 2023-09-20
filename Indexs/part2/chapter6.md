## 목차
1. [경진대회 이해](#경진대회-이해)    
2. [경진대회 접속 방법 및 세부 메뉴](#경진대회-접속-방법-및-세부-메뉴)  
    2.1. [경진대회 접속 방법](#경진대회-접속-방법)  
    2.2. [경진대회 메뉴 설명](#경진대회-메뉴-설명)  
3. [탐색적 데이터 분석](#탐색적-데이터-분석)  
    3.1. [캐글 노트북 환경 설정](#캐글-노트북-환경-설정)  
    3.2. [데이터 둘러보기](#데이터-둘러보기)  
    3.3. [더 효과적인 분석을 위한 피쳐 엔지니어링](#더-효과적인-분석을-위한-피쳐-엔지니어링)  
    3.4. [데이터 시각화](#데이터-시각화)  
4. [베이스라인 모델](#베이스라인-모델)  
    4.1. [피쳐 엔지니어링](#피쳐-엔지니어링)  
    4.2. [평가지표 계산 함수 작성](#평가지표-계산-함수-작성)  
    4.3. [모델 훈련](#모델-훈련)  
    4.4. [모델 성능 검증-1](#모델-성능-검증-1)  
    4.5. [예측 및 결과 제출-1](#예측-및-결과-제출-1)  
5. [성능 개선1:릿지 회귀 모델](#성능-개선1:릿지-회귀-모델)  
    5.1. [하이퍼파라미터 최적화(모델 훈련)-1](#하이퍼파라미터-최적화모델-훈련-1)  
    5.2. [성능 검증](#성능-검증)  
6. [성능 개선2:라쏘 회귀 모델](#성능-개선2:라쏘-회귀-모델)  
7. [성능 개선3:랜덤 포레스트 회귀 모델](#성능-개선3:랜덤-포레스트-회귀-모델)  
    7.1. [하이퍼파라미터 최적화(모델 훈련)-2](#하이퍼파라미터-최적화모델-훈련-2)  
    7.2. [모델 성능 검증-2](#모델-성능-검증-2)  
    7.3. [예측 및 결과 제출-2](#예측-및-결과-제출-2)  
8. [학습 마무리](#학습-마무리)  
    8.1. [핵심 요약](#핵심-요약)  

<br/><br/>

-------

<br/><br/>

# 경진대회 이해
자전거 무인 대여 시스템의 데이터로 2011~2012년의 데이터로 이루어져 있다.  
예측값이 수치형 데이터로 시간대별 자전거 대여 수량 예측의 회귀문제이다.  
플레이그라운드 대회로 누구나 참여하기 좋은 쉬운 대회이다.

<br/><br/>

# 경진대회 접속 방법 및 세부 메뉴
캐글의 경진대회 접속 및 활용에 효율적인 정보 제공

<br/>

## 경진대회 접속 방법
1. 캐글 홈페이지 상단의 검색창으로 대회 이름 검색  
2. competitions 영역에서 해당하는 대회 선택  
대회와 관련된 주최자, 참여팀, 대회 시기등등의 기본 자료 제공

<br/>

## 경진대회 메뉴 설명
경진대회 세부 메뉴는 왼쪽부터 아래와 같다.  
1. Overview  
대회의 전반적인 preview  
    1.1. Description : 경진대회의 소개글  
    1.2. Evaluation : 경진대회의 평가지표 및 제출 형식(<span style="color:red">*중요</span>)  
2. data
제공되는 피쳐에 대한 설명 및 예측해야 하는 값에 대한 정보 제공  
    2.1. Detail : 피쳐의 분포도와 실제값 제공  
    2.2. Compact : 실제값을 table의 형태로 제공  
    2.3. Column : 피쳐의 통계값 제공  
3. code  
캐글러들이 공개 설정한 코드들의 리스트 공개  
4. Discussion  
캐글러들이 해당 데이터셋에서 알게된 인사이트들 공유
5. Leaderboard
    * public  
    대회 종료전 일부 데이터를 활용한 점수를 순위별로 보여줌
    * private
    대회 종료후 모든 데이터를 활용한 점수를 순위별로 보여줌
6. rules
대회 규정에 대한 정보가 담겨 있음
7. team
팀 초대 및 관리를 할 수 있음

<br/><br/>

# 탐색적 데이터 분석
데이터를 보면서 결과 도출에 도움이 되는지 확인하는 단계

<br/>

## 캐글 노트북 환경 설정
다른 캐글러가 작성한 환경과 코드를 활용하려면 해당 노트북의 Copy & Edit을 통하여 설정

<br/>

## 데이터 둘러보기
정형 데이터를 확인하기 위하여 pandas를 활용한 데이터 탐색

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#데이터-둘러보기)

캐글에서 제공 되는 데이터 정보 활용
|피쳐명|설명|
|--|--|
|datetime|기록일시(1시간 간격)|
|season|계절(1:봄,2:여름,3:가을,4:겨울)|
|holiday|공휴일 여부(0: 공휴일 아님, 1: 공휴일)|
|workingday|근무일 여부(0: 근무일 아님, 1: 근무일) <br/> *주말과 공휴일이 아니면 근무일로 취급|
|weather|날씨(1: 맑음, 2:옅은 안개, 약간흐림 <br/> 3: 약간의 눈,비,천둥번개, 흐림 <br/> 4: 폭우와 천둥번개, 눈과 짙은 안개) <br/> *숫자가 크면 기상악화|
|temp|실제 온도|
|atemp|체감 온도|
|humidity|상대 습도|
|windspeed|풍속|
|casual|등록되지 않은 사용자 수|
|registered|등록된 사용자 수|
|count|자전거 대여 수량(예측값)|

train, test 데이터간의 일치여부 확인 (<span style="color:red">*중요</span>)

<br/>

## 더 효과적인 분석을 위한 피쳐 엔지니어링
데이터를 다양한 관점으로 시각화 하면 다양한 특징들을 찾을 수 있는데 그러기 위하여 피쳐들의 가공이 필요하기도 하다.  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#더-효과적인-분석을-위한-피쳐-엔지니어링)

<br/>

## 데이터 시각화

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#데이터-시각화)

* 분포도 확인  
수치형 데이터의 가시화를 위한 분포도 확인  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#데이터-시각화displot)

* 막대그래프  
범주형 데이터와 결과의 관계 파악을 위한 시각화  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#데이터-시각화barplot)

* 박스플롯  
범주형 데이터에 따른 수치형 데이터를 나타내는 그래프  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#데이터-시각화boxplot)

* 포인트플롯  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#데이터-시각화pointplot)

* 회귀선을 포함한 산점도  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#데이터-시각화regplot)

* heatmap  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#데이터-시각화heatmap)

<br/><br/>

# 베이스라인 모델
앞서 진행한 데이터 시각화를 통하여 얻은 인사이트를 활용하여 기본형태의 모델을 만든다.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#베이스라인-모델)

<br/>

## 피쳐 엔지니어링
데이터를 가공하는 작업(train, test dataset을 합쳤다가 다시 나눈다.)

* 데이터 합치기  
train data, test data에 동일한 피쳐 엔지니어링을 적용하기 위하여 데이터를 합친다.

* 이상치 제거
시각화를 통하여 얻은 인사이트를 이용하여 이상치로 판단된 데이터를 지운다.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#피쳐-엔지니어링)

<br/>

## 평가지표 계산 함수 작성
경진대회의 평가지표 계산 함수 만들기

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#평가지표-계산-함수-작성)

<br/>

## 모델 훈련
기본적인 모델을 만들어 테스트 해본다.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#모델-훈련)

<br/>

## 모델 성능 검증-1
훈련한 모델을 평가지표를 활용하여 검증을 한다.

<br/>

## 예측 및 결과 제출-1
대회에 적절한 포멧을 맞춰서 결과를 제출 한다.

<br/><br/>

# 성능 개선1:릿지 회귀 모델
regression model 중에서 순차적으로 릿지 모델부터 테스트 해본다. (<span style="color:red">비추천</span>)

<br/>

## 하이퍼파라미터 최적화(모델 훈련)-1
grid search와 같은 튜닝을 진행후 cross validation으로 검증을 진행

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#하이퍼파라미터-최적화모델-훈련-1)

<br/>

## 성능 검증
하이퍼파라미터를 진행후 최대성능의 모델을 통하여 검증을 진행

<br/><br/>

# 성능 개선2:라쏘 회귀 모델

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#성능-개선2:라쏘-회귀-모델)

<br/><br/>

# 성능 개선3:랜덤 포레스트 회귀 모델

<br/>

## 하이퍼파라미터 최적화(모델 훈련)-2

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter6.ipynb#성능-개선3:랜덤-포레스트-회귀-모델)

<br/>

## 모델 성능 검증-2

<br/>

## 예측 및 결과 제출-2

<br/><br/>

# 학습 마무리

<br/>

## 핵심 요약
경진대회 이해 -> EDA -> 베이스라인 모델 -> 검증 -> 개선 -> 제출
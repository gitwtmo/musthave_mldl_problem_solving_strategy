## 목차
- [1. 경진대회 이해](#1-경진대회-이해)
- [2. 탐색적 데이터 분석](#2-탐색적-데이터-분석)
  * [2.1. 데이터 둘러보기](#21-데이터-둘러보기)
  * [2.2. 데이터 시각화](#22-데이터-시각화)
- [3. 베이스라인 모델](#3-베이스라인-모델)
  * [3.1. 피쳐 엔지니어링 1:피쳐명 한글화](#31-피쳐-엔지니어링-1피쳐명-한글화)
  * [3.2. 피쳐 엔지니어링 2:데이터 다운캐스팅](#32-피쳐-엔지니어링-2데이터-다운캐스팅)
  * [3.3. 피쳐 엔지니어링 3:데이터 조합 생성](#33-피쳐-엔지니어링-3데이터-조합-생성)
  * [3.4. 피쳐 엔지니어링 4:타깃값(월간 판매량)추가](#34-피쳐-엔지니어링-4타깃값월간-판매량추가)
  * [3.5. 피쳐 엔지니어링 5:테스트 데이터 이어붙이기](#35-피쳐-엔지니어링-5테스트-데이터-이어붙이기)
  * [3.6. 피쳐 엔지니어링 6:나머지 데이터 병합(최종 데이터 생성)](#36-피쳐-엔지니어링-6나머지-데이터-병합최종-데이터-생성)
  * [3.7. 피쳐 엔지니어링 7:마무리](#37-피쳐-엔지니어링-7마무리)
  * [3.8. 모델 훈련 및 성능 검증](#38-모델-훈련-및-성능-검증)
  * [3.9. 예측 및 결과 제출](#39-예측-및-결과-제출)
- [4. 성능 개선](#4-성능-개선)
  * [4.1. 피쳐 엔지니어링 1:피쳐명 한글화와 데이터 다운캐스팅](#41-피쳐-엔지니어링-1피쳐명-한글화와-데이터-다운캐스팅)
  * [4.2. 피쳐 엔지니어링 2:개별 데이터 피쳐 엔지니어링](#42-피쳐-엔지니어링-2개별-데이터-피쳐-엔지니어링)
  * [4.3. 피쳐 엔지니어링 3:데이터 조합 및 파생 피쳐 생성](#43-피쳐-엔지니어링-3데이터-조합-및-파생-피쳐-생성)
  * [4.4. 피쳐 엔지니어링 4:데이터 합치기](#44-피쳐-엔지니어링-4데이터-합치기)
  * [4.5. 피쳐 엔지니어링 5:시차 피쳐 생성](#45-피쳐-엔지니어링-5시차-피쳐-생성)
  * [4.6. 피쳐 엔지니어링 6:기타 피쳐 엔지니어링](#46-피쳐-엔지니어링-6기타-피쳐-엔지니어링)
  * [4.7. 피쳐 엔지니어링 7:마무리](#47-피쳐-엔지니어링-7마무리)
  * [4.8. 모델 훈련 및 성능 검증](#48-모델-훈련-및-성능-검증)
  * [4.9. 예측 및 결과 제출](#49-예측-및-결과-제출)
- [5. 머신러닝 경진대회를 마치며](#5-머신러닝-경진대회를-마치며)
  * [5.1. 학습 마무리](#51-학습-마무리)
  * [5.2. 핵심 요약](#52-핵심-요약)
<br/><br/>

-------

<br/><br/>

# 1. 경진대회 이해

* 과거의 판매데이터를 활용해 미래의 판매량을 예측하는 대회  
* 상품과 상점에 대한 정보를 제공함  
* 판매량과 관련된 피쳐및 결과는 0~20으로 제한함

<br/><br/>

# 2. 탐색적 데이터 분석

<br/>

## 2.1. 데이터 둘러보기

* sales_train  
  * date : datetime day.month.year  
  * date_block_num : 월 구분자  
  * shop_id : 상점 id  
  * item_id : 상품 id  
  * item_cnt_Day : 당일 판매량  
시계열 데이터이기 때문에 OOF와 같은 기법은 사용하기 힘들다.  

* shop  
  * shop_name : 러시아어로 구성된 상점명 
  * shop_id : sales_train에 있는 인자와 같음
EDA결과 shop_name의 첫번째 단어가 지명임이 확인됨

* items  
  * item_name : 상품명  
  * item_id : sales_train에 있는 인자와 같음  
  * item_category_id : 상품분류 id값  

* item_categories  
  * item_categories_name : 상품분류명
  * item_category_id : items에 있는 인자와 같음
EDA결과 item_categories_name 첫번째 단어가 대분류임이 확인됨

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#21-데이터-둘러보기)

<br/>

## 2.2. 데이터 시각화

* pd.groupby()  
  * sum : 합  
  * mean : 평균  
  * median : 최빈값  
  * std : 표준편차  
  * var : 분산  
  * count : 갯수  
  * min : 최솟값  
  * max : 최댓값  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#22-데이터-시각화)

<br/><br/>

# 3. 베이스라인 모델

<br/>

## 3.1. 피쳐 엔지니어링 1:피쳐명 한글화

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#31-피쳐-엔지니어링-1피쳐명-한글화)

<br/>

## 3.2. 피쳐 엔지니어링 2:데이터 다운캐스팅

* 다운캐스팅  
피쳐의 적절한 타입으로 변경을 해주는 방법 메모리 효율 증가, 속도 개선  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#32-피쳐-엔지니어링-2데이터-다운캐스팅)

<br/>

## 3.3. 피쳐 엔지니어링 3:데이터 조합 생성

* 유의미 할 수 있는데 없는 데이터를 만들어준다.  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#33-피쳐-엔지니어링-3데이터-조합-생성)

<br/>

## 3.4. 피쳐 엔지니어링 4:타깃값(월간 판매량)추가

* garbage collection을 사용하자  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#34-피쳐-엔지니어링-4타깃값월간-판매량추가)

<br/>

## 3.5. 피쳐 엔지니어링 5:테스트 데이터 이어붙이기

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#35-피쳐-엔지니어링-5테스트-데이터-이어붙이기)

<br/>

## 3.6. 피쳐 엔지니어링 6:나머지 데이터 병합(최종 데이터 생성)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#36-피쳐-엔지니어링-6나머지-데이터-병합최종-데이터-생성)

<br/>

## 3.7. 피쳐 엔지니어링 7:마무리

* clip을 활용하여 값의 범위를 제한한다.  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#37-피쳐-엔지니어링-7마무리)

<br/>

## 3.8. 모델 훈련 및 성능 검증

* clip을 활용하여 값의 범위를 제한한다.  
* 카테고리형 데이터는 카테고리 데이터 임을 표기해야 범주형 데이터로 인식되지 않음  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#38-모델-훈련-및-성능-검증)

<br/>

## 3.9. 예측 및 결과 제출

<br/><br/>

# 4. 성능 개선

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#4-성능-개선)

<br/>

## 4.1. 피쳐 엔지니어링 1:피쳐명 한글화와 데이터 다운캐스팅

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#41-피쳐-엔지니어링-1피쳐명-한글화와-데이터-다운캐스팅)

<br/>

## 4.2. 피쳐 엔지니어링 2:개별 데이터 피쳐 엔지니어링

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#42-피쳐-엔지니어링-2개별-데이터-피쳐-엔지니어링)

<br/>

## 4.3. 피쳐 엔지니어링 3:데이터 조합 및 파생 피쳐 생성

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#43-피쳐-엔지니어링-3데이터-조합-및-파생-피쳐-생성)

<br/>

## 4.4. 피쳐 엔지니어링 4:데이터 합치기

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#44-피쳐-엔지니어링-4데이터-합치기)

<br/>

## 4.5. 피쳐 엔지니어링 5:시차 피쳐 생성

* 시차 피쳐는 시계열 데이터에서 자주 생성  
본인의 상태에 대한 데이터에 이전상태의 데이터를 추가로 학습을 시켜주기 위한 방법  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#45-피쳐-엔지니어링-5시차-피쳐-생성)

<br/>

## 4.6. 피쳐 엔지니어링 6:기타 피쳐 엔지니어링

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#46-피쳐-엔지니어링-6기타-피쳐-엔지니어링)

<br/>

## 4.7. 피쳐 엔지니어링 7:마무리

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#47-피쳐-엔지니어링-7마무리)

<br/>

## 4.8. 모델 훈련 및 성능 검증

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter9.ipynb#48-모델-훈련-및-성능-검증)

<br/>

## 4.9. 예측 및 결과 제출

<br/><br/>

# 5. 머신러닝 경진대회를 마치며

<br/>

## 5.1. 학습 마무리

<br/>

## 5.2. 핵심 요약
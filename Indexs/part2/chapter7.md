## 목차
- [1. 경진대회 이해](#1-경진대회-이해)
- [2. 탐색적 데이터 분석](#2-탐색적-데이터-분석)
  * [2.1. 데이터 둘러보기](#21-데이터-둘러보기)
  * [2.2. 데이터 시각화](#22-데이터-시각화)
- [3. 베이스라인 모델](#3-베이스라인-모델)
  * [3.1. 피쳐 엔지니어링](#31-피쳐-엔지니어링)
  * [3.2. 모델 훈련](#32-모델-훈련)
  * [3.3. 모델 성능 검증](#33-모델-성능-검증)
  * [3.4. 예측 및 결과 제출](#34-예측-및-결과-제출)
- [4. 성능 개선 1](#4-성능-개선-1)
  * [4.1. 피쳐 엔지니어링 1 : 피쳐 맞춤 인코딩](#41-피쳐-엔지니어링-1--피쳐-맞춤-인코딩)
  * [4.2. 피쳐 엔지니어링 2 : 피쳐 스케일링](#42-피쳐-엔지니어링-2--피쳐-스케일링)
  * [4.3. 하이퍼파라미터 최적화](#43-하이퍼파라미터-최적화)
  * [4.4. 모델 성능 검증](#44-모델-성능-검증)
  * [4.5. 예측 및 결과 제출](#45-예측-및-결과-제출)
- [5. 성능 개선 2](#5-성능-개선-2)
- [6. 학습 마무리](#6-학습-마무리)
  * [6.1. 핵심 요약](#61-핵심-요약)

<br/><br/>

-------

<br/><br/>

# 1. 경진대회 이해

* 인위적인 데이터
* 피쳐와 타겟값의 의미를 알 수 없음(도메인 없음)  
* 범주형 데이터
분류문제는 타겟 예측(cluster) 또는 타겟의 확률(logistic)을 예측함

<br/><br/>

# 2. 탐색적 데이터 분석

Categorical Feature Encoding Challenge 경진대회를 진행  

<br/>

## 2.1. 데이터 둘러보기

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#21-데이터-둘러보기)

<br/>

## 2.2. 데이터 시각화

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#22-데이터-시각화)

* 이진형 피쳐  
특정 피쳐가 타겟에 편향성이 있는지 확인(편향도가 강하면 피쳐의 의미 퇴색)  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#이진형-피쳐)

* 명목형 피쳐  
특정 피쳐가 타겟예측에 유의미할지 본다(균등하게 분포되면 유의미 하다 볼 수 있음)  
    * 교차 분석표  
    * 포인트플롯  
    * 피쳐 분포도 및 포인트 플롯 생성 함수  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#명목형-피쳐)

* 순서형 피쳐  
서순에 따른 타겟예측이 유의미한지 본다  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#순서형-피쳐)

* 날짜 피쳐  
서순에 따른 타겟예측이 유의미한지 본다  
날짜와 같아 반복성을 가지는 피쳐는 Fourier Features와 같이 루틴을 가진 모양을 만들기도 한다  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#날짜-피쳐)

<br/><br/>

# 3. 베이스라인 모델

<br/>

## 3.1. 피쳐 엔지니어링

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#31-피쳐-엔지니어링)

<br/>

## 3.2. 모델 훈련

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#32-모델-훈련)

<br/>

## 3.3. 모델 성능 검증

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#33-모델-성능-검증)

<br/>

## 3.4. 예측 및 결과 제출

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#34-예측-및-결과-제출)

<br/><br/>

# 4. 성능 개선 1

<br/>

## 4.1. 피쳐 엔지니어링 1 : 피쳐 맞춤 인코딩

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#41-피쳐-엔지니어링-1--피쳐-맞춤-인코딩)

<br/>

## 4.2. 피쳐 엔지니어링 2 : 피쳐 스케일링

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#42-피쳐-엔지니어링-2--피쳐-스케일링)

<br/>

## 4.3. 하이퍼파라미터 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#43-하이퍼파라미터-최적화)

<br/>

## 4.4. 모델 성능 검증

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter7.ipynb#44-모델-성능-검증)

<br/>

## 4.5. 예측 및 결과 제출

<br/><br/>

# 5. 성능 개선 2
train, valid를 사용하지 않고 train으로 합하여 사용하면 성능향상이 될 수 있다.

<br/><br/>

# 6. 학습 마무리

<br/>

## 6.1. 핵심 요약
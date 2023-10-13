## 목차
- [1. 경진대회 이해](#1-경진대회-이해)
- [2. 탐색적 데이터 분석](#2-탐색적-데이터-분석)
  * [2.1. 데이터 둘러보기](#21-데이터-둘러보기)
  * [2.2. 데이터 시각화](#22-데이터-시각화)
- [3. 베이스라인 모델](#3-베이스라인-모델)
  * [3.1. 피쳐 엔지니어링](#31-피쳐-엔지니어링)
  * [3.2. 평가지표 계산 함수 작성](#32-평가지표-계산-함수-작성)
  * [3.3. 모델 훈련 및 성능 검증](#33-모델-훈련-및-성능-검증)
  * [3.4. 예측 및 결과 제출](#34-예측-및-결과-제출)
- [4. 성능 개선 1:LightGBM 모델](#4-성능-개선-1lightgbm-모델)
  * [4.1. 피쳐 엔지니어링](#41-피쳐-엔지니어링)
  * [4.2. 하이퍼파라미터 최적화](#42-하이퍼파라미터-최적화)
  * [4.3. 모델 훈련 및 성능 검증](#43-모델-훈련-및-성능-검증)
  * [4.4. 예측 및 결과 제출](#44-예측-및-결과-제출)
- [5. 성능 개선 2:XGBoost 모델](#5-성능-개선-2xgboost-모델)
  * [5.1. 피쳐 엔지니어링](#51-피쳐-엔지니어링)
  * [5.2. 하이퍼파라미터 최적화](#52-하이퍼파라미터-최적화)
  * [5.3. 모델 훈련 및 성능 검증](#53-모델-훈련-및-성능-검증)
  * [5.4. 예측 및 결과 제출](#54-예측-및-결과-제출)
- [6. 성능 개선 3:LightGBM과 XGBoost 앙상블](#6-성능-개선-3lightgbm과-xgboost-앙상블)
  * [6.1. 앙상블 수행](#61-앙상블-수행)
  * [6.2. 예측 및 결과 제출](#62-예측-및-결과-제출)
- [7. 학습 마무리](#7-학습-마무리)
  * [7.1. 핵심 요약](#71-핵심-요약)

<br/><br/>

-------

<br/><br/>

# 1. 경진대회 이해

* 안전 운전자 예측  
* 난폭운전자는 많은 보험금  
* 보험금 청구를 위한 모델  
* 보험금 청구는 1, 반대는 0으로 예측

<br/><br/>

# 2. 탐색적 데이터 분석

<br/><br/>

## 2.1. 데이터 둘러보기

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter8.ipynb#21-데이터-둘러보기)

<br/>

## 2.2. 데이터 시각화

* 타겟값의 분포를 확인  
0또는 1에 편향적이면 고려사항이 증가  
* 타겟값과 독립변수간의 분포 확인  
분별력 없이 분포 비율이 같으면 의미가 없음  
* 독립변수의 타겟값에 대한 유효성 확인
분포 비율이 달라도 신뢰도가 낮으면 의미 없음  

<br/><br/>

# 3. 베이스라인 모델

<br/>

## 3.1. 피쳐 엔지니어링

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter8.ipynb#31-피쳐-엔지니어링)

<br/>

## 3.2. 평가지표 계산 함수 작성

* 지니계수  
지니계수는 낮으면 평등 높으면 불평등을 나타내는 지표  
2*ROC AUC-1 과 같은 값을 가짐  
* 정규화 지니계수  
예측 지니계수 / 완벽예측의 지니계수  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter8.ipynb#32-평가지표-계산-함수-작성)

<br/>

## 3.3. 모델 훈련 및 성능 검증

* OOF  
K-Fold를 진행하여 검증데이터를 사용하는 방식

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter8.ipynb#33-모델-훈련-및-성능-검증)

<br/>

## 3.4. 예측 및 결과 제출

<br/><br/>

# 4. 성능 개선 1:LightGBM 모델

<br/>

## 4.1. 피쳐 엔지니어링

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter8.ipynb#41-피쳐-엔지니어링)

<br/>

## 4.2. 하이퍼파라미터 최적화

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter8.ipynb#42-하이퍼파라미터-최적화)

<br/>

## 4.3. 모델 훈련 및 성능 검증

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter8.ipynb#43-모델-훈련-및-성능-검증)

<br/>

## 4.4. 예측 및 결과 제출

<br/><br/>

# 5. 성능 개선 2:XGBoost 모델

<br/>

## 5.1. 피쳐 엔지니어링

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter8.ipynb#51-피쳐-엔지니어링)

<br/>

## 5.2. 하이퍼파라미터 최적화

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter8.ipynb#52-하이퍼파라미터-최적화)

<br/>

## 5.3. 모델 훈련 및 성능 검증

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter8.ipynb#53-모델-훈련-및-성능-검증)

<br/>

## 5.4. 예측 및 결과 제출

<br/><br/>

# 6. 성능 개선 3:LightGBM과 XGBoost 앙상블

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter8.ipynb#6-성능-개선-3lightgbm과-xgboost-앙상블)

<br/>

## 6.1. 앙상블 수행

<br/>

## 6.2. 예측 및 결과 제출

<br/><br/>

# 7. 학습 마무리

<br/>

## 7.1. 핵심 요약
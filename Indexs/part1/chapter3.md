## 목차
1. [머신러닝 문제해결 프로세스](#머신러닝-문제해결-프로세스)  
1.1. [머신러닝 체크리스트](#머신러닝-체크리스트)
2. [딥러닝 문제해결 프로세스](#딥러닝-문제해결-프로세스)  
2.1. [딥러닝 체크리스트](#딥러닝-체크리스트)  

<br/><br/>

-------

<br/><br/>

# 머신러닝 문제해결 프로세스

머신러닝의 대표적인 프로세스를 요약하면 아래와 같습니다.

|문제 이해|EDA|base model|성능 개선, 검증|결과 도출|
|--|--|--|--|--|
|목표에 대한 이해|데이터 구조 분석|모델 훈련, 검증|피쳐 엔지니어링|
|평가지표 파악|중요 피쳐 시각화|결과 예측 및 제출|하이퍼 파라미터 최적화|

성능 검증 이후에 만족 하지 못할 성능을 보이면 EDA 단계부터 다시 시도해보며 피쳐를 다시 분석해본다.

<br/>

아래는 각 단계별로 세분화한 머신러닝의 프로세스 설명입니다.

|문제 이해|||
|--|--|--|
|목표에 대한 이해|경진대회|대회의 목적과 배경을 파악, 어떤 데이터로 어떠한 결과를 도출하려는지 확인이 필요|
|목표에 대한 이해|실제상황|목적과 배경을 파악, 필요한 데이터를 파악하고 원하는 결과의 확인이 필요|
|평가지표 파악|경진대회|대회에서 체크하는 평가지표의 확인이 필요|

|EDA||
|--|--|
|데이터 구조 분석|피쳐 분석을 위한 데이터의 전반적인 구조 확인|
|중요 피쳐 시각화|피쳐들을 분석하고 시각화를 진행하여 중요한 피쳐를 탐색하고 모델링의 방향성을 구함|

|base model||
|--|--|
|모델 훈련, 검증|성능보다는 기초적인 뼈대의 모델을 구현 및 훈련|
|결과 예측 및 제출|훈련 모델을 사용하여 테스트 데이터를 예측|

|성능 개선, 검증||
|--|--|
|피쳐 엔지니어링|이상치 제거, 결측치 처리, 인코딩, 스케일링, 복합 피쳐 생성 및 제거를 진행하며 **도메인 지식**이 많이 필요하다|
|하이퍼 파라미터 최적화|파라미터 튜닝을 통하여 최적의 파라미터를 찾는 과정(RandomSearch, GridSearch, bayesian-optimization)|

### [머신러닝 체크리스트](https://docs.google.com/spreadsheets/d/1kVygnwbR_YUpNFgw-6mZQuPn8ILY2m3vl32BOu7gQsc/edit#gid=39315817)

<br/><br/>

# 딥러닝 문제해결 프로세스

딥러닝의 대표적인 프로세스를 요약하면 아래와 같습니다.

|문제 이해|EDA|base model|성능 개선, 검증|결과 도출|
|--|--|--|--|--|
|목표에 대한 이해|데이터 구조 분석|데이터 준비, 환경설정|성능 개선 기법 적용|
|평가지표 파악|데이터 시각화|모델 훈련, 검증|성능 검증|
||||결과 예측 및 제출|

성능 검증 이후에 만족 하지 못할 성능을 보이면 EDA 단계부터 다시 시도해보며 피쳐를 다시 분석해본다.

<br/>

아래는 각 단계별로 세분화한 딥러닝의 프로세스 설명입니다.

|문제 이해|||
|--|--|--|
|목표에 대한 이해|경진대회|대회의 목적과 배경을 파악, 어떤 데이터로 어떠한 결과를 도출하려는지 확인이 필요|
|목표에 대한 이해|실제상황|목적과 배경을 파악, 필요한 데이터를 파악하고 원하는 결과의 확인이 필요|
|평가지표 파악|경진대회|대회에서 체크하는 평가지표의 확인이 필요|

|EDA||
|--|--|
|데이터 구조 분석|피쳐 분석을 위한 데이터의 전반적인 구조 확인|
|데이터 시각화|타깃 분포의 시각화, 이미지 확인등을 통하여 진행할 모델을 선택, DL은 데이터 수에 영향을 많이 받기 때문에 충분한지 판단|

|base model||
|--|--|
|데이터 준비, 환경설정|프레임워크에 맞는 데이터형식 수정, 시드 고정으로 실험 결과 확인, GPU 설정으로 속도향상|
|모델 훈련, 검증|기초적인 뼈대의 모델을 구현 후 손실함수와 옵티마이저를 설정하여 훈련|

|성능 개선, 검증||
|--|--|
|성능 개선 기법 적용|옵티마이저 재설정 및 스케쥴러 설정, 데이터 부족시 테스트 데이터 증강 및 레이블 스무딩을 진행, 하이퍼파라미터 조정 및 앙상블 실행|
|성능 검증|모델의 성능을 확인하는 단계로 성능이 부족하면 EDA부터 다시 시작|
|결과 예측 및 제출|훈련 모델을 사용하여 테스트 데이터를 예측|

### [딥러닝 체크리스트](https://docs.google.com/spreadsheets/d/1kVygnwbR_YUpNFgw-6mZQuPn8ILY2m3vl32BOu7gQsc/edit#gid=1051001003)
<!-- ### [체크리스트](../../minimap/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%20%EB%94%A5%EB%9F%AC%EB%8B%9D%20%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0%20%EC%A0%84%EB%9E%B5%20%EA%B3%B5%EB%9E%B5%EC%A7%91.pdf) -->
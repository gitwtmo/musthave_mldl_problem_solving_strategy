## 목차
1. [분류와 회귀](#분류와-회귀)  
    1.1. [분류](#분류)  
    1.2. [회귀](#회귀)  
2. [분류 평가지표](#분류-평가지표)  
    2.1. [오차 행렬(confusion matrix)](#오차-행렬confusion-matrix)  
    2.2. [로그 손실](#로그-손실)  
    2.3. [ROC 곡선과 AUC](#ROC-곡선과-AUC)  
3. [데이터 인코딩](#데이터-인코딩)  
    3.1. [레이블 인코딩](#레이블-인코딩)  
    3.2. [오디널 인코딩](#오디널-인코딩)  
    3.3. [원핫 인코딩](#원핫-인코딩)  
4. [피쳐 스케일링](#피쳐-스케일링)  
    4.1. [min-max 정규화(normalization)](#min-max-정규화normalization)  
    4.2. [표준화(standardization)](#표준화standardization)  
5. [교차 검증](#교차-검증)  
    5.1. [K 폴드 교차 검증](#K-폴드-교차-검증)  
    5.2. [층화 K 폴드 교차 검증](#층화-K-폴드-교차-검증)  
6. [주요 머신러닝 모델](#주요-머신러닝-모델)  
    6.1. [선형 회귀 모델](#선형-회귀-모델)  
    6.2. [로지스틱 회귀 모델](#로지스틱-회귀-모델)  
    6.3. [결정 트리](#결정-트리)  
    6.4. [앙상블 학습](#앙상블-학습)  
    6.5. [랜덤 포레스트](#랜덤-포레스트)  
    6.6. [XGBoost](#XGBoost)  
    6.7. [LightGBM](#LightGBM)  
7. [하이퍼 파라미터 최적화](#하이퍼-파라미터-최적화)  
    7.1. [그리드서치](#그리드서치)  
    7.2. [랜덤서치](#랜덤서치)  
    7.3. [베이지안 최적화](#베이지안-최적화) 

<br/><br/>

-------

<br/><br/>

# 분류와 회귀
해결하려는 문제의 타겟이 수치형이면 회귀, 범주형이면 분류의 문제로 볼 수있다.(캐글에서는 대부분 분류문제)  

<br/>

## 분류
타겟의 갯수에 따라 이진분류, 다중분류로 나뉘어지며 데이터들을 정해진 범위의 범주로 나누는것을 분류 문제라고 한다.

<br/>

## 회귀
어떠한 영향을 주는 피쳐들로 이루어진 독립변수와 영향을 받는 변수인 종속변수로 이루어지며 두변수간의 관계를 통하여 데이터가 주어질때 종속변수값을 예측하는것을 회귀문제라고 한다. 종속변수가 다변항일 경우 다중선형회귀, 단일항일 경우 단순 선형 회귀로 분류가 가능하다.  
* 회귀 평가지표  
분류는 범주에 옳게 나뉘어지는 것을 토대로 성능을 알 수 있지만, 회귀의 경우 수치형으로 이루어지기 때문에 예측값과 실제값간의 오차를 통하여 성능평가가 가능하다. 하지만 오차가 매우 작으면 오버피팅된 모델일 수 있기에 오버피팅여부의 확인도 중요하다.  

|평가지표|수식|설명|
|--|--|--|
|MAE|${1 \over N} \sum_{i=1}^N\|y_i - \hat{y_i}\|$||
|MSE|${1 \over N} \sum_{i=1}^N(y_i - \hat{y_i})^2$||
|RMSE|$\sqrt{{1 \over N} \sum_{i=1}^N(y_i - \hat{y_i})^2}$||
|MSLE|${1 \over N} \sum_{i=1}^N(log(y_i+1)-log(\hat{y_i}+1))^2$|$-\infty$를 방지하기 위하여 log에 +1을 취함|
|RMSLE|$\sqrt{{1 \over N} \sum_{i=1}^N(log(y_i+1)-log(\hat{y_i}+1))^2}$|$-\infty$를 방지하기 위하여 log에 +1을 취함|
|$R^2$|$ \hat{\sigma}^2 \over {\sigma}^2$|1에 근첩하는게 정확도가 높음|  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#회귀)

* 상관계수  
일반적으로 피이슨 상관계수를 나타내며 경향의 강도, 경향의 방향을 가진다.

<br/><br/>

# 분류 평가지표

<br/>

## 오차 행렬(confusion matrix)  
다음과 같이 예측값을 기준으로 positive와 negative를 가지며 실제값과 맞으면 True 틀리면 False를 가진다. 타겟값이 discrete해야함(값이 1에 가까우면 좋음)  

<table>
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>predict</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>positive</td>
      <td>negative</td>
    </tr>
    <tr>
      <td rowspan="2">real</td>
      <td>positive</td>
      <td>TP</td>
      <td>FN</td>
    </tr>
    <tr>
      <td>negative</td>
      <td>FP</td>
      <td>TN</td>
    </tr>
  </tbody>
</table>

* 정확도(accuracy)  
전체에서 True가 차지하는 비율  
(*모델의 우수성을 따질때 잘 사용하지 않음)  
${TP+TN}\over{TP+TN+FP+FN}$

* 정밀도(precision)  
Positive predict중의 True가 차지하는 비율  
(*실제 negative가 positive로 측정되는것이 critical할때 사용)  
${TP}\over{TP+FP}$

* 재현율(recall)(TPR)  
positive real중의 True가 차지하는 비율  
(*실제 positive가 negative로 측정되는것이 critical할때 사용)  
${TP}\over{TP+FN}$

* F1 점수(F1 score)  
정밀도와 재현율의 조화평균으로 편중되지않은 균등한 모델을 만들때 사용  
${2}\over{{{1} \over {precision}}+{{1} \over {recall}}}$

<br/>

## 로그 손실  
타겟을 확률적으로 예측시 사용되는 모델(0에 가까울 수록 좋음)  
$logloss = -{{1}\over{N}}\sum_{i=1}^N(y_ilog(\hat{y_i})+(1-y_i)log(1-\hat{y_i}))$

<br/>

## ROC 곡선과 AUC  
FPR에 대한 TPR을 ROC 곡선이라고 칭하며 ROC 곡선의 하단부 영역의 면적을 AUC라고 한다.  
로그손실과 같이 예측값이 확률일때 사용하게 된다.  
$FPR = 1 - TNR$  
TNR은 특이도(specificity)라고도 불린다.
<center>
  <img
    src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Roc_curve.svg/512px-Roc_curve.svg.png"
    width="350"
    height="400"
  />
</center>

<br/><br/>

# 데이터 인코딩
범주형 데이터를 숫자(수치형X)로 바꿔주는 작업  
숫자로 이루어진 범주형 데이터도 성능향상을 위해 넣어주기도 함  

<br/>

## 레이블 인코딩  
범주형 데이터를 숫자로 1대1 매칭해주는 방법(1차원 데이터)  
데이터간의 상관관계가 있을때 사용  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#레이블-인코딩)

<br/>

## 오디널 인코딩  
범주형 데이터를 숫자로 1대1 매칭해주는 방법(고차원 데이터)  
데이터간의 상관관계가 있을때 사용  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#오디널-인코딩)

<br/>

## 원-핫 인코딩  
범주형 데이터 value수 만큼 feature를 늘려서 해당하면 1 아니면 0을 나타냄  
메모리를 아끼기위하여 Compressed sparse row로 변환됨  
데이터간의 상관관계가 없을때 사용  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#원-핫-인코딩)

<br/><br/>

# 피쳐 스케일링
피쳐들마다 범위가 다르기때문에 범위를 조절하는 기법  
tree model은 피쳐들간의 크기에 영향을 받지 않아 필요없음  

<br/>

## min-max 정규화(normalization)  
0~1의 범위의 값으로 수치를 변화시키는것을 의미하며 아래의 식으로 변환됨  
(outlier에 취약함)  
$x_{scaled} = {{x-x_{min}} \over {x_{max}-x_{min}}}$  
fit, transform을 따로 할때 음수 발현가능

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#min-max-정규화normalization)

<br/>

## 표준화(standardization)  
평균이 0, 분산이 1이 되게 피쳐를 조정  
$x_{scaled} = {{x-\hat{x}}\over{\sigma}}$

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#min-max-표준화standardization)

<br/><br/>

# 교차 검증
모델의 성능을 검증하는 방법으로 아래의 문제해결을 위해 사용됨  
* 과적합  
훈련, 테스트 데이터셋이 고정되면 과적합 가능성이 높아짐
* 명확한 성능확인  
경진대회에서는 제출제한 횟수, 실제에서는 실제데이터 적용의 문제로 명확하게 성능확인이 힘들 수 있음

<br/>

## K 폴드 교차 검증  
아래의 진행방식을 가지는 검증법  
1. 데이터를 K개의 그룹으로 나눔
2. 그룹을 하나의 valid_data, K-1의 practive_data로 지정하여 여러 폴드 생성
3. K개의 폴드를 평가 후 평균을 구함

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#K-폴드-교차-검증)

<br/>

## 층화 K 폴드 교차 검증  
K 폴드 교차 검증에서 업그레이드 버전으로 분류문제에서 주로 사용  
아래와 같을때 사용함
* 특정 타겟이 다른 타겟에 비해 너무 적을때  
* 특정 타겟의 균등한 분배가 필요할때

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#층화-K-폴드-교차-검증)

<br/><br/>

# 주요 머신러닝 모델

<br/>

## 선형 회귀 모델  
선형 회귀식을 사용하는 모델

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#선형-회귀-모델)

<br/>

## 로지스틱 회귀 모델  
$x$가 변할때 $y$가 1이 되는 경향성을 따지는 모델
* odds  
성공확률과 실패 확률의 비율  

$$odds = \tfrac{p(y=1|x)}{1-p(y=1|x)}$$

* logit  
odds에 log를 취한 함수  

$$logit(p) = log(\tfrac{p}{1-p})$$

* sigmoid function  
logit 함수의 입력과 출력을 바꾼함수  

$$p(X) = \tfrac{1}{1+e^{-\beta X}}$$

* logistic function  
sigmoid 함수 만들어진 예측 모델  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#로지스틱-회귀-모델)

<br/>

## 결정 트리  
분류와 회귀 모두에 활용이 되는 모델이며 아래의 구조를 따름  
1. 조건의 생성
2. 조건으로 데이터 분할
3. 반복  

분할을 할때는 불순도를 최소화하는 방향으로 진행  

tree는 root(뿌리), intermediate(중간), leaf(말단) node로 나뉘어짐  

* 엔트로피  
불확실도를 의미하며 불순도가 높으면 낮아진다 0~1
* 정보 이득(information gain)  
트리는 정보 이득이 최대(엔트로피 최소)가 되게 분할된다.
* 지니 불순도(gini impurity)  
엔트로피와 비슷한 개념

<br/>

## 앙상블 학습  
다양한 모델에서 나온 결과를 복합적으로 사용하여 성능을 향상하는 기법

* 하드 보팅(hard voting)  
실행한 모델들에서 나온 결과에서 다수결 투표를 진행
* 소프트 보팅(soft voting)  
실행한 모델들에서 나온 확률의 평균값으로 진행

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#앙상블-학습)

* 배깅(bagging)  
개별 모델에 다른 데이터셋(랜덤 샘플링(복원 추출)을 통하여 샘플수를 늘리는 방식)을 활용해 보팅하는 방식

* 부스팅(boosting)  
가중치를 활용해 다음 모델학습시 오차를 줄이고 결과들을 결합하는 방식

<br/>

## 랜덤 포레스트  
결정 트리에 배깅을 시행한 앙상블 기법

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#랜덤-포레스트)

<br/>

## XGBoost  
결정 트리에 부스팅을 시행한 앙상블 기법

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#XGBoost)

<br/>

## LightGBM  
결정 트리에 부스팅을 시행한 앙상블 기법으로 XGBoost와 다르게 lead node가 예측 오류가 최소가되는 방향으로 깊이 분할을 합니다.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#XGBoost)

<br/><br/>

# 하이퍼 파라미터 최적화
최적의 파라미터를 찾아가는 방법

<br/>

## 그리드서치  
기본적인 기법으로 입력한 모든 파라미터를 전부 실행

<br/>

## 랜덤서치  
그리드 서치에서 무작위로 추출하여 최적의 파라미터를 찾아가기

<br/>

## 베이지안 최적화  
사전 정보를 바탕으로 최적의 파라미터를 찾아가기

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part2/chapter5.ipynb#베이지안-최적화)
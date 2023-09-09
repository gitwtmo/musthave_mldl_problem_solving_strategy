## 목차
1. [데이터 종류](#데이터-종류)  
    1.1. [수치형 데이터](#수치형-데이터)  
    1.2. [범주형 데이터](#범주형-데이터)  
2. [탐색적 데이터 분석과 그래프](#탐색적-데이터-분석과-그래프)  
3. [수치형 데이터 시각화](#수치형-데이터-시각화)  
    3.1. [히스토그램(histplot)](#히스토그램histplot)  
    3.2. [커널밀도추정 함수 그래프(kdeplot)](#커널밀도추정-함수-그래프kdeplot)  
    3.3. [분포도(displot)](#분포도displot)  
    3.4. [러그플롯(rugplot)](#러그플롯rugplot)  
4. [범주형 데이터 시각화](#범주형-데이터-시각화)  
    4.1. [막대 그래프(barplot)](#막대-그래프barplot)  
    4.2. [포인트플롯(pointplot)](#포인트플롯pointplot)  
    4.3. [박스플롯(boxplot)](#박스플롯boxplot)  
    4.4. [바이올린플롯(violinplot)](#바이올린플롯violinplot)  
    4.5. [카운트플롯(countplot)](#카운트플롯countplot)  
    4.6. [파이크래프(pie)](#파이크래프pie)  
5. [데이터 관계 시각화](#데이터-관계-시각화)  
    5.1. [히트맵(heatmap)](#히트맵heatmap)  
    5.2. [라인플롯(lineplot)](#라인플롯lineplot)  
    5.3. [산점도(scatterplot)](#산점도scatterplot)  
    5.4. [회귀선을 포함한 산점도 그래프(regplot)](#회귀선을-포함한-산점도-그래프regplot)  

<br/><br/>

-------

<br/><br/>

# 데이터 종류

<table>
  <thead>
    <tr>
      <th>대분류</th>
      <th>소분류</th>
      <th>예시</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">수치형</td>
      <td>연속형</td>
      <td>키, 수입</td>
    </tr>
    <tr>
      <td>이산형</td>
      <td>책의 페이지</td>
    </tr>
    <tr>
      <td rowspan="2">범주형</td>
      <td>순서형</td>
      <td>학점</td>
    </tr>
    <tr>
      <td>명목형</td>
      <td>성별</td>
    </tr>
  </tbody>
</table>

<br/>

## 수치형 데이터

사칙연산이 가능한 데이터  
* 연속형 : 연속으로 표현이 가능한 실수형 데이터
* 이산형 : 연속으로 표현이 가능한 정수형 데이터

<br/>

## 범주형 데이터

범주를 구분가능한 사칙연산이 불가능한 데이터  
* 순서형 : 순위로 표현이 가능한 데이터
* 명목형 : 순위로 표현이 불가능한 데이터

<br/><br/>

# 탐색적 데이터 분석과 그래프
다양한 그래프를 활용하여 데이터를 분석하고 중요한 피쳐를 찾고 불필요한 피쳐를 삭제함

<br/><br/>

# 수치형 데이터 시각화
일정한 범위에서 분포도를 보는것이 중요  

<br/>

## 히스토그램(histplot)
구간별 빈도수를 나타내는 그래프
```
sns.histplot(data=<data_set>, x=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#히스토그램histplot)
<br/><br/>

## 커널밀도추정 함수 그래프(kdeplot)
쉽게 표현하면 히스토그램을 스무딩하여 표현하는것과 유사한것  
정확한 표현은 적분시 1의 값을 가지는 함수를 커널함수, 관측한 데이터로 원래의 확률을 추정하는것을 밀도추정이라고 할때, 커널함수를 이용한 밀도 추정을 시행한 것  

```
sns.kdeplot(data=<data_set>, x=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#커널밀도추정-함수-그래프kdeplot)
<br/><br/>

## 분포도(displot)
분포도를 나타내는 그래프로 파라미터 조정으로 hist, kde 둘다 표현이 가능
```
sns.displot(data=<data_set>, x=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#분포도displot)
<br/><br/>

## 러그플롯(rugplot)
주변 분포도를 알 수 있으며 보통 다른분포와 같이 사용  
kde에서 kernel의 위치를 참고할 수 있음
```
sns.rugplot(data=<data_set>, x=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#러그플롯rugplot)
<br/><br/><br/>

# 범주형 데이터 시각화

<br/>

## 막대 그래프(barplot)
범주형 데이터에 따라서 수치형 데이터가 변화하는것을 표현하는데 적합하며 수치형 데이터의 다양한 값을 확인가능(functional input, confidence interval)
```
sns.barplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#막대-그래프barplot)
<br/><br/>

## 포인트플롯(pointplot)
막대 그래프와 표현이 같으며 선과 점으로 나타낸다. hue가 있을때 막대 그래프보다 가시성이 좋다.
```
sns.pointplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#포인트플롯pointplot)
<br/><br/>

## 박스플롯(boxplot)
사분위와 IQR을 이용하여 나타내며 이상치를 알 수 있다.
```
sns.boxplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#박스플롯boxplot)
<br/><br/>

## 바이올린플롯(violinplot)
박스플롯과 커널밀도함수의 융합
```
sns.violinplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#바이올린플롯violinplot)
<br/><br/>

## 카운트플롯(countplot)
막대그래프와 다르게 하나의 범주형 피쳐에 대한 갯수를 알 수 있다
```
sns.countplot(data=<data_set>, x=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#카운트플롯countplot)
<br/><br/>

## 파이크래프(pie)
범주형 데이터의 비율을 볼때 유용
```
import matplotlib.pyplot as plt
plt.pie(x=x, labels=<data_set>, autopct='%.1f%%')
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#파이크래프pie)
<br/><br/><br/>

# 데이터 관계 시각화

<br/>

## 히트맵(heatmap)
데이터간의 관계를 수치와 색상으로 표현하는 방법
```
pivot=<data_set>.pivot(index=, columns=, values=)
sns.heatmap(data=<pivot>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#히트맵heatmap)
<br/><br/>

## 라인플롯(lineplot)
수치형 데이터간의 관계를 나타내는 그래프(confidence interval)
```
sns.lineplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#라인플롯lineplot)
<br/><br/>

## 산점도(scatterplot)
두 데이터의 관계를 점으로 표현하는 방법
```
sns.scatterplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#산점도scatterplot)
<br/><br/>

## 회귀선을 포함한 산점도 그래프(regplot)
산점도와 회귀선을 같이 표현(axis-level-function, confidence interval)
axis-level은 정해진 figure에서 엑션을 취함
```
sns.regplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#회귀선을-포함한-산점도-그래프regplot)
<br/><br/>

## 회귀선을 포함한 산점도 그래프(lmplot)
산점도와 회귀선을 같이 표현(figure-level-function, confidence interval)
figure-level은 grid단에서 액션을 취하기 때문에 여러 figure를 그릴 수 있음
```
sns.lmplot(data=<data_set>, x=<colum_name>, y=<colum_name>, hue=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#회귀선을-포함한-산점도-그래프lmplot)
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
아래의 코드는 수치형 데이터 분석에 사용되는 기본 코드입니다.
```
import seaborn as sns
<data_set> = sns.load_dataset('titanic')
```

<br/>

## 히스토그램(histplot)
```
sns.histplot(data=<data_set>, x=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#scrollTo=zslTSLN-DuDM)
<br/><br/>

## 커널밀도추정 함수 그래프(kdeplot)
```
sns.kdeplot(data=<data_set>, x=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#scrollTo=5pSIaWY8DuDN)
<br/><br/>

## 분포도(displot)
```
sns.displot(data=<data_set>, x=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#분포도displot)
<br/><br/>

## 러그플롯(rugplot)
```
sns.rugplot(data=<data_set>, x=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#scrollTo=qIqq5GjJDuDN)
<br/><br/><br/>

# 범주형 데이터 시각화
ㅇㅇ
```
import seaborn as sns
<data_set> = sns.load_dataset('titanic')
```

<br/>

## 막대 그래프(barplot)
```
sns.barplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#scrollTo=IdSISTQcDuDO)
<br/><br/>

## 포인트플롯(pointplot)
```
sns.pointplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#scrollTo=vasrGJ9fDuDO)
<br/><br/>

## 박스플롯(boxplot)
```
sns.boxplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#scrollTo=yeN0jnRWDuDO)
<br/><br/>

## 바이올린플롯(violinplot)
```
sns.violinplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#scrollTo=4lbsdj4fDuDO)
<br/><br/>

## 카운트플롯(countplot)
```
sns.countplot(data=<data_set>, x=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#scrollTo=3TnwZSTbDuDO)
<br/><br/>

## 파이크래프(pie)
```
import matplotlib.pyplot as plt
plt.pie(x=x, label=<data_set>, autopct='%.1f%%')
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#scrollTo=ZfTTbrnIDuDO)
<br/><br/><br/>

# 데이터 관계 시각화
ㅇㅇ
```
import seaborn as sns
<data_set> = sns.load_dataset('flights')
```

<br/>

## 히트맵(heatmap)
```
pivot=<data_set>.pivot(index=, columns=, values=)
sns.heatmap(data=<pivot>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#scrollTo=c5J72GZ9DuDO)
<br/><br/>

## 라인플롯(lineplot)
```
sns.lineplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#scrollTo=cErNQUOuDuDO)
<br/><br/>

## 산점도(scatterplot)
```
sns.scatterplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#scrollTo=k4Qdw8wwDuDO)
<br/><br/>

## 회귀선을 포함한 산점도 그래프(regplot)
```
sns.regplot(data=<data_set>, x=<colum_name>, y=<colum_name>)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter4.ipynb#scrollTo=TLI8S7P_DuDO)
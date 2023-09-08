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
titanic = sns.load_dataset('titanic')
```

<br/>

## 히스토그램(histplot)
```
sns.histplot(data=titanic, x='age')
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/part1/chapter3.ipynb#히스)
<br/>

## 커널밀도추정 함수 그래프(kdeplot)


<br/>

## 분포도(displot)


<br/>

## 러그플롯(rugplot)


<br/><br/>

# 범주형 데이터 시각화


<br/>

## 막대 그래프(barplot)


<br/>

## 포인트플롯(pointplot)


<br/>

## 박스플롯(boxplot)


<br/>

## 바이올린플롯(violinplot)


<br/>

## 카운트플롯(countplot)


<br/>

## 파이크래프(pie)


<br/><br/>

# 데이터 관계 시각화


<br/>

## 히트맵(heatmap)


<br/>

## 라인플롯(lineplot)


<br/>

## 산점도(scatterplot)


<br/>

## 회귀선을 포함한 산점도 그래프(regplot)

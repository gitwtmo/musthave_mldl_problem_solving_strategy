## 목차
1. [plotly](#plotly)  
    1.1. [installation](#installation)  
2. [plotly 모듈](#plotly-모듈)  
    2.1. [express](#express)  
    2.2. [graph_objects](#graph_objects)  
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

# plotly
인터렉티브한 시각화 라이브러리로 [chart studio](https://chart-studio.plotly.com/create/#/), [Dash](https://plotly.com/dash/)와 연동이 가능

<br/>

## installation

* plotly : pip install plotly
* 정적 그림 저장 : pip install kaleido
* 추세선 추가하기 : pip install statsmodels

<br/><br/>

# plotly 모듈
사용자가 빠르고 쉽게 데이터분석을 할 수 있게 하는 express와 미세조정을 통하여 더 가시성이 좋게 나타낼 수 있는 graph_objects로 나뉘게 된다.

<br/>

## express
플롯이 담긴 figure로 만들어내는 방법
```
import plotly.express as px
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/appendix/plotly.ipynb#커널밀도추정-함수-그래프kdeplot)

<br/>

## graph_objects
figure를 만들고 figure위에 플롯을 만들어내는 방법
```
import plotly.graph_objects as go
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gitwtmo/musthave_mldl_problem_solving_strategy/blob/main/Indexs/appendix/plotly.ipynb#커널밀도추정-함수-그래프kdeplot)

<br/><br/>

# p
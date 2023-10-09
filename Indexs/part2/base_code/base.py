import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def resumetable(df):
    summary = pd.DataFrame(df.dtypes, columns=['type'])
    summary = summary.reset_index()
    summary = summary.rename(columns={'index':'피쳐'})
    summary['결측치'] = df.isnull().sum().values
    summary['고유값'] = df.nunique().values
    summary['임의값'] = df.loc[0].values

    return summary


def write_percent(fig, total_size):
    for patch in fig.patches:
        height = patch.get_height()
        width = patch.get_width()
        left_coord = patch.get_x()
        percent = height/total_size*100

        fig.text(x=left_coord + width/2,
                 y=height + total_size*0.001,
                 s=f'{percent:1.1f}%',
                 ha='center'
                )
    return None


def get_crosstab(df, feature):
    crosstab = pd.crosstab(df[feature], df['target'], normalize='index')*100
    crosstab = crosstab.reset_index()
    return crosstab


def plot_pointplot(ax, feature, crosstab, train):
    # sns.countplot(data=train, x=feature, order=crosstab[feature].values, ax=ax)
    ax2 = ax.twinx()
    ax2 = sns.pointplot(x=feature, y=1, data=crosstab, order=crosstab[feature].values)
    ax2.set_ylabel('Target Ratio(%)')
    return None


def plot_ratio(df, features, num_rows, num_cols, x_size, size=(12,18), wspace=0.45, option='point'):
    plt.figure(figsize=size)
    grid = gridspec.GridSpec(num_rows,num_cols)
    plt.subplots_adjust(wspace=wspace, hspace=0.3)

    for idx, feature in enumerate(features):
        ax = plt.subplot(grid[idx])
        crosstab = get_crosstab(df, feature)

        if x_size:
            df[feature] = pd.cut(df[feature], x_size)
        
        write_percent(ax, len(df))
        if option == 'point':
            sns.countplot(x=feature, data=df,
                     order=crosstab[feature].values,
                     color='skyblue',
                     ax=ax)
            plot_pointplot(ax, feature, crosstab, df)
        elif option == 'bar':
            sns.barplot(ax=ax, x=feature, y='target', data=df, palette='Set2')

        ax.set_title(f'{feature} Dis')
    
    return None
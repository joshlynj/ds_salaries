import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from clean import add_job_count

ds_df = pd.read_csv('/Users/joshy/Desktop/dai/daimil5/projects/'
                    'midterm/ds_salaries/data/ds_salaries.csv')


def plot_highest_pay(highest_pay_top):
    ''' Function takes in the highest paid data frame
        Returns a bar graph'''
    fig, ax1 = plt.subplots(figsize=(16, 9))
    sns.barplot(y=highest_pay_top.index,
                x=highest_pay_top.salary_in_usd,
                orient="h",
                palette="crest")
    plt.xlabel('Salary (in USD)', size=15)
    plt.ylabel('Job Title', size=15)
    plt.title('The 10 Highest Paid Data Science Jobs (2020-2023)', size=18)
    return fig, ax1


def plot_lowest_pay(lowest_pay_top):
    ''' Function takes in the lowest paid data frame
        Returns a bar chart'''
    fig, ax1 = plt.subplots(figsize=(16, 9))
    sns.barplot(y=lowest_pay_top.index,
                x=lowest_pay_top.salary_in_usd,
                orient="h",
                palette="crest")
    plt.xlabel('Salary (in USD)', size=15)
    plt.ylabel('Job Title', size=15)
    plt.title('The 10 Lowest Paid Data Science Jobs (2020-2023)', size=18)
    return fig, ax1


def plot_most_common(most_common_df):
    '''Function that takes in a dataframe
        Returns a dual axes graph'''
    add_job_count(ds_df)
    fig, ax1 = plt.subplots(figsize=(16, 9))
    sns.barplot(x=most_common_df.index,
                y=most_common_df.salary_in_usd,
                palette="crest")
    ax2 = ax1.twinx()
    sns.lineplot(data=most_common_df['job_count'],
                 marker='o',
                 sort=False,
                 ax=ax2,
                 color='#aa42f5')
    ax1.set_ylabel('Salary (in USD)',
                   size=15)
    ax2.set_ylabel('Job Count',
                   size=15,
                   color='#aa42f5')
    ax1.set_xlabel('Job Title',
                   size=15)
    ax1.tick_params(axis='x', rotation=45)
    plt.title('The 10 Most Common Jobs and Their Average Pay (2020-2023)',
              size=18)
    return fig, ax1


def plot_remote_size(s_df, m_df, l_df):
    '''Function that takes in 3 dataframes
    Returns a plot of the data in 3 bar graphs'''
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16, 6))

    sns.countplot(x='remote_ratio', data=s_df, ax=axes[0], palette="crest")
    axes[0].set_title('Small Company', fontsize=15)
    axes[0].set_xlabel('Remote Ratio', fontsize=15)
    axes[0].set_ylabel('Jobs Total', fontsize=15)

    sns.countplot(x='remote_ratio', data=m_df, ax=axes[1], palette="crest")
    axes[1].set_title('Medium Company', fontsize=15)
    axes[1].set_xlabel('Remote Ratio', fontsize=15)
    axes[1].set_ylabel('Jobs Total', fontsize=15)

    sns.countplot(x='remote_ratio', data=l_df, ax=axes[2], palette="crest")
    axes[2].set_title('Large Company', fontsize=15)
    axes[2].set_xlabel('Remote Ratio', fontsize=15)
    axes[2].set_ylabel('Jobs Total', fontsize=15)

    plt.suptitle('Remote Ratios by Company Size 2020-2023', fontsize=18)

    plt.tight_layout()

    return fig, axes


def plot_exp(exp_df):
    '''Function takes in a dataframe
        Returns a boxplot'''
    fig, ax = plt.subplots(figsize=(8, 6))
    order = ['EN', 'MI', 'SE', 'EX']
    sns.boxplot(x='experience_level',
                y='salary_in_usd',
                data=exp_df,
                order=order,
                ax=ax,
                palette="crest")

    ax.set_xlabel('Experience Level', fontsize=15)
    ax.set_ylabel('Salary (in USD)', fontsize=15)
    ax.set_title('Salary Distribution by Experience Level (2020-2023)',
                 size=18)
    return fig, ax


if __name__ == '__main__':
    print(plot_highest_pay(ds_df))
    print(plot_lowest_pay(ds_df))
    print(plot_most_common(ds_df))
    print(plot_remote_size(ds_df, ds_df, ds_df))
    print(plot_exp(ds_df))

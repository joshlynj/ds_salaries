import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds_df = pd.read_csv('../data/ds_salaries.csv')


def plot_highest_pay():
    highest_pay = ds_df.groupby("job_title")["salary_in_usd",
                                             "employment_type",
                                             "company_location"].\
                                                min().sort_values(
                                                by='salary_in_usd',
                                                ascending=False)
    mask = highest_pay['company_location'].isin(["US"]) \
        & highest_pay['employment_type'].isin(["FT"])
    highest_pay_top = highest_pay[mask].head(10)

    fig, ax1 = plt.subplots(figsize=(16, 9))
    sns.barplot(y=highest_pay_top.index,
                x=highest_pay_top.salary_in_usd,
                orient="h",
                palette="crest")
    plt.xlabel('Salary (in USD)')
    plt.ylabel('Job Title')
    plt.title('The 10 Highest Paid Data Science Jobs In The U.S. (2022-2023)')
    return fig, ax1


if __name__ == '__main__':
    plot_highest_pay()

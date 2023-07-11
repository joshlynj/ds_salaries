import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds_df = pd.read_csv('/Users/joshy/Desktop/dai/daimil5/projects/midterm/ds_salaries/data/ds_salaries.csv')


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


def create_us_only():
    ft_only_df = ds_df.drop(ds_df[ds_df['employment_type'] != "FT"].index)
    us_ft_df = ft_only_df.drop(ft_only_df[ft_only_df['company_location']
                                          != "US"].index)
    return us_ft_df

def plot_most_common(us_ft_df):
    most_common_df = us_ft_df.groupby("job_count", 
                                      as_index=False)[["salary_in_usd",
                                                       "job_title"]].mean(numeric_only=True).sort_values(by = 'job_count', ascending=False).head(10)

    index_labels = ["Data Engineer", 
            "Data Scientist", 
            "Data Analyst", 
            "Machine Learning Engineer", 
            "Data Architect",
            "Analytics Engineer", 
            "Applied Scientist", 
            "Research Scientist", 
            "Data Science Manager", 
            "Research Engineer"]

    most_common_df.index = index_labels
    return most_common_df



if __name__ == '__main__':
    plot_highest_pay()
    create_us_only()

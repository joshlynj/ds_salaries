import pandas as pd

ds_df = pd.read_csv('/Users/joshy/Desktop/dai/daimil5/projects/'
                    'midterm/ds_salaries/data/ds_salaries.csv')


def create_highest_pay(ds_df):
    ''' Function takes in a dataframe
        Returns a dataframe that is grouped by the Job Title and Includes:
        Salary in USD, Employment Type, and Company Location'''
    highest_pay = ds_df.groupby("job_title")["salary_in_usd",
                                             "employment_type",
                                             "company_location"] \
        .min().sort_values(by='salary_in_usd', ascending=False)
    mask = highest_pay['company_location']\
        .isin(["US"]) & highest_pay['employment_type'].isin(["FT"])
    highest_pay_top = highest_pay[mask].head(10)
    return highest_pay_top


def create_lowest_pay(ds_df):
    ''' Function takes in a dataframe
    Returns a dataframe that is grouped by the Job Title and Includes:
    Salary in USD, Employment Type, and Company Location'''
    lowest_pay = ds_df.groupby("job_title")["salary_in_usd",
                                            "employment_type",
                                            "company_location"]\
        .min().sort_values(by='salary_in_usd',
                           ascending=True)
    mask = lowest_pay['company_location']\
        .isin(["US"]) & lowest_pay['employment_type'].isin(["FT"])
    lowest_pay_top = lowest_pay[mask].head(10)
    return lowest_pay_top


def create_us_only(ds_df):
    ''' Function takes in a dataframe
    Returns a dataframe that only shows U.S. entries'''
    ft_only_df = ds_df.drop(ds_df[ds_df['employment_type'] != "FT"].index)
    us_ft_df = ft_only_df \
        .drop(ft_only_df[ft_only_df['company_location'] != "US"].index)
    return us_ft_df


def add_job_count(us_ft_df):
    '''Function takes in a dataframe
    Returns a dataframe with a count of the jobs'''
    us_ft_df['job_count'] = us_ft_df\
        .groupby('job_title')['job_title']\
        .transform('count')
    return us_ft_df


def create_most_common(us_ft_df):
    ''' Function takes in a dataframe 
        Returns a dataframe that shows '''
    most_common_df = us_ft_df\
        .groupby("job_count",
                 as_index=False)[["salary_in_usd",
                                  "job_title"]]\
        .mean(numeric_only=True).sort_values(by='job_count',
                                             ascending=False)\
        .head(10)

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


def create_remote_df(us_ft_df):
    '''Function takes in a dataframe
        Returns a data frame with only the remote ratio and company size'''
    remote_df = us_ft_df[['remote_ratio',
                          "company_size"]]\
        .sort_values(by='company_size',
                     ascending=False)
    return remote_df


def create_s_df(remote_df):
    ''' Function takes in a remote dataframe
        Function returns the smallest company size '''
    s_df = remote_df[remote_df['company_size'] == 'S']
    return s_df


def create_m_df(remote_df):
    ''' Function takes in a remote dataframe
        Function returns the medium company size '''
    m_df = remote_df[remote_df['company_size'] == 'M']
    return m_df


def create_l_df(remote_df):
    ''' Function takes in a remote dataframe
        Function returns the large company size '''
    l_df = remote_df[remote_df['company_size'] == 'L']
    return l_df


def create_exp_df(us_ft_df):
    '''Function that takes in the U.S. only dataframe
    Returns a new dataframe with select columns'''
    exp_df = us_ft_df[['experience_level',
                       "salary_in_usd",
                       "job_title"]]\
        .sort_values(by='salary_in_usd',
                        ascending=False)
    return exp_df


if __name__ == '__main__':
    print(create_highest_pay(ds_df))
    print(create_lowest_pay(ds_df))
    print(create_us_only(ds_df))
    print(add_job_count(ds_df))
    print(create_most_common(ds_df))
    print(create_remote_df(ds_df))
    print(create_s_df(ds_df))
    print(create_m_df(ds_df))
    print(create_l_df(ds_df))
    print(create_exp_df(ds_df))

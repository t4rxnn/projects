import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with a Bachelor's degree
    total = len(df)
    bachelors = df[df['education'] == 'Bachelors']
    percentage_bachelors = round((len(bachelors) / total) * 100, 1)

    # 4. Advanced education
    advanced = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_edu_rich = round((len(advanced[advanced['salary'] == '>50K']) / len(advanced)) * 100, 1)
    lower_edu_rich = round((len(lower[lower['salary'] == '>50K']) / len(lower)) * 100, 1)

    # 5. Min hours and rich % among them
    min_hours = df['hours-per-week'].min()
    min_workers = df[df['hours-per-week'] == min_hours]
    rich_min_workers = round((len(min_workers[min_workers['salary'] == '>50K']) / len(min_workers)) * 100, 1)

    # 6. Country with highest % of rich people
    country_group = df.groupby('native-country')
    rich_by_country = country_group['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    highest_earning_country = rich_by_country.idxmax()
    highest_earning_country_percentage = round(rich_by_country.max(), 1)

    # 7. Most common rich job in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_edu_rich)
        print("Percentage without higher education that earn >50K:", lower_edu_rich)
        print("Min work time:", min_hours)
        print("Percentage of rich among min workers:", rich_min_workers)
        print("Country with highest % of rich:", highest_earning_country)
        print("Highest % of rich people in country:", highest_earning_country_percentage)
        print("Top occupation in India for >50K earners:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_hours,
        'rich_percentage_min_workers': rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

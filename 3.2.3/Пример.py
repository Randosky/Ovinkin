import pandas as pd

pd.set_option("expand_frame_repr", False)

file_name = input("Введите название файла: ")
vacancy_name = input("Введите название профессии: ")

df = pd.read_csv(file_name)

df["years"] = df["published_at"].apply(lambda date: int(".".join(date[:4].split("-"))))  # apply что-то вроде map
years = list(df["years"].unique())  # unique берет отдельную колонку в виде списка уникальных значений

for year in years:
    data = df[df["years"] == year]
    data.iloc[:, :6].to_csv(f"created_csv_files\\part_{year}.csv", index=False)

df["published_at"] = df["published_at"].apply(lambda date: int(".".join(date[:4].split("-"))))
years = list(df["published_at"].unique())
# df.loc[:, 'salary'] = df[['salary_from', 'salary_to']].mean(axis=1)
df.loc[:, 'salary'] = df.loc[:, ['salary_from', 'salary_to']].mean(axis=1)  # применить вычисление построчно
df_vacancy = df[df["name"].str.contains(vacancy_name)]  # вакансии по заданному названию профессии

salaries_by_year = {year: [] for year in years}
vacancies_by_year = {year: 0 for year in years}
inp_vacancy_salary = {year: [] for year in years}
inp_vacancy_count = {year: 0 for year in years}


def fill_dicts():
    for year in years:
        df_s = df[df['published_at'] == year]
        df_v_s = df_vacancy[df_vacancy['published_at'] == year]

        salaries_by_year[year] = int(df_s['salary'].mean())
        vacancies_by_year[year] = len(df_s)
        inp_vacancy_salary[year] = int(df_v_s['salary'].mean())
        inp_vacancy_count[year] = len(df_v_s)


print("Динамика уровня зарплат по годам:", salaries_by_year)
print("Динамика количества вакансий по годам:", vacancies_by_year)
print("Динамика уровня зарплат по годам для выбранной профессии:", inp_vacancy_salary)
print("Динамика количества вакансий по годам для выбранной профессии:", inp_vacancy_count)

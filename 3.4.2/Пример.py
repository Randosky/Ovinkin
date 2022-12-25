import pandas as pd


class UserInput:
    def __init__(self):
        self.file_name = input("Введите название файла: ")
        self.vacancy_name = input("Введите название профессии: ")


inputed = UserInput()
file, vac = inputed.file_name, inputed.vacancy_name
df = pd.read_csv(file)
df["years"] = df["published_at"].apply(lambda date: int(".".join(date[:4].split("-"))))
years = list(df["years"].unique())

df["published_at"] = df["published_at"].apply(lambda date: int(".".join(date[:4].split("-"))))
df['salary'] = df.loc[:, ['salary_from', 'salary_to']].mean(axis=1)

vacancies = len(df)
df["count"] = df.groupby("area_name")['area_name'].transform("count")
df_norm = df[df['count'] >= 0.01 * vacancies]
others = len(df[df['count'] < 0.01 * vacancies])
cities = list(df_norm["area_name"].unique())

print(others)
print(others /vacancies )
print( 0.3454583695106974)
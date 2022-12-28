import math
import sqlite3
from statistics import mean
import pandas as pd


def sort_area_dict(dictionary):
    sorted_tuples = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:10]
    sorted_dict = {k: v for k, v in sorted_tuples}
    return sorted_dict


def sort_dict(dictionary):
    sorted_dict = {}
    for key in sorted(dictionary):
        sorted_dict[key] = dictionary[key]
    return sorted_dict


print("Используемая база данных: new_vac_with_dif_currencies.db")
vac = input("Введите название профессии: ")
con = sqlite3.connect("new_vac_with_dif_currencies.db")
cur = con.cursor()
df = pd.read_sql("SELECT * From new_vac_with_dif_currencies", con)
df["published_at"] = df["published_at"].apply(lambda date: date[:4])
years = list(df["published_at"].unique())

salaries_by_year, vacancies_by_year, inp_vacancy_salary, inp_vacancy_count, salaries_areas, vacancies_areas \
        = {}, {}, {}, {}, {}, {}

# По городам
vacancies = len(df)
df["count"] = df.groupby("area_name")['area_name'].transform("count")
df_norm = df[df['count'] >= 0.01 * vacancies]
cities = list(df_norm["area_name"].unique())
others = len(df[df['count'] < 0.01 * vacancies]) / vacancies

for city in cities:
    df_s = df_norm[df_norm['area_name'] == city]
    salaries_areas[city] = int(df_s['salary'].mean())
    vacancies_areas[city] = round(len(df_s) / len(df), 4)

# По годам
df_vac = df[df["name"].str.contains(vac)]
for year in years:
    df_v_s = df_vac[df_vac['years'] == year]
    if not df_v_s.empty:
        inp_vacancy_salary[year] = int(df_v_s['salary'].mean())
        inp_vacancy_count[year] = len(df_v_s)

# Вывод
print("Динамика уровня зарплат по годам:", sort_dict(salaries_by_year))
print("Динамика количества вакансий по годам:", sort_dict(vacancies_by_year))
print("Динамика уровня зарплат по годам для выбранной профессии:", sort_dict(inp_vacancy_salary))
print("Динамика количества вакансий по годам для выбранной профессии:", sort_dict(inp_vacancy_count))
print("Уровень зарплат по городам (в порядке убывания):", sort_area_dict(salaries_areas))
print("Доля вакансий по городам (в порядке убывания):", sort_area_dict(vacancies_areas))


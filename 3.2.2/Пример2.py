import pandas as pd


def sort_area_dict(dictionary):
    sorted_tuples = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:10]
    sorted_dict = {k: v for k, v in sorted_tuples}
    return sorted_dict


currency_to_rub = {
    "AZN": 35.68,
    "BYR": 23.91,
    "EUR": 59.90,
    "GEL": 21.74,
    "KGS": 0.76,
    "KZT": 0.13,
    "RUR": 1,
    "UAH": 1.64,
    "USD": 60.66,
    "UZS": 0.0055,
}

pd.set_option("expand_frame_repr", False)

file_name = "5.csv"
vacancy_name = "Программист"

df = pd.read_csv(file_name)

df['salary'] = df.loc[:, ['salary_from', 'salary_to']].mean(axis=1)

salaries_areas = {}
vacancies_areas = {}


vacancies = len(df)
df["count"] = df.groupby("area_name")['area_name'].transform("count")
df_norm = df[df['count'] >= 0.01 * vacancies]
cities = list(df_norm["area_name"].unique())

for city in cities:
    df_s = df_norm[df_norm['area_name'] == city]
    salaries_areas[city] = int(df_s['salary'].mean())
    vacancies_areas[city] = round(len(df_s) / len(df), 4)

print(sort_area_dict(salaries_areas))
print(sort_area_dict(vacancies_areas))

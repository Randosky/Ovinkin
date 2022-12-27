import math
from statistics import mean

import pandas as pd


def get_salary(s_from, s_to, s_cur, date):
    date = date[1] + "/" + date[0]
    s_cur_value = 0

    if s_cur != "RUR" and (s_cur == s_cur) and s_cur in ["BYN", "BYR", "EUR", "KZT", "UAH", "USD"]:
        s_cur.replace("BYN", "BYR")
        df_date_row = df_date.loc[df_date["date"] == date]
        s_cur_value = df_date_row[s_cur].values[0]
    elif s_cur == "RUR":
        s_cur_value = 1

    if math.isnan(s_from) and not (math.isnan(s_to)):
        return s_to * s_cur_value
    elif not (math.isnan(s_from)) and math.isnan(s_to):
        return s_from * s_cur_value
    elif not (math.isnan(s_from)) and not (math.isnan(s_to)):
        return mean([s_from, s_to]) * s_cur_value


pd.set_option("expand_frame_repr", False)

file = "6.csv"
vac = "а"
reg = "Москва"
df = pd.read_csv(file)
df["years"] = df["published_at"].apply(lambda date: int(".".join(date[:4].split("-"))))
years = list(df["years"].unique())
df_date = pd.read_csv("CB_Currency.csv")
df["salary"] = df.apply(lambda row: get_salary(row["salary_from"], row["salary_to"], row["salary_currency"],
                                               row["published_at"][:7].split("-")), axis=1)
df_vac = df[df["name"].str.contains(vac)]

inp_vacancy_salary, inp_vacancy_count = {}, {}

for year in years:
    df_v_s = df_vac[(df_vac['years'] == year) & (df_vac['area_name'] == reg)]
    if not df_v_s.empty:
        inp_vacancy_salary[year] = int(df_v_s['salary'].mean())
        inp_vacancy_count[year] = len(df_v_s)
#
print(inp_vacancy_salary)
print(inp_vacancy_count)

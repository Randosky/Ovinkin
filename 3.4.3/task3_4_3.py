# import math
# from statistics import mean
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from jinja2 import Environment, FileSystemLoader
# import pdfkit
# from matplotlib import ticker
#
#
# def sort_area_dict(dictionary):
#     sorted_tuples = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:10]
#     sorted_dict = {k: v for k, v in sorted_tuples}
#     return sorted_dict
#
#
# def sort_dict(dictionary):
#     sorted_dict = {}
#     for key in sorted(dictionary):
#         sorted_dict[key] = dictionary[key]
#     return sorted_dict
#
#
# def get_salary(s_from, s_to, s_cur, date):
#     date = date[1] + "/" + date[0]
#     s_cur_value = 0
#
#     if s_cur != "RUR" and (s_cur == s_cur) and s_cur in ["BYN", "BYR", "EUR", "KZT", "UAH", "USD"]:
#         s_cur.replace("BYN", "BYR")
#         df_date_row = df_date.loc[df_date["date"] == date]
#         s_cur_value = df_date_row[s_cur].values[0]
#     elif s_cur == "RUR":
#         s_cur_value = 1
#
#     if math.isnan(s_from) and not (math.isnan(s_to)):
#         return s_to * s_cur_value
#     elif not (math.isnan(s_from)) and math.isnan(s_to):
#         return s_from * s_cur_value
#     elif not (math.isnan(s_from)) and not (math.isnan(s_to)):
#         return mean([s_from, s_to]) * s_cur_value
#
#
# class UserInput:
#     def __init__(self):
#         self.file_name = input("Введите название файла: ")
#         self.vacancy_name = input("Введите название профессии: ")
#         self.region = input("Введите название региона: ")
#
#
# class Report:
#     def __init__(self, vac_name, region, dicts_by_area, dicts_by_year, vac_with_others):
#         self.generate_image(vac_name, region, dicts_by_area, dicts_by_year, vac_with_others)
#         self.generate_pdf(vac_name, region, dicts_by_area, dicts_by_year)
#
#     @staticmethod
#     def generate_pdf(vac_name, region, dicts_by_area, dicts_by_year):
#         env = Environment(loader=FileSystemLoader('.'))
#         template = env.get_template("pdf_template.html")
#
#         pdf_template = template.render(
#             {'name': vac_name, 'reg': region, 'by_area': dicts_by_area, 'by_year': dicts_by_year,
#              'keys_0_area': list(dicts_by_area[0].keys()), 'values_0_area': list(dicts_by_area[0].values()),
#              'keys_1_area': list(dicts_by_area[1].keys()), 'values_1_area': list(dicts_by_area[1].values())})
#
#         options = {'enable-local-file-access': None}
#         config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
#         pdfkit.from_string(pdf_template, 'report.pdf', configuration=config, options=options)
#
#     @staticmethod
#     def generate_image(vac_name, region, dicts_by_area, dicts_by_year, vac_with_others):
#         y1_cities = np.arange(len(dicts_by_area[0].keys()))
#         y1_cities_names = {}
#         for key, value in dicts_by_area[0].items():
#             if "-" in key or " " in key:
#                 key = key.replace("-", "-\n")
#                 key = key.replace(" ", "\n")
#             y1_cities_names[key] = value
#
#         x_nums = np.arange(len(dicts_by_year[0].keys()))
#         width = 0.4
#         x_list1 = x_nums
#         fig = plt.figure()
#
#         ax = fig.add_subplot(221)
#         ax.set_title("Уровень зарплат по годам")
#         ax.bar(x_list1, dicts_by_year[0].values(), width, label=f"з/п {vac_name.lower()} {region.lower()}")
#         ax.set_xticks(x_nums, dicts_by_year[0].keys(), rotation="vertical")
#         ax.tick_params(axis="both", labelsize=8)
#         ax.legend(fontsize=8)
#         ax.grid(True, axis="y")
#
#         ax = fig.add_subplot(222)
#         ax.set_title("Количество вакансий по годам")
#         ax.bar(x_list1, dicts_by_year[1].values(), width,
#                label=f"Количество вакансий \n{vac_name.lower()} {region.lower()}")
#         ax.set_xticks(x_nums, dicts_by_year[1].keys(), rotation="vertical")
#         ax.tick_params(axis="both", labelsize=8)
#         ax.legend(fontsize=8)
#         ax.grid(True, axis="y")
#
#         ax = fig.add_subplot(223)
#         ax.set_title("Уровень зарплат по городам")
#         width = 0.8
#         ax.barh(y1_cities, dicts_by_area[0].values(), width, align="center")
#         ax.set_yticks(y1_cities, labels=y1_cities_names.keys(), horizontalalignment="right", verticalalignment="center")
#         ax.tick_params(axis="x", labelsize=8)
#         ax.tick_params(axis="y", labelsize=6)
#         ax.xaxis.set_major_locator(ticker.MultipleLocator(100000))
#         ax.invert_yaxis()
#         ax.grid(True, axis="x")
#
#         ax = fig.add_subplot(224)
#         ax.set_title("Доля вакансий по городам")
#         dicts_by_area[1]["Другие"] = vac_with_others
#         ax.pie(dicts_by_area[1].values(), labels=dicts_by_area[1].keys(), textprops={'size': 6},
#                colors=["#ff8006", "#28a128", "#1978b5", "#0fbfd0", "#bdbe1c", "#808080", "#e478c3", "#8d554a",
#                        "#9567be",
#                        "#d72223", "#1978b5", "#ff8006"])
#         ax.axis('equal')
#
#         plt.tight_layout()
#         plt.savefig("graph.png")
#
#
# inputed = UserInput()
# file, vac, reg = inputed.file_name, inputed.vacancy_name, inputed.region
# df = pd.read_csv(file)
#
# df["years"] = df["published_at"].apply(lambda date: int(".".join(date[:4].split("-"))))
# years = list(df["years"].unique())
#
# salaries_areas, vacancies_areas, inp_vacancy_salary, inp_vacancy_count = {}, {}, {}, {}
#
# # Преобразование валют
# df_date = pd.read_csv("CB_Currency.csv")
# df["salary"] = df.apply(lambda row: get_salary(row["salary_from"], row["salary_to"], row["salary_currency"],
#                                                row["published_at"][:7].split("-")), axis=1)
# df = df[df["salary"].notnull()]
#
# # По городам
# vacancies = len(df)
# df["count"] = df.groupby("area_name")['area_name'].transform("count")
# df_norm = df[df['count'] >= 0.01 * vacancies]
# cities = list(df_norm["area_name"].unique())
# others = len(df[df['count'] < 0.01 * vacancies]) / vacancies
#
# for city in cities:
#     df_s = df_norm[df_norm['area_name'] == city]
#     salaries_areas[city] = int(df_s['salary'].mean())
#     vacancies_areas[city] = round(len(df_s) / len(df), 4)
#
# # По годам и региону
# df_vac = df[df["name"].str.contains(vac)]
# for year in years:
#     df_v_s = df_vac[(df_vac['years'] == year) & (df_vac['area_name'] == reg)]
#     if not df_v_s.empty:
#         inp_vacancy_salary[year] = int(df_v_s['salary'].mean())
#         inp_vacancy_count[year] = len(df_v_s)
#
# # Вывод
# print("Уровень зарплат по городам (в порядке убывания):", sort_area_dict(salaries_areas))
# print("Доля вакансий по городам (в порядке убывания):", sort_area_dict(vacancies_areas))
# print("Динамика уровня зарплат по годам для выбранной профессии и региона:", sort_dict(inp_vacancy_salary))
# print("Динамика количества вакансий по годам для выбранной профессии и региона:", sort_dict(inp_vacancy_count))
#
# dicts_list_by_area = [sort_area_dict(salaries_areas), sort_area_dict(vacancies_areas)]
# dicts_list_by_year = [sort_dict(inp_vacancy_salary), sort_dict(inp_vacancy_count)]
#
# report = Report(vac, reg, dicts_list_by_area, dicts_list_by_year, others)

import sqlite3
import pandas as pd

con = sqlite3.connect("new_vac_with_dif_currencies.db")
cur = con.cursor()
years = cur.execute("SELECT DISTINCT years From new_vac_with_dif_currencies").fetchall()


salaries_by_year, vacancies_by_year, inp_vacancy_salary, inp_vacancy_count, salaries_areas, vacancies_areas \
    = {}, {}, {}, {}, {}, {}

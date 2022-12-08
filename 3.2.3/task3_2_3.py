from concurrent import futures
import pandas as pd


def start_processes(arguments):
    vac_name = arguments[0]
    year = arguments[1]
    pr_df = pd.read_csv(f'created_csv_files\\part_{year}.csv')

    # применить вычисление построчно
    pr_df.loc[:, 'salary'] = pr_df.loc[:, ['salary_from', 'salary_to']].mean(axis=1)

    # вакансии по заданному названию профессии
    pr_df_vac = pr_df[pr_df["name"].str.contains(vac_name)]

    s_by_year, v_by_year, inp_v_s, inp_v_c = {year: []}, {year: 0}, {year: []}, {year: 0}

    s_by_year[year] = int(pr_df['salary'].mean())
    v_by_year[year] = len(pr_df)
    inp_v_s[year] = int(pr_df_vac['salary'].mean())
    inp_v_c[year] = len(pr_df_vac)

    d_list = [s_by_year, v_by_year, inp_v_s, inp_v_c]
    return d_list


if __name__ == "__main__":
    def sort_dict(dictionary):
        sorted_dict = {}
        for key in sorted(dictionary):
            sorted_dict[key] = dictionary[key]
        return sorted_dict


    def sort_area_dict(dictionary):
        sorted_tuples = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:10]
        sorted_dict = {k: v for k, v in sorted_tuples}
        return sorted_dict


    class UserInput:
        def __init__(self):
            self.file_name = input("Введите название файла: ")
            self.vacancy_name = input("Введите название профессии: ")


    class MakeCvs:
        def __init__(self, file_name):
            self.dataframe = pd.read_csv(file_name)

            self.dataframe["years"] = self.dataframe["published_at"].apply(
                lambda date: int(".".join(date[:4].split("-"))))
            self.years = list(self.dataframe["years"].unique())

            for year in self.years:
                data = self.dataframe[self.dataframe["years"] == year]
                data[["name", "salary_from", "salary_to",
                      "salary_currency", "area_name",
                      "published_at"]].to_csv(f"created_csv_files\\part_{year}.csv", index=False)


    inputed = UserInput()
    file, vac = inputed.file_name, inputed.vacancy_name
    make_csv = MakeCvs(file)
    df = make_csv.dataframe
    years = make_csv.years

    df["published_at"] = df["published_at"].apply(lambda date: int(".".join(date[:4].split("-"))))
    df['salary'] = df.loc[:, ['salary_from', 'salary_to']].mean(axis=1)

    vacancies = len(df)
    df["count"] = df.groupby("area_name")['area_name'].transform("count")
    df_norm = df[df['count'] >= 0.01 * vacancies]
    cities = list(df_norm["area_name"].unique())

    salaries_by_year, vacancies_by_year, inp_vacancy_salary, inp_vacancy_count, salaries_areas, vacancies_areas \
        = {}, {}, {}, {}, {}, {}

    for city in cities:
        df_s = df_norm[df_norm['area_name'] == city]
        salaries_areas[city] = int(df_s['salary'].mean())
        vacancies_areas[city] = round(len(df_s) / len(df), 4)

    executor = futures.ProcessPoolExecutor()
    processes = []
    for year in years:
        args = (vac, year)
        returned_list = executor.submit(start_processes, args).result()
        salaries_by_year.update(returned_list[0])
        vacancies_by_year.update(returned_list[1])
        inp_vacancy_salary.update(returned_list[2])
        inp_vacancy_count.update(returned_list[3])

    print("Динамика уровня зарплат по годам:", sort_dict(salaries_by_year))
    print("Динамика количества вакансий по годам:", sort_dict(vacancies_by_year))
    print("Динамика уровня зарплат по годам для выбранной профессии:", sort_dict(inp_vacancy_salary))
    print("Динамика количества вакансий по годам для выбранной профессии:", sort_dict(inp_vacancy_count))
    print("Уровень зарплат по городам (в порядке убывания):", sort_area_dict(salaries_areas))
    print("Доля вакансий по городам (в порядке убывания):", sort_area_dict(vacancies_areas))
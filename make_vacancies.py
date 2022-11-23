import os
import re
import csv
from prettytable import PrettyTable
from datetime import datetime


def quick_quit(msg):
    print(msg)
    exit(0)


rus_names = {
    "name": "Название",
    "description": "Описание",
    "key_skills": "Навыки",
    "experience_id": "Опыт работы",
    "premium": "Премиум-вакансия",
    'employer_name': 'Компания',
    'salary': 'Оклад',
    'area_name': 'Название региона',
    'published_at': 'Дата публикации вакансии',
}

experience = {
    "noExperience": "Нет опыта",
    "between1And3": "От 1 года до 3 лет",
    "between3And6": "От 3 до 6 лет",
    "moreThan6": "Более 6 лет",
}

experience_sort = {
    "Нет опыта": 0,
    "От 1 года до 3 лет": 1,
    "От 3 до 6 лет": 2,
    "Более 6 лет": 3,
}

currency = {
    "AZN": "Манаты",
    "BYR": "Белорусские рубли",
    "EUR": "Евро",
    "GEL": "Грузинский лари",
    "KGS": "Киргизский сом",
    "KZT": "Тенге",
    "RUR": "Рубли",
    "UAH": "Гривны",
    "USD": "Доллары",
    "UZS": "Узбекский сум",
}

sal_gross = {
    'True': 'Без вычета налогов',
    'False': 'С вычетом налогов',
    'TRUE': 'Без вычета налогов',
    'FALSE': 'С вычетом налогов',
}

premium = {
    'True': 'Да',
    'False': 'Нет',
    'TRUE': 'Да',
    'FALSE': 'Нет',
}

currency_to_rub = {
    "Манаты": 35.68,
    "Белорусские рубли": 23.91,
    "Евро": 59.90,
    "Грузинский лари": 21.74,
    "Киргизский сом": 0.76,
    "Тенге": 0.13,
    "Рубли": 1,
    "Гривны": 1.64,
    "Доллары": 60.66,
    "Узбекский сум": 0.0055,
}

names_to_eng = {
    "Название": 'name',
    "Описание": 'description',
    "Навыки": 'key_skills',
    "Опыт работы": 'experience_id',
    "Премиум-вакансия": 'premium',
    "Компания": 'employer_name',
    "Нижняя граница вилки оклада": 'salary_from',
    "Верхняя граница вилки оклада": 'salary_to',
    "Оклад указан до вычета налогов": 'salary_gross',
    "Идентификатор валюты оклада": 'salary_currency',
    "Оклад": 'salary',
    "Название региона": 'area_name',
    "Дата публикации вакансии": 'published_at',
}


class UserInput:
    filter_phrases = ["Название", "Навыки", "Опыт работы", "Премиум-вакансия", "Компания", "Оклад",
                      "Идентификатор валюты оклада", "Название региона", "Дата публикации вакансии"]

    sort_phrases = ["Название", "Описание", "Навыки", "Опыт работы", "Премиум-вакансия",
                    "Компания", "Оклад", "Название региона", "Дата публикации вакансии"]

    def __init__(self):
        self.file_name = input('Введите название файла: ')
        self.f_param = input('Введите параметр фильтрации: ')
        self.s_param = input('Введите параметр сортировки: ')
        self.r_s_param = input('Обратный порядок сортировки (Да / Нет): ')
        self.int_param = input('Введите диапазон вывода: ').split()
        self.names_param = self.check_names(input('Введите требуемые столбцы: ').split(', '))

        self.f_param = self.check_f_param(self.f_param)
        self.s_param = self.check_s_param(self.s_param)
        self.r_s_param = self.check_r_s_param(self.r_s_param)

    def check_f_param(self, f_param):
        if f_param != "" and ": " not in f_param:
            quick_quit("Формат ввода некорректен")

        if f_param != "" and f_param.split(": ")[0] not in self.filter_phrases:
            quick_quit("Параметр поиска некорректен")
        return f_param

    def check_s_param(self, s_param):
        if s_param != "" and s_param not in self.sort_phrases:
            quick_quit("Параметр сортировки некорректен")
        return s_param

    @staticmethod
    def check_r_s_param(r_s_param):
        if r_s_param not in ["Да", "Нет", ""]:
            quick_quit("Порядок сортировки задан некорректно")
        return r_s_param == "Да"

    @staticmethod
    def check_names(lst_names):
        if "" in lst_names:
            lst_names = ["Название", "Описание", "Навыки",
                         "Опыт работы", "Премиум-вакансия", 'Компания',
                         'Оклад', 'Название региона', 'Дата публикации вакансии']
        lst_names.insert(0, "№")
        return lst_names


class DataSet:
    def __init__(self, file_name):
        if os.stat(file_name).st_size == 0:
            quick_quit("Пустой файл")

        self.data = [row for row in csv.reader(open(file_name, encoding="utf_8_sig"))]
        self.names = self.data[0]
        self.all_data = [row for row in self.data[1:] if len(row) == len(self.names) and row.count('') == 0]

        if len(self.all_data) == 0:
            quick_quit('Нет данных')


class Vacancy:
    name: str
    description: str
    key_skills: str or list
    experience_id: str
    premium: str
    employer_name: str
    salary_from: int or float
    salary_to: int or float
    salary_gross: str
    salary_currency: str
    area_name: str
    full_published_time: str
    published_at: str
    salary: str

    def __init__(self, pers_data):
        for key, value in pers_data.items():
            self.__setattr__(key, self.formatter(key, value))

        self.salary = f'{self.salary_from} - {self.salary_to} ({self.salary_currency}) ({self.salary_gross})'

    def formatter(self, key, value):
        if key == 'key_skills' and type(value) == list:
            return "\n".join(value)
        elif key == 'premium':
            return premium[value]
        elif key == 'salary_gross':
            return sal_gross[value]
        elif key == 'experience_id':
            return experience[value]
        elif key == 'salary_currency':
            return currency[value]
        elif key == "salary_to" or key == "salary_from":
            return '{:,}'.format(int(float(value))).replace(',', ' ')
        elif key == 'published_at':
            self.full_published_time = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S%z').strftime("%d.%m.%Y-%H:%M:%S")
            return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S%z').strftime("%d.%m.%Y")
        else:
            return value

    def check_filter_cond(self, f_param):
        if f_param == '':
            return True

        f_key, f_value = f_param.split(': ')
        if f_key == 'Оклад':
            return float(self.salary_from.replace(' ', '')) <= float(f_value) <= float(self.salary_to.replace(' ', ''))
        elif f_key == 'Идентификатор валюты оклада':
            return self.salary_currency == f_value
        elif f_key == 'Навыки':
            for skill in f_value.split(", "):
                if skill not in self.key_skills.split("\n"):
                    return False
            return True
        else:
            return self.__dict__[names_to_eng[f_key]] == f_value


class Table:
    def __init__(self):
        self.table = PrettyTable(["№", "Название", "Описание", "Навыки", "Опыт работы", "Премиум-вакансия",
                                  'Компания', 'Оклад', 'Название региона', 'Дата публикации вакансии'])
        self.table.hrules = 1
        self.table.align = "l"
        self.table.max_width = 20

    def print(self, all_data, start, end, list_names):
        for index, pers_data in enumerate(all_data):
            row = [index + 1]
            for name in self.table.field_names[1:]:
                pers_data_value = pers_data.__dict__[names_to_eng[name]]

                if len(pers_data_value) > 100:
                    pers_data_value = pers_data_value[:100] + "..."
                row.append(pers_data_value)
            self.table.add_row(row)

        print(self.table.get_string(start=start, end=end, fields=list_names))


def get_vacancies(all_data, f_param, s_param, r_s_param, names):
    f_data = []
    for pers_data in all_data:
        parsed_data = Vacancy(dict(zip(names, map(parse_html, pers_data))))
        if parsed_data.check_filter_cond(f_param):
            f_data.append(parsed_data)
    return sort_vacancies(f_data, s_param, r_s_param)


def sort_vacancies(all_data, s_param, r_s_param):
    if s_param == "":
        return all_data

    return sorted(all_data, key=lambda pers_data: get_sort_func(pers_data, s_param), reverse=r_s_param)


def get_sort_func(pers_data, s_param):
    if s_param == "Навыки":
        return len(pers_data.key_skills.split("\n"))
    elif s_param == "Оклад":
        return currency_to_rub[pers_data.salary_currency] * (
                float(pers_data.salary_from.replace(' ', '')) + float(pers_data.salary_to.replace(' ', ''))) // 2
    elif s_param == "Дата публикации вакансии":
        return pers_data.full_published_time
    elif s_param == "Опыт работы":
        return experience_sort[pers_data.experience_id]
    else:
        return pers_data.__getattribute__(names_to_eng[s_param])


def parse_html(info):
    info = re.sub('<.*?>', '', info)
    info = info.replace("\r\n", "\n")
    res = [' '.join(word.split()) for word in info.split('\n')]
    return res[0] if len(res) == 1 else res


def print_vacancies(all_data, list_int, list_names):
    if len(all_data) == 0:
        quick_quit('Ничего не найдено')

    start = int(list_int[0]) - 1 if len(list_int) >= 1 else 0
    end = int(list_int[1]) - 1 if len(list_int) >= 2 else len(all_data)

    table = Table()
    table.print(all_data, start, end, list_names)


class StartProcess:
    def __init__(self):
        inputed = UserInput()
        dataset = DataSet(inputed.file_name)
        (names, all_vac_data) = dataset.names, dataset.all_data
        f_s_data = get_vacancies(all_vac_data, inputed.f_param, inputed.s_param, inputed.r_s_param, names)
        print_vacancies(f_s_data, inputed.int_param, inputed.names_param)

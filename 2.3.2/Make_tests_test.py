from unittest import TestCase
import Make_tests


class DataSetTests(TestCase):
    dataset = Make_tests.DataSet("4.csv")

    def test_names_type(self):
        self.assertEqual(type(self.dataset.names).__name__, "list")

    def test_zero_length_str(self):
        count = 0
        for value in self.dataset.all_data:
            if value == "":
                count += 1
        self.assertEqual(0, count)


class StaticInfoTests(TestCase):
    static = Make_tests.StaticInfo()
    currency_to_rub = {"Манаты": 35.68, "Белорусские рубли": 23.91, "Евро": 59.90, "Грузинский лари": 21.74,
                       "Киргизский сом": 0.76, "Тенге": 0.13, "Рубли": 1, "Гривны": 1.64, "Доллары": 60.66,
                       "Узбекский сум": 0.0055, }
    correct_dict = {"Доллары": 60.66, "Евро": 59.90, "Манаты": 35.68, "Белорусские рубли": 23.91,
                    "Грузинский лари": 21.74, "Гривны": 1.64, "Рубли": 1, "Киргизский сом": 0.76,
                    "Тенге": 0.13, "Узбекский сум": 0.0055, }

    def test_sort_dict(self):
        self.assertEqual(self.static.sort_dict(self.currency_to_rub), self.correct_dict)


class VacancyTest(TestCase):
    vac1 = Make_tests.Vacancy(
        {"name": "Программист", "salary_from": "10000", "salary_to": "20000", "salary_currency": "RUR",
         "area_name": "Екатеринбург", "published_at": "2022-01-12T14:12:06-0500"})
    vac2 = Make_tests.Vacancy(
        {"name": "Программист", "salary_from": "100", "salary_to": "5000", "salary_currency": "GEL",
         "area_name": "Екатеринбург", "published_at": "2022-01-12T14:12:06-0500"})

    def test_salary_from(self):
        self.assertEqual(self.vac1.salary_from, "10 000")

    def test_salary_to(self):
        self.assertEqual(self.vac1.salary_to, "20 000")

    def test_salary(self):
        self.assertEqual(self.vac1.salary, 15000)

    def test_salary_currency(self):
        self.assertEqual(self.vac2.salary, 55436)
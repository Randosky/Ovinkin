import make_vacancies
import make_pdf

inputed = input("Вакансии или Статистика: ")

if inputed == "Вакансии":
    make_vacancies.StartProcess()
elif inputed == "Статистика":
    make_pdf.StartProcess()
else:
    print("Вы ввели некорректное значение")

import make_vacancies
import make_pdf

<<<<<<< HEAD
inputed = input("Необходимо ввести слово Вакансии или Статистика: ")
=======
inputed = input("Введите слово Вакансии или Статистика: ")
>>>>>>> develop

if inputed == "Вакансии":
    make_vacancies.StartProcess()
elif inputed == "Статистика":
    make_pdf.StartProcess()
else:
    print("Вы ввели некорректное значение")

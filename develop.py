import make_tables
import make_graph

inputed = input("Вакансии или Статистика: ")

if inputed == "Вакансии":
    make_tables.StartProcess()
elif inputed == "Статистика":
    make_graph.StartProcess()
else:
    print("Вы ввели некорректное значение")

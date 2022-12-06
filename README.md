# Ovinkin
2.3.2

Проверка доктестов

![image](https://user-images.githubusercontent.com/103418173/204130682-05dcf43d-2b46-4eef-91c5-fd3c89527f76.png)

Проверка юниттестов

![image](https://user-images.githubusercontent.com/103418173/204130669-b84ce555-f800-440f-b876-39e371c7881f.png)


2.3.3

1-й вариант: 

Преобразование даты и времени с помощью datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z').strftime("%Y")

![image](https://user-images.githubusercontent.com/103418173/205276604-7b877ae7-7e56-4902-9dd0-6c443205ccfc.png)

2-й вариант: 

Преобразование даты и времени с помощью обрезания строки ".".join(date[:4].split("-"))

![image](https://user-images.githubusercontent.com/103418173/205272001-a97040c5-665c-46b5-860c-5e12850196b0.png)

3-й вариант: 

Преобразование даты и времени с помощью:

big, small = date[:19].split('T') 
year, month, day = big.split('-') 
new_data = int(year) 

![image](https://user-images.githubusercontent.com/103418173/205277745-0d87b4f5-2efc-4b2e-a15c-75fbb6cbd656.png)

Таким образом самый быстрый способ преобразования строки - обрезание строки с помощью ".".join(date[:4].split("-")). Его и оставляем

3.2.1

Созданные csv файлы

![image](https://user-images.githubusercontent.com/103418173/205935474-1054d3d2-fd7f-4d03-95c1-e8c22109aca9.png)

Соответствие колонок файлов

![image](https://user-images.githubusercontent.com/103418173/205935556-08cb09b7-f893-49f7-8cf4-bfc8ef828e87.png)

![image](https://user-images.githubusercontent.com/103418173/205935609-82ab07d1-9a2a-483f-a38f-e64ceeb7bd0d.png)

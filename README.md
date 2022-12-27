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



3.2.2



Без многопроцессорной обработки весь код выполнился за 18.840 секунд

![image](https://user-images.githubusercontent.com/103418173/206158509-d5149fa2-6e36-40e2-8fe2-8ff68efffc9e.png)

С многопроцессорной обработкой весь код выполнился за 12.326 секунд

![image](https://user-images.githubusercontent.com/103418173/206159829-b27e988b-978a-4e66-bacf-b2fa3cc8c496.png)



3.2.3



Многопроцессорная обработка с помощью Concurrent futures всего кода выполнилась за 8.918 секунд

![image](https://user-images.githubusercontent.com/103418173/206534124-58418363-23f0-4df4-9d97-3e6f6df2ec67.png)

Значит по итогу мы оставляем решение с Concurrent futures



3.3.1

Частотность подсчитаная двумя способами

![image](https://user-images.githubusercontent.com/103418173/208423143-dd7f7530-7aa1-4f8b-8872-7306f07a1a70.png)



3.3.3

Получившийся датафрейм

![image](https://user-images.githubusercontent.com/103418173/208748010-fc4e605b-c8bb-493e-8e57-13acc1b1fcc9.png)



3.5.1

Получившаяся база данных

![image](https://user-images.githubusercontent.com/103418173/209650963-d1434996-2586-425c-8af1-cbc76de47486.png)

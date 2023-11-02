# Уровень 2 кейс 10
## Описание:
Задача 1 «Программирование на Python»

Цель проектного задания:

Проверка базовых знаний языка программирования Python.

Формат применения кейс-задания:

Задание для отбора студентов к прохождению практики.

Исходные данные, постановка задачи и требования к результату:

На языке программирования Python необходимо написать следующие программы:

-Программа, которая находит и выводит все пифагоровы тройки (𝑥2+𝑦2=𝑧2) для 𝑧<=200, а также выводит их
количество.

-Программа, которая вычисляет и выводит N-ное простое число (например, сотое — 541). Номер простого
числа должен вводиться в программу через клавиатуру.

-Программа, которая создаёт массив, столбцы которого идентичны заданным массивам. Элементы
массива в каждом его столбце должны быть отсортированы в порядке возрастания значения (сверху вниз).
Значения всех элементов, расположенных на диагоналях массива, должны быть заменены на цифру 5. После
чего данный массив объединяется по третьему измерению с массивом такого же размера, но заполненного
случайными числами

от -10 до 0. Первые строчки кода:

- colum_1 = np.array([0, 1, 3, 1, 0])

- colum_2 = np.array([1, 3, 1, 4, 1])

- colum_3 = np.array([4, 1, 3, 5, 4])

- colum_4 = np.array([4, 8, 4, 8, 5])

- colum_5 = np.array([7, 1, 3, 1, 0])

# Инструкция запуска :
## Python/Python3 :
Необходимое ПО: python 3.*, git.
```console
example@user:~/$ git clone https://github.com/AlekseiYuzhanin/radar_python_projects
example@user:~/$ cd radar_python_projects
```
Для первого задания:
```console
example@user:~/radar_python_projects$ cd first_project

example@user:~/radar_python_projects/first_project$ python main.py

// Другой вариант

example@user:~/radar_python_projects/first_project$ python3 main.py
```
Для второго задания:
```console
example@user:~/radar_python_projects$ cd second_project

example@user:~radar_python_projects/second_project/$ python main.py

// Другой вариант

example@user:~/radar_python_projects/second_project$ python3 main.py

```
Для третьего задания:
```console
example@user:~/radar_python_projects$ pip install numpy

// Другой вариант

example@user:~/radar_python_projects$ apt-get install python-numpy

example@user:~/radar_python_projects$ cd third_project

example@user:~/radar_python_projects/third_project$ python main.py

// Другой вариант

example@user:~/radar_python_projects/third_project$ python3 main.py

```
## Venv :
Необходимые библиотеки: venv.
Для запуска приложения таким образом нужно установить Python. Venv необходимо для запуска третьего проекта, так как содержит в себе стороннюю библиотеку.
```console
example@user:~/$ cd radar_python_projects
example@user:~/radar_python_projects$ python -m venv venv
example@user:~/radar_python_projects$ source ./venv/bin/activate
(venv)example@user:~/radar_python_projects$ pip freeze > requirenments.txt
```
Далее необходимо проделать те же шаги, что и при запуске через обычный Python.

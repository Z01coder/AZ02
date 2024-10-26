# Задание: Исследование оценок учеников
# Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам.
# Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:
# 1. Самостоятельно создайте DataFrame с данными
# 2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
# 3. Вычислите среднюю оценку по каждому предмету
# 4. Вычислите медианную оценку по каждому предмету
# 5. Вычислите Q1 и Q3 для оценок по математике:
#       Q1_math = df['Математика'].quantile(0.25)
#       Q3_math = df['Математика'].quantile(0.75)
# 6. Можно также попробовать рассчитать IQR
# 7. Вычислите стандартное отклонение

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. DataFrame с данными
students = ['Святослав', 'Мирослава', 'Бронислав', 'Светлана', 'Ярослав',
            'Златослава', 'Вячеслав', 'Доброслава', 'Борислав', 'Любава']
subjects = ['Математика', 'Физика', 'Химия', 'История', 'Литература']
grades = np.random.randint(1, 6, size=(10, 5))  # Генерация случайных оценок от 1 до 5

df = pd.DataFrame(grades, columns=subjects, index=students)

# 2. Первые несколько строк DataFrame
print (df.head())

# 3. Вычисление средней оценки по каждому предмету
mean_grades = df.mean()

# 4. Вычисление медианной оценки по каждому предмету
median_grades = df.median()

# 5. Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)

# 6. Вычисление IQR
IQR = Q3_math - Q1_math

# 7. Вычисление стандартного отклонения по каждому предмету
std_deviation = df.std()

# Печать результатов
print("Средние оценки:")
print(mean_grades)

print("\nМедианные оценки:")
print(median_grades)

print("\nКвантили:")
print(f"Первый квантиль: {Q1_math}, третий квантиль: {Q3_math}")

print("\nМежквартильный размах (IQR):")
print(IQR)

print("Стандартное отклонение по каждому предмету:")
print(std_deviation)



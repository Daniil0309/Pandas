import pandas as pd
import numpy as np

data = {
    'Ученик': ['Ученик 1', 'Ученик 2', 'Ученик 3', 'Ученик 4', 'Ученик 5',
               'Ученик 6', 'Ученик 7', 'Ученик 8', 'Ученик 9', 'Ученик 10'],
    'Математика': [5, 4, 3, 5, 4, 3, 4, 5, 3, 4],
    'Физика': [4, 3, 4, 5, 3, 4, 4, 3, 5, 4],
    'Химия': [3, 4, 5, 4, 3, 4, 5, 4, 3, 4],
    'Биология': [5, 5, 4, 4, 3, 4, 5, 4, 3, 5],
    'Литература': [4, 3, 4, 4, 5, 4, 3, 4, 5, 4]
}

df = pd.DataFrame(data)
# Вывод первых нескольких строк DataFrame
print(df.head())

# Вычисление средней оценки по каждому предмету
mean_scores = df.mean(numeric_only=True)
print(mean_scores)
# Вычисление медианной оценки по каждому предмету
median_scores = df.median(numeric_only=True)
print(median_scores)

# Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(Q1_math, Q3_math, IQR_math)

# Вычисление стандартного отклонения по каждому предмету
std_deviation = df.std(numeric_only=True)
print(std_deviation)
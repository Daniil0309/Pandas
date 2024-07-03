import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# # Загружаем данные из CSV файла
#df = pd.read_csv("Dataset salary 2024.csv")
# # Считаем количество каждого типа занятости
# employment_counts = df['employment_type'].value_counts().sort_index()
# # Создаем новый столбец с типом занятости и количеством каждого типа
# df['employment_type_with_count'] = df['employment_type'].map(lambda x: f"{x}\n(N={employment_counts[x]})")
# # Устанавливаем размер фигуры
# plt.figure(figsize=(12, 8))
# # Используем seaborn для построения boxplot
# sns.boxplot(x='employment_type_with_count', y='salary_in_usd', data=df)
# # Добавляем заголовок и метки осей
# plt.title('Распределение заработной платы по видам занятости')
# plt.xlabel('Тип занятости')
# plt.ylabel('Заработная плата')
# # Поворачиваем метки по оси X для лучшей читаемости
# plt.xticks(rotation=45)
# # Показываем график
# plt.show()

# average_salary_by_job_title = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)
# top_10_job_title = average_salary_by_job_title.head(15)
# top_10_job_title = top_10_job_title.reset_index()
#
#
# plt.figure(figsize=(10, 6))
# sns.barplot(x='salary_in_usd', y='job_title', data=top_10_job_title, palette='viridis')
# plt.title('Топ-15 должностей по средней заработной плате')
# plt.xlabel('Средняя заработная плата')
# plt.ylabel('Должность')
# plt.show()
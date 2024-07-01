import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Временные ряды
# dates = pd.date_range(start = '2022-01-26', periods=10, freq='D') # Генерация дат
#
# values = np.random.rand(10) # Генерация случайных значений
#
# df = pd.DataFrame({'Date': dates, 'Value': values}) # Создание датафрейма
#
# df.set_index('Date', inplace=True) # Установка даты в качестве индекса
#
# print(df)
# month = df.resample('M').mean() # Группировка данных по месяцам и расчет средней зарплаты
#
# print(month)


# #Обработка выбросов
# data = {'value':[1,2,2,2,3,3,3,4,4,4,4,5,6,7,8,9,10,55]} # Создание датафрейма
# df = pd.DataFrame(data)
#
# df.boxplot(column='value') # Построение графика
# plt.show()
#
# q1 = df['value'].quantile(0.25) # Вычисление первого квартиля
# q3 = df['value'].quantile(0.75) # Вычисление третьего квартиля
# iqr = q3 - q1 # Вычисление размаха
#
#
# downside = q1 - 1.5*iqr # Нижняя граница
# upside = q3 + 1.5*iqr # Верхняя граница
#
# df_new = df[(df['value'] >= downside) & (df['value'] <= upside)] # Удаление выбросов
#
# df_new.boxplot(column='value') # Построение графика
# plt.show()

#Категориальные данные
# data = {
#     'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'gender': ['female', 'male', 'male', 'male', 'female'],
#     'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
# }
# df = pd.DataFrame(data)
#
# df['gender'] = df['gender'].astype('category') # Преобразование в категориальные данные
# df['department'] = df['department'].astype('category') # Преобразование в категориальные данные
#
# #print(df['gender'].cat.categories) # Вывод категорий
# #print(df['gender'].cat.codes) # Кодировка категорий
#
# df['department'] = df['department'].cat.add_categories(['IT']) # Добавление категорий
# df['department'] = df['department'].cat.remove_categories(['HR'])# Удаление категорий
#
# print(df)








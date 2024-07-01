import pandas as pd

df = pd.read_csv("dz.csv")

df = df.dropna(subset=['City', 'Salary']) # Удалим строки, где значение в столбце City или Salary отсутствует

average_salary_by_city = df.groupby('City')['Salary'].mean() # Группировка данных по городу и расчет средней зарплаты

print(average_salary_by_city)
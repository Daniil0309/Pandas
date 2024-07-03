from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt
import re

# Настройка веб-драйвера
driver = webdriver.Firefox()  # Убедитесь, что chromedriver установлен и находится в PATH

# Открытие сайта
driver.get('https://www.divan.ru/category/divany-i-kresla')

# Найдем элемент с диванами на сайте (необходима корректировка под актуальную структуру сайта)
sofas = driver.find_elements(By.CLASS_NAME, 'lsooF')

# Сбор данных о диванах
data = []
for sofa in sofas:
    name = sofa.find_element(By.CLASS_NAME, "ui-GPFV8").text
    price = sofa.find_element(By.CLASS_NAME, "ui-LD-ZU").text
    # Убираем пробелы и приведение цены к числовому типу
    price = re.sub(r'\D', '', price)  # Удаляем все, кроме цифр
    if price:  # Проверка, что после очистки цена не пустая
        price = int(price)
        data.append([name, price])

# Закрытие драйвера
driver.quit()

# Создание DataFrame и сохранение в CSV
df = pd.DataFrame(data, columns=['Name', 'Price'])
df.to_csv('divan.csv', index=False)

# Чтение данных из CSV файла
df = pd.read_csv('divan.csv')

# Вычисление средней цены
average_price = df['Price'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} ₽')

# Построение гистограммы цен
plt.hist(df['Price'], bins=20, edgecolor='black')
plt.title('Распределение цен на диваны')
plt.xlabel('Цена, ₽')
plt.ylabel('Количество диванов')
plt.show()



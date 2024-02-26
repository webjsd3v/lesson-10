import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных из файла JSON в DataFrame
df = pd.read_json('events.json')

# Извлечение значения столбца 'signature' из столбца 'events'
df['signature'] = df['events'].apply(lambda x: x['signature'])

# Просмотр первых нескольких строк DataFrame с добавленным столбцом 'signature'
print(df.head())

# Удаление столбца 'events', так как мы уже извлекли нужную информацию
df.drop(columns=['events'], inplace=True)

# Построение графика распределения типов событий информационной безопасности
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='signature')
plt.xticks(rotation=90)
plt.xlabel('Типы событий информационной безопасности')
plt.ylabel('Количество событий')
plt.title('Распределение типов событий информационной безопасности')
plt.show()

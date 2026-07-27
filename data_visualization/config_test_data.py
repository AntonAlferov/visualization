import pandas as pd

# читаю файлы по ссылке в интернете
white = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
red = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
white_wine = pd.read_csv(white, sep=';')
red_wine = pd.read_csv(red, sep=';')

# сохраняю тип вина как атрибут
red_wine['wine_type'] = 'red'
white_wine['wine_type'] = 'white'

# делаю оценку качества вина менее гранулярной
red_wine['quality_label'] = red_wine['quality'].apply(lambda value: 'low'
                                                      if value <= 5 else 'medium'
                                                      if value <= 7 else 'high')
red_wine['quality_label'] = pd.Categorical(red_wine['quality_label'],
                                           categories=['low', 'medium', 'high'])
white_wine['quality_label'] = white_wine['quality'].apply(lambda value: 'low'
                                                          if value <= 5 else 'medium'
                                                          if value <= 7 else 'high')
white_wine['quality_label'] = pd.Categorical(white_wine['quality_label'],
                                             categories=['low', 'medium', 'high'])

# Соединяю наборы данных по красному и белому вину
wines = pd.concat([red_wine, white_wine])

# Перемешаю данные
wines = wines.sample(frac=1, random_state=42).reset_index(drop=True)

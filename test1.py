"""
Задача: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1
столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head())
data1 = data['whoAmI'].unique()
data2 = pd.DataFrame({d: lst for d in data1})
for c in data2.columns:
    for i, row in data2.iterrows():
        if row[c] == c:
            row[c] = 1
        else:
            row[c] = 0
print(data2)

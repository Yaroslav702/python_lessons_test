import pandas as pd
import numpy as np
# from googletrans import Translator

# translator = Translator()

# text = pd.read_excel('lessons/semester II/lesson2/Grades.xlsx')

# a = translator.translate(text=text, src='en', dest='uk')
# print(a.text)

products = ['Water', 'Milk', 'Melon', 'Apples']
price = [15, 50, 200, np.nan]
data = pd.DataFrame(list(zip(products, price)), columns=['Products', 'Price'])
# data.to_excel('lessons/semester II/lesson2/groceries.xlsx', index=None)

with pd.ExcelWriter('lessons/semester II/lesson2/groceries.xlsx') as writer:
    data.to_excel(writer, sheet_name='groceries1', index=None)
    data.to_excel(writer, sheet_name='groceries2')
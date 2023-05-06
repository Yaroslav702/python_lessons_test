import pandas as pd
data = pd.read_excel('Grades.xlsx', usecols=['Subject', 'Grade'])
print(data)
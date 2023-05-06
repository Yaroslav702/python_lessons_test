# try:
#     raise AttributeError('test exception')
# except Exception as e:
#     print(f'Exception has occurred --- {str(e)}')



# print('Next code')

# print(len('My name is Yaroslav'))

# file = open('lessons/semester II/lesson 1/my_name.txt', 'w')

# with open('lessons/semester II/lesson 1/my_name.txt', 'w', encoding='utf-8') as file:

#     file.write('Мене звуть Ярослав')
# # file.close()


# file = open('lessons/semester II/lesson 1/my_name.txt', 'a')
# file.write('\n\nI am 16.')
# file.close()



# file = open('lessons/semester II/lesson 1/my_name.txt', 'r')
# # info = file.read(-1)
# # print(repr(info))
# # print(info)

# print(file.readlines()[::-1])

# info = file.readlines()

# file.close()



# file = open('lessons/semester II/lesson 1/grades.csv', 'r')
# print(file.read())
# file.close()

# file = open('lessons/semester II/lesson 1/grades.csv', 'a')
# file.write('\n№5, 6, 7, 8')
# file.close()


file = open('semester II/lesson 1/grades.csv', 'r')
result = []
for line in file:
    arr = line.split(',')
    result.append(arr)

sum_of_grades = sum(map(int, result[6][1:]))
print(sum_of_grades)


# sixth_student = result[6]
# list_of_grades = sixth_student[1:]
# b = [int(i) for i in list_of_grades]
# print(list_of_grades)
# print(b)
# print(sum(b))

file.close()

# with open('semester II/lesson 1/grades.csv', 'r+', encoding='utf-8') as file:
#     a = file.read()
#     a = a.replace('"', '')
#     file.write(a)



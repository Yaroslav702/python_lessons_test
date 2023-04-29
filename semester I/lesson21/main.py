# file = open('lessons/lesson21/seek.txt')
# file.seek(2)
# print(file.read(1))
# file.close()

# file = open('lessons/lesson21/seek.txt')

# try:
#     print(file.read(3))
# finally:
#     print('The end of the statement')
#     file.close()

# try:
#     file.open('lessons/lesson21/seek.txt')
# except Exception as e:
#     print('An error has occurred:', str(e))



# print('Some next code')


# with open('lessons/lesson21/seek.txt') as file:
#     file.seek(2)
#     print(file.read(1))

# bytes = b'Hello'
# print(bytes[1])

# bytes_str_utf16 = 'Hello World!'.encode(encoding='utf-16')
# bytes_str_utf8 = 'Hello World'.encode()

# print(list(bytes_str_utf16))
# print(list(bytes_str_utf8))

# print(list(bytes_str))
# Capital_h = b'H'
# lower_h = b'h'

# print(list(Capital_h))
# print(list(lower_h))

# numbers = [0, 128, 255]
# bytes_numbers = bytes(numbers)

# for i in numbers:
#     print(hex(i))

# symbol = 'a'

# print(ord(symbol))

# symbol_bytes = 97
# print(chr(symbol_bytes))


# check = ['🐔', '🥚']
# check.sort()

# print(check)


# a = '🐔'.encode()
# b = '🥚'.encode()


# print(a > b)


# .bin

# with open('lessons/lesson21/data.bin', 'wb') as file:
#     file.write(b'Hello World!2')
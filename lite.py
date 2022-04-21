# task 1 ----------------------------
print('-' * 5, 'Задача №1', '-' * 5)

stroke = ''
for i in range(4):
    stroke += '0'

for i in range(4):
    print(i, stroke)


# task 2 ----------------------------
print()
print('-' * 5, 'Задача №2', '-' * 5)

print('Введите 10 произвольных цифр')
count = 1
all_digit = []
while count < 11:
    one_digit = int(input('введите ' + str(count) + 'ую цифру: '))
    if one_digit >= 10 or one_digit < 0:
        print('Вы ввели число, а НЕ ЦИФРУ!')
        continue
    count += 1
    all_digit = all_digit + [one_digit]

count = 0
for i in all_digit:
    if i == 5:
        count += 1
print('Всего введено', count, ' цифр 5')


# task 3 ----------------------------
print()
print('-' * 5, 'Задача №3', '-' * 5)

summa = 0
for i in range(50):
    summa += 101
print('Сумма чисел от 1 до 100 равна', summa)

# summa = 0
# for i in range(1, 101):
#     summa += i
# print('Сумма чисел от 1 до 100 равна', summa)


# task 4 ----------------------------
print()
print('-' * 5, 'Задача №4', '-' * 5)

product = 1
number_init = 10
number = number_init
while number > 0:
    product *= number
    number -= 1
print('Факториал ' + str(number_init) + '! равен', product)


# task 5 ----------------------------
print()
print('-' * 5, 'Задача №5', '-' * 5)

number = 123567
number = str(number)
for one_char in number:
    print(one_char)

# end of Lite version ---------------

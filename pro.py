# task 6 ----------------------------
print()
print('-' * 5, 'Задача №6', '-' * 5)

number = 254314
number = str(number)

summa = 0
for digit in number:
    summa += int(digit)

stroke = 'Сумма цифр числа - ' + str(summa) + '('
count = 0
for digit in number:
    count += 1
    if count != len(number):
        stroke += digit + '+'
    else:
        stroke += digit

stroke += ')'
print(stroke)


# task 7 ----------------------------
print()
print('-' * 5, 'Задача №7', '-' * 5)

number = 254314
number = str(number)

product = 1
for digit in number:
    product *= int(digit)

stroke = 'Произведение цифр числа - ' + str(product) + '('
count = 0
for digit in number:
    count += 1
    if count != len(number):
        stroke += digit + '*'
    else:
        stroke += digit

stroke += ')'
print(stroke)


# task 8 ----------------------------
print()
print('-' * 5, 'Задача №8', '-' * 5)

number = int(input('Введите произвольное число: '))
number = str(number)
seek_res = False
for digit in number:
    if digit == '5':
        seek_res = True
        break
if seek_res:
    print('Цифра 5 есть в числе')
else:
    print('Цифры 5 нет в числе')


# task 9 ----------------------------
print()
print('-' * 5, 'Задача №9', '-' * 5)

number = 354359688
number = str(number)
maxi = int(number[0])
for digit in number:
    if  maxi < int(digit):
        maxi = int(digit)
print('Цифра - ' + str(maxi) + ' максимальная в числе ' + number)


# task 10 ---------------------------
print()
print('-' * 5, 'Задача №10', '-' * 4)

number = 543231235643
number = str(number)
seek_res = 0
for digit in number:
    if digit == '5':
        seek_res += 1
print('В числе', seek_res, '5-ки')

# end of Pro version ---------------

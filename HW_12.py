str = input('Введите пожалуйста строку: ')
symb = input('Введите пожалуйста искомый символ: ')
search = -1
quant = 0
while True:
    search = str.find(symb, search + 1)
    if search == -1:
        break
    quant += 1
    if quant == 1:
        print('\nИндекс указанного символа: ', end=" ")
    print(search, end=" ")
if quant == 0:
    print('\nИскомый символ в строке не найден')
print()
if quant > 0:
    print("\nКоличество раз вхождений указанного символа: ", quant)

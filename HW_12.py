str = input('Введите пожалуйста строку: ')
symb = input('Введите пожалуйста искомый символ: ')
index = -1
quant = 0
for new_str in str:
    index += 1
    search = new_str.find(symb)
    if search != -1:
        quant += 1
        if quant == 1:
            print('Индекс указанного символа: ', end=" ")
    if search != -1:
        print(index, end=" ")
if quant > 0:
    print("\nКоличество раз вхождений указанного символа: ", quant)

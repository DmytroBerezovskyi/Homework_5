str = input('Введите пожалуйста строку: ')
n = len(str)                            # Определение количества элементов в строке
quant = str.find('h')                   # Находит индекс первого заданого элемента
if quant == -1:                         # В случае если индекс не найден выводим строку без измений
    print(str)
else:
    quant_r = str.rfind('h')            # Находим последний индекс заданого элемента
    if quant_r == quant:                # В случае если вхождение только одно выводим строку без измений
        print(str)
    else:
        new_str = str[quant+1:quant_r]  # Формирование новой строки (с помощью среза без первого и последнего вхождения)
        str_repl = new_str.replace('h', 'H')                   # Замена букв в строке
        print(str[0:quant+1]+str_repl+str[quant_r:n])          # Вывод строки с изменными буквами
str = input('Введите пожалуйста строку: ')
print('a.', str[2])         # вывод третего символа этой строки
print('b.', str[-2])        # вывед предпоследнего символа этой строки
print('c.', str[0:4])       # вывод первых пять символов этой строки
print('d.', str[:-2])       # вывод всей строки, кроме последних двух символов
print('e.', str[::2])       # вывод всех символов с четными индексами
print('f.', str[1::2])      # вывод всех символов с нечетными индексами, то есть начиная со второго символа строки
print('g.', str[::-1])      # вывод всех символов в обратном порядке
print('h.', str[-1::-2])    # вывод всех символов строки через один в обратном порядке, начиная с последнего
print('i.', len(str))       # вывод длины данной строки
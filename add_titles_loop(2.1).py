                   # создаём пустой список и в цикле добовляем переменную для добовления в список

lists = []

while True:
    i = input('Введите название заголовка: ')                  # добовляем в цикле завершение программы при пустом вводе
    if i == '':
        print('Вы ввели пустое значение попробуйте еще раз')
    lists.append(i)
    a = input('Желаете продолжить?(да/нет) (Enter - выход):')
    if a != 'да' or a == 'нет' :                               # добовляем условия для продолжения\завершения цикла
        break
print('Вы ввели: ' , (len(set(lists))),'заголовка')                        # проверяем на уникальность и количество
print('Ваши заголовки: ','\n',                                             # введённых заголовков, выводим результат
str(set(lists)).replace(',','\n',))                            # выводим список на экран, проверяем на


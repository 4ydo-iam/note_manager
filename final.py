
# Собираем данные пользователя
name = input('Введите имя пользователя: ')
title = input('Введите содержание заметки: ')
content = input('Введите описание заметки: ')
created_date = input('Введите дату создания в формате 12.12.2024: ')
issue_date = input('Введите дату окончания в формате 12.12.2024: ')

# Создаём словарь загаловков
title1 = input('Введите описание главы1: ')
title2 = input('Введите описание главы2: ')
title3 = input('Введите описание главы3: ')
# создаём общий словарь с созданием вложенного славоря
dictionary = {
    'blok1':{
        'имя' : name,
        'содержание' : content,
        'дата создания' : created_date[:5],
        'дата окончания' : issue_date[:5]},
    'blok2':{
        'описание главы1' : title1,
        'описание главы2' : title2,
        'описание главы3' : title3}}

# Выводим всё на экран
print('Вы ввели имя пользователя: ',name)
print('Описание Вашей заметки: ',content)
print('Дата создания: ',created_date[:5])
print('Дата завершения:',issue_date[:5])
final = dictionary['blok2']['описание главы1']
print('Описание вашей главы :',final)
a = dictionary['blok1']['имя']
a1 = dictionary['blok1']['содержание']
a2 = dictionary['blok1']['дата создания']
a3 = dictionary['blok1']['дата окончания']
a4 = dictionary['blok2']['описание главы1']
a5 = dictionary['blok2']['описание главы2']
a6 = dictionary['blok2']['описание главы3']
print(a,a1,a2,a3,a4,a5,a6)

# собираем информацию у пользователя и добовляем в список
note = [
name := input('Ввидите имя пользователя: '),
title := input('Ввидите загаловок заметки: '),
content := input('Введите содержание заметки: '),
created_date := input('Введите дату создания заметки (в формате - число.месяц.год): '),
issue_date := input('Ввидите дату оканчания заметки (в формате - число.месяц.год): '),

#  создаём заголовки
[titl1 := input('Ввидите подзаголовок 1: '),
title2 := input('Введите подзаголовок 2: '),
title3 := input('Введите подзаголовок 3: ')]
]
# выводим на экран
print('Вы ввели данные:')
print('Имя: ',name)
print('Заголовок: ',title)
print('Содержание: ',content)
print('Дата создания',created_date[:5])
print('Дата окончания: ',issue_date[:5])
print('Подзаголовок: ',note[5][1])

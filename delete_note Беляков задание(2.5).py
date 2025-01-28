from datetime import datetime

time_now = datetime.now().date()
time_print = datetime.strftime(time_now,'%d.%m.%Y')

note = [{'имя' : 'Алексей','название' : 'Список покупок',             # список словарей по умолчанию
         'описание' : 'Купить продукты на неделю',
         'deadline' : 'Заметка закончится через 60 дней'},
        {'имя' : 'Мария','название' : 'Учёба',
         'описание' : 'Подготовиться к экзамену',
         'deadline' : 'Заметка закончится сегодня'}
        ]
my_list = {}

def del_notes():
    while True:                                                          # создаём функцию для удаления
        del_notes = input('Желаете удалить заметку?(да/нет): ').lower()  # с помощью функции .lower
        if del_notes == 'нет':                                           # делаем ввод не чувствительным к регистру
            print('Отлично! Всего доброго!')
            break
        if del_notes != 'да':
            print('Ошибка! Не верный ввод используйте (да/нет)')
            continue
        if del_notes == 'да':
            print('\nПриступим!')
            shou_notes()
            del_notes_input = input('Ведите имя пользователя или название заметки для удаления: ')
            for my_list in note:
                if my_list['имя'] == del_notes_input or my_list['название'] == del_notes_input:
                    ask = input('Заметка найдена! Вы уверены в удалении?(да/нет): ')
                    if ask == 'да':
                        note.remove(my_list)
                        print('Заметка удалена!')
                        break
                    elif ask == 'нет':
                        print('хорошо')
                        break
                    else:
                        print('Ошибка! Используйте только (да/нет)')
                        continue
                else:
                    print('Заметка не найдена!')
                    continue

def shou_notes():
    print('\nВаши заметки:')                              # создаём функцию для финальной печати всего списка заметок
    for my_list in note:
        print('-' * 40)
        print(f'Имя: {my_list['имя']}')
        print(f'Название заметки: {my_list['название']}')
        print(f'Описание заметки: {my_list['описание']}')
        print(f'Время истечения: {my_list['deadline']}')

print('Приветствую в менеджере заметок!')
print(f'     Сегодня: {time_print}')
while True:                                         # основной цикл для создания заметок
    new_titles = input('Желаете создать новую заметку?(да/нет): ').lower()
    if new_titles == 'нет':
        print('Отлично!')
        break
    elif new_titles == 'да':
        print('Отлично приступим!')
    else:
        print('Ошибка! Используйте только (да/нет).')
        continue

    while True:                             # вложенный цикл для имени пользователя
        name_input = input('Введите Имя пользователя: ')
        if name_input == '':
            print('Ошибка! Имя пользователя не может быть пустым!')
            continue

        while True:                         # вложенный цикл для создания заметки и описания
            title_input = input('Введите название заметки: ').lower()
            description_input = input('Введите описание заметки: ').lower()
            if title_input == '' or description_input == '':
                print('Ошибка! "название" и "опиcание" не могут быть пустыми!')
                continue

            while True:                             # вложенный цикл для работы со временим
                try:
                    time_input = input('Введите дату окончания заметки в формате(дд.мм.гггг): ')
                    data_new = datetime.strptime(time_input,'%d.%m.%Y').date()
                    data_check = (data_new - time_now).days
                except ValueError:
                    print('Ошибка! Не верны формат даты! Введите в формате (дд.мм.гггг)')
                    continue
                if data_check == 0:
                    deadline = 'Заметка закончится сегодня!'
                    break
                if data_check > 0:
                    deadline = f'Заметка закончится через {data_check} дней'
                    break
                if data_check < 0:
                    print('Ошибка! Дата окончания не может быть меньше текущей!')
                    continue
            my_list = {'имя': name_input, 'название': title_input, 'описание': description_input, 'deadline': deadline}
            note.append(my_list)  # добавляем словарь в список
            break
        break
del_notes()          # вызываем функцию удаления заметок
shou_notes()         # вызываем функцию демонстрации заметок
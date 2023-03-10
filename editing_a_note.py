import json
from datetime import datetime


def print_menu_editing_note():

    print()
    print("Что Вы собираетесь редактировать: ")
    print()
    print("notename - имя заметки")
    print("notebody - тело заметки")
    print()


def editing_note():

    editing = input("Что Вы выбрали: ").lower()
    print()

    with open('Заметки.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    if editing == 'notename':
        try:
            note_id = int(input("Введите id заметки: "))
            print()
            print('Меняем имя заметки\n')
            for text in data['zametki']:
                if text['id'] == note_id:
                    new_note = input('Введите новое имя заметки: ')
                    print()
                    text['Заголовок'] = new_note
                    text['Дата'] = datetime.now().strftime(
                        '%Y-%m-%d  %H:%M:%S')
                    print("Имя заметки успешно изменено. \n")
        except ValueError:
            print("ERROR!")
            print("Убедитесь в правильности ввода id заметки\n")
            editing_note()

    elif editing == 'notebody':
        note_id = int(input("Введите id заметки: "))
        print()
        print('Меняем тело заметки\n')
        for text in data['zametki']:
            if text['id'] == note_id:
                new_note = input('Введите новое тело заметки: ')
                print()
                text['Тело_заметки'] = new_note
                text['Дата'] = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
                print("Тело заметки успешно изменено. \n")

    else:
        print("Проверьте правильность ввода команды\n")
        editing_note()

    with open('Заметки.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

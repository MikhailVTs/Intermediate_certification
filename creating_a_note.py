import json
from datetime import datetime


def creatin_note():

    print()

    data_time = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
    heading = input("Введите заголовок: ")
    note_body = input("Введите тело заметки: ")

    new_data = {"zametki": [{'id': 1, 'Дата': data_time,
                             'Заголовок': heading, 'Тело_заметки': note_body}]}

    with open("Заметки.json", 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)

    print()
    print('Заметка успешно сохранена')
    print()

import json
from datetime import datetime


def add_note():
    try:
        print()
        add_data = {}

        with open('Заметки.json', 'r', encoding='utf-8') as f:
            text = json.load(f)

        for txt in text['zametki']:
            index = int(txt['id'])

        add_data['id'] = index + 1
        add_data['Дата'] = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
        add_data['Заголовок'] = input("Введите заголовок: ")
        add_data['Тело_заметки'] = input("Введите тело заметки: ")

        with open("Заметки.json", encoding='utf-8') as f:
            data = json.load(f)
            data["zametki"].append(add_data)
            with open("Заметки.json", 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=3)
        print()
        print("Заметка добавлена")
        print()
    except FileNotFoundError:
        print()
        print("Error !!!")
        print("Необходимо для начала, создать заметку")
        print()

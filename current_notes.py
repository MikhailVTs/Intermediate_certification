import json
from datetime import datetime


def current_note():
    print()

    with open('Заметки.json', 'r', encoding='utf-8') as f:
        text = json.load(f)

    for row in sorted(text['zametki'], key=lambda x: datetime.strptime(x['Дата'], '%Y-%m-%d  %H:%M:%S')):

        try:
            print(
                f"id - {row['id']}; Дата/время - {row['Дата']}; Заголовок - {row['Заголовок']}; Тело-заметки - {row['Тело_заметки']}")
        except:
            print("Error!!!")

    print()

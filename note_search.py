import json


def note_find():
    print()

    with open('Заметки.json', 'r', encoding='utf-8') as f:
        text = json.load(f)

        try:
            id_note = int(
                input("Укажите id заметки, которую необходимо вывести: "))

            for key in text['zametki']:

                if key['id'] == id_note:

                    index = int(key['id'])
                    data_time = key['Дата']
                    heading = key['Заголовок']
                    note_body = key['Тело_заметки']
                    note = f'id - {index}; Дата/время - {data_time}; Заголовок - {heading}; Тело заметки - {note_body}'
                    break

                else:
                    note = "Нет записи"

            print()
            print(note)

        except ValueError:
            print()
            print("ERROR!!!")
            print("Будьте внимательней при вводе id")
            note_find()

    print()

from creating_a_note import creatin_note
from add_a_note import add_note
from deleting_a_note import deleting_note
from current_notes import current_note
from editing_a_note import editing_note, print_menu_editing_note
from note_search import note_find


def print_menu():

    print()
    print("#############################")
    print("# 1 - Создать заметку       #")
    print("# 2 - Добавить заметку      #")
    print("# 3 - Редактировать заметку #")
    print("# 4 - Удалить заметку       #")
    print("# 5 - Текущие заметки       #")
    print("# 6 - Поиск заметки         #")
    print("# 0 - Выход                 #")
    print("#############################")
    print()


def choosing_an_action():

    try:

        option = int(input("Введите команду: "))

        while option != 0:
            if option == 1:
                creatin_note()
            elif option == 2:
                add_note()
            elif option == 3:
                print_menu_editing_note()
                editing_note()
            elif option == 4:
                deleting_note()
            elif option == 5:
                current_note()
            elif option == 6:
                note_find()
            else:
                print()
                print("Ошибка !!!")
                print("Введите верную команду!")
                print()

            option = int(input("Введите команду: "))

    except ValueError:

        print()
        print("ERROR !!!")
        print()
        choosing_an_action()

    print("Вы вышли из программы!!!")
    print("________________________")

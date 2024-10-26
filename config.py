#  Основные настройки
#  Импорт библиотек
import os

#  Корневая директория проекта
ROOT_DIR = os.path.dirname(__file__)

#  Путь до готового файла
PATH_TO_FILE = os.path.join(ROOT_DIR, "html", "contacts.html")


if __name__ == "__main__":
    print(ROOT_DIR)
    print()
    print(PATH_TO_FILE)

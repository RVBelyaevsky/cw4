from src.json_saver import JSONSaver
from src.utils import user_connector


def main():
    top = user_connector()
    json_saver = JSONSaver('data/data.json')

    user_choice = input("Для сохранения файла введите 'yes', для вывода в консоль введите 'ENTER': ").lower()
    if user_choice == 'yes':
        json_saver.add_vacancy(top)
    else:
        for i in top:
            print(i)

if __name__ == "__main__":
    main()

import argparse
import re

def parse_arguments():
    """Получаем имя файла, который был передан в качестве строки."""
    parser = argparse.ArgumentParser(description="Find people living in Moscow.")
    parser.add_argument('filename', type=str, help='Name of the file to read')
    return parser.parse_args()

def read_file(filename):
    """открываем файл"""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def find_people_in_moscow(data):
    """ищем анкеты, которые подходят под наши условия"""
    pattern = r'Фамилия: (.+?)\nИмя: (.+?)\nПол: (.+?)\nДата рождения: (.+?)\nНомер телефона: (.+?)\nГород: Москва'
    matches = re.findall(pattern, data)
    return matches

def print_results(people):
    """Выводим результат"""
    for surname, name, gender, birth_date, phone in people:
        print(f"Фамилия: {surname}\n Имя: {name}\n Пол: {gender}\n Дата рождения: {birth_date}\n Номер телефона: {phone}\n")

def main():
    args = parse_arguments()
    try:
        data = read_file(args.filename)
        people_in_moscow = find_people_in_moscow(data)
        print_results(people_in_moscow)
    except FileNotFoundError:
        print(f"Файл {args.filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()

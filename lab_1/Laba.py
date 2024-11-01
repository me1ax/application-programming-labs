import argparse
import re

def get_filename() -> str:
    """
    Получаем имя файлы, который был передан в качестве строки.

    Returns:
        str: Имя файла.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='your name file')
    args = parser.parse_args()
    return args.filename

def read_filename(filename: str) -> str:

    """"открываем файл"""

    with open(filename, "r", encoding="UTF-8") as file:
        text = file.read()
    return text

def live_in_Moscow(text: str) -> list[str]:

    """ищем анкеты, которые подходят под наши условия"""

    pattern = r'\d+\)\n'
    anketa = re.split(pattern, text, maxsplit=0)
    result = []
    for question in anketa:
        if "Москва" in question:
            result.append(question)
        else:
            continue
    return result
    
def print_live_in_Moscow(text_sort: list[str]) -> None:
    """вывожу анкеты"""
    for question in text_sort:
        print(question)
    return None

def main():
    filename = get_filename()
    text = read_filename(filename)

    print_live_in_Moscow(live_in_Moscow(text))

if __name__ == "__main__":
    main()

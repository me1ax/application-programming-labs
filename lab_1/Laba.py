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

    pattern =  r"\bМосква\b"
    return len(re.findall(pattern, text))

if __name__ == "__main__":
    filename = get_filename()
    text = read_filename(filename)
    print(f"Количество людей, которые проживают в Москве: {live_in_Moscow(text)}")
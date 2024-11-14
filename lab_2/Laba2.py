import os
import csv
import argparse
from icrawler import ImageDownloader
from icrawler.builtin import GoogleImageCrawler

def download_images(keyword, save_dir, num_images):
    # Создание директории для сохранения изображений
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Инициализация загрузчика
    crawler = GoogleImageCrawler(storage={'root_dir': save_dir})
    crawler.crawl(keyword=keyword, max_num=num_images)

def create_annotation_csv(save_dir, csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['absolute_path', 'relative_path'])

        # Проходим по всем файлам в директории и записываем пути в файл
        for root, dirs, files in os.walk(save_dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                relative_path = os.path.relpath(file_path, save_dir)
                writer.writerow([file_path, relative_path])

class ImageIterator:
    def __init__(self, annotation_file):
        self.annotation_file = annotation_file
        self.images = self.load_images()

    def load_images(self):
        images = []
        with open(self.annotation_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Пропустить заголовок
            for row in reader:
                images.append(row[0])  # Добавляем только абсолютный путь
        return images

    def __iter__(self):
        return iter(self.images)

def main():
    parser = argparse.ArgumentParser(description='Download images and create an annotation CSV file.')
    parser.add_argument('keyword', type=str, help='The keyword to search for images.')
    parser.add_argument('save_dir', type=str, help='Directory to save downloaded images.')
    parser.add_argument('csv_file', type=str, help='Path to the output CSV file for annotation.')
    parser.add_argument('--num_images', type=int, default=100, help='Number of images to download (50-1000).')

    args = parser.parse_args()

    if args.num_images < 50 or args.num_images > 1000:
        raise ValueError("Number of images must be between 50 and 1000.")

    # Загрузка изображений
    download_images(args.keyword, args.save_dir, args.num_images)

    # Создание аннотации
    create_annotation_csv(args.save_dir, args.csv_file)

    # Создание итератора
    image_iterator = ImageIterator(args.csv_file)
    for image_path in image_iterator:
        print(image_path)

if __name__ == "__main__":
    main()
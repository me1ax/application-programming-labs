import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

def read_image(input_image_path):
    image = cv2.imread(input_image_path)
    if image is None:
        raise FileNotFoundError(f"Ошибка: изображение не найдено по пути: {input_image_path}")
    return image

def print_image_size(image):
    print(f"Размер изображения: {image.shape[1]}x{image.shape[0]} (ширина x высота)")

def plot_histogram(image):
    color = ('b', 'g', 'r')
    plt.figure(figsize=(12, 6))

    for i, col in enumerate(color):
        histogram, bins = np.histogram(image[:, :, i], bins=256, range=(0, 256))
        plt.plot(bins[:-1], histogram, color=col)
        plt.xlim([0, 256])

    plt.title('Гистограмма цветного изображения')
    plt.xlabel('Яркость')
    plt.ylabel('Количество пикселей')
    plt.legend(['Синий', 'Зеленый', 'Красный'])
    plt.grid()
    plt.show()

def convert_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def display_images(original_image, gray_image):
    plt.figure(figsize=(12, 6))

    # Исходное изображение
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title('Исходное изображение')
    plt.axis('off')

    # Изображение в полутоновом
    plt.subplot(1, 2, 2)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Полутоновое изображение')
    plt.axis('off')

    plt.show()

def save_image(output_image_path, gray_image):
    cv2.imwrite(output_image_path, gray_image)
    print(f"Полутоновое изображение сохранено в: {output_image_path}")

def main(input_image_path, output_image_path):
    try:
        image = read_image(input_image_path)
        print_image_size(image)
        plot_histogram(image)
        gray_image = convert_to_gray(image)
        display_images(image, gray_image)
        save_image(output_image_path, gray_image)
    except FileNotFoundError as e:
        print(e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Обработка изображений.')
    parser.add_argument('input_image_path', type=str, help='Путь к входному изображению.')
    parser.add_argument('output_image_path', type=str, help='Путь для сохранения результата.')

    args = parser.parse_args()

    # Проверка на существование входного файла
    if not os.path.exists(args.input_image_path):
        print(f"Ошибка: файл не найден по пути: {args.input_image_path}")
    else:
        main(args.input_image_path, args.output_image_path)
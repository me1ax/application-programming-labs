import cv2
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

def create_dataframe(image_paths):
    data = []

    for path in image_paths:
        img = cv2.imread(path)
        if img is not None:
            height, width, depth = img.shape
            data.append([path, os.path.abspath(path), height, width, depth])
        else:
            print(f"Error loading image: {path}")

    df = pd.DataFrame(data, columns=["File Name", "Absolute Path", "Height", "Width", "Depth"])
    return df

def filter_dataframe(df, max_height, max_width):
    filtered_df = df[(df["Height"] <= max_height) & (df["Width"] <= max_width)]
    return filtered_df

def main(image_folder, max_height, max_width):
    image_paths = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('jpg', 'jpeg', 'png'))]

    df = create_dataframe(image_paths)

    # Рассчитать статистику по размеру изображения
    print(df[["Height", "Width", "Depth"]].describe())

    # Добавить столбец области
    df['Area'] = df['Height'] * df['Width']

    # Сортировка по площади
    df.sort_values(by="Area", inplace=True)

    # Фильтровать DataFrame
    filtered_df = filter_dataframe(df, max_height, max_width)

    # Гистограмма
    plt.figure(figsize=(10, 6))
    plt.hist(df['Area'], bins=20, edgecolor='black')
    plt.title("Распределение площадей изображений")
    plt.xlabel("Площадь изображения (пиксели)")
    plt.ylabel("Количество изображений")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <image_folder> <max_height> <max_width>")
        sys.exit(1)

    image_folder = sys.argv[1]
    max_height = int(sys.argv[2])
    max_width = int(sys.argv[3])

    main(image_folder, max_height, max_width)
from PIL import Image, ImageFilter
from random import randint
import numpy as np


# метод изменяющий изображение
def image_transform(file):
    with Image.open(file) as im:
        str1 = file.split('.')
        print(f'На обработку принято изображение со следующими характеристиками\n'
              f'Формат: {im.format}\nРазмер: {im.size}\nЦветовая палитра: {im.mode}\n')
        # конвертируем изображение
        image = im.convert('RGB')
        # создаем новый слой розового цвета
        pink_layer = Image.new('RGB', image.size, (242, 13, 194))
        # накладываем новый слой
        blend_image = Image.blend(image, pink_layer, alpha=0.15)
        # обрезаем по карям
        image_crop = blend_image.crop((43, 42, 810, 956))
        # накладываем фильтр bluer
        image_filter = image_crop.filter(ImageFilter.GaussianBlur(1.4))
        # меняем раземер картинки
        resize_image = image_filter.resize((im.width - 200, im.height - 200))
        # сохраняем картинку в другом формате
        resize_image.save(str1[0] + str(randint(1, 100)) + '.jpg')
        print(f'Изображение обработано, вот его новые характеристики\n'
              f'Формат: {resize_image.format}\nРазмер: {resize_image.size}\nЦветовая палитра: {resize_image.mode}\n')


def numpy_array():
    # создаем массив
    a = np.random.randint(0, 100, 15)
    # сортируем массив
    a.sort()
    # выводим массив
    print(a)
    # выводим сумму элементов массив
    print(f'сумма элементов массива- {a.sum()}')
    # изменяем массив на двумерный 5х3
    b = a.reshape(5, 3)
    # выводим новый массив
    print(b)
    # суммируем элементы массива по столбцам
    print(f'сумма элементов массива по столбцам:\n{b.sum(axis=0)}')
    # вывод количество элементов
    print(f'количество элементов массива- {b.size}')
    # вывод размерности
    print(f'размерность массива- {b.shape}')
    # вывод минимального элемента
    print(f'минимальный элемент- {b.min()}')
    # вывод максимального элемента
    print(f'максимальный элемент- {b.max()}')
    div_2 = (a % 2 == 0)
    print(f'элементы массива которые делятся на 2:\n{a[div_2]}')
    c = b * 5
    print(f'умножаем элементы массива на число:\n{c}')
    summ_b_c = b + c
    print(f'сложение 2 массивов:\n {summ_b_c}')
    array_flip = np.flip(summ_b_c)
    print(f'переворачиваем предыдущий массив:\n{array_flip}')


image_file = "d'va.png"
image_transform(image_file)
numpy_array()

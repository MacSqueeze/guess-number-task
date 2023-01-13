"""Игра угадай число
Компьютер сам загадывает и сам угадывает число 
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Функция угадывания числа

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0 # Число попыток
    predict_number = 50 # Серединное значение диапазона, откуда берем случайное число
    step = predict_number # Переменная для сдвига, уменьшающаяся вдвое с каждой итерацией
    
    """Если представить диапазон случайных чисел, откуда берется загадываемое число,
    как отрезок, то predict_number будет точкой на середине, которая с каждой
    итерацией будет смещаться на step влево или вправо по этому отрезку
    """

    while True:
        count += 1
        step = int(step / 2) # Уменьшение следующего шага вдвое
        if step < 1:
            step = 1 # После некоторого числа итераций step станет меньше единицы.
                     # В таком случае step становится 1
        if number < predict_number:
            predict_number -= step # Смещение влево на step
        elif number == predict_number:
            break # Выход из цикла
        else:
            predict_number += step # Смещение вправо на step
        
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))  # Загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number)) # Угадывание каждого числа в массиве

    score = int(np.mean(count_ls))
    print(f"Минимальное число попыток: {min(count_ls)}")
    print(f"Максимальное число попыток: {max(count_ls)}")
    print(f"Среднее число попыток: {score}")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
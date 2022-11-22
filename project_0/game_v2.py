"""
Игра угадай число
Компьютер сам загадывает сам пытается угадать число
"""

import numpy as np


def random_predict_with_correction(number:int=1) -> int:
    """Угадываем случайное число с коррекцией

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    min = 0
    max = 101
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(min, max)
        if number == predict_number:
            break # выход из цикла когда угадали число
        
        elif number < predict_number: # предполагаемое число
            max = predict_number
        
        elif number > predict_number:
            min = predict_number
            
    return count
        

def random_predict(number:int=1) -> int:
    """Угадываем случайное число

    Args:
        number (int, optional): Загадывем число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 501) # предполагаемое число
        if number == predict_number:
            break # выход из цикла когда угадали число
    return count


def score_game(predict_function) -> int:
    """За какое количество попыток в средлнем угадывает число компьютер по нашему алгоритму

    Args:
        predict_function ([type]): функция угадывания числа

    Returns:
        int: среднее количетсво попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем "сид" рандома для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # заранее загадали 1000 чисел и заложили в список
    
    for number in random_array:
        count_ls.append(predict_function(number))
        
        score = int(np.mean(count_ls))
        print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
        return(score)
    

if __name__ == "__main__":
    # RUN
    score_game(random_predict_with_correction)
    # print(f'Среднее количество попыток компьютера при случайном подборе: {score_game(random_predict)}')
    # print(f'Среднее количество попыток компьютера при случайном подборе с коррекцией: {}')
    
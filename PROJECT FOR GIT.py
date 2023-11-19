import numpy as np

def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1

    Returns:
        int: число попыток
    """
    
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count


def score_game(random_predict) -> int:
    """ За какое количество попыток в среднем наш алгоритм справляется из 1000 подходов

    Args:
        random_predict([type]): функция угадывания

    Returns:
        int: среднее значение попыток
    """
    
    count_lst = [] # пустой список, в нем будут вычисляться средние значения
    np.random.seed(1) # Закрепляем seed -> фиксируем один и тот же Рандом постоянно
    random_array = np.random.randint(1, 101, size = (1000))
    
    for num in random_array:
        count_lst.append(random_predict(num))
        
    general_score = int(np.mean(count_lst))
    
    print(f"Алгоритм справляется с нахождением загаданно числа за {general_score} попыток")
    
    return general_score

# Конструкция, которая в случае импорта как библиотеки не запускает return, а в файле запускает

if __name__ == '__main__':
    score_game(random_predict) 
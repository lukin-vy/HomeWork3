import random
from customers_functions import get_win

def win_random_agent(observation, configuration):
    random_value = random.randint(0, 2)
    #наш ход бьет случайное значение
    return get_win(random_value)

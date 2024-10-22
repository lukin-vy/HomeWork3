import random
from customers_functions import get_win

def win_last_agent(observation, configuration):
    if observation.step > 0:
        lastOpponentAction = observation.lastOpponentAction
        #Наш ход бьет предыдущий ход оппонента
        return get_win(lastOpponentAction)
    else:
        return random.randint(0, 2)

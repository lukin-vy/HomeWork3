import random
from collections import Counter
from customers_functions import get_win

agent_10_opponent_series = Counter()

def win_often_agent(observation, configuration):
    #Счетчик как ходит противник
    global agent_10_opponent_series
    
    if observation.step > 0:
        lastOpponentAction = observation.lastOpponentAction
        #Запишем ход противника
        agent_10_opponent_series[lastOpponentAction] =+ 1
        #Получим часто используемый ход противника
        often_actions = agent_10_opponent_series.most_common(1)[0][0]
        #Наш ход бьет часто используемый ход противника
        return get_win(often_actions)
    else:
        return random.randint(0, 2)

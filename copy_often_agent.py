import random
from collections import Counter

agent_9_opponent_series = Counter()

def copy_often_agent(observation, configuration):
    #Счетчик как ходит противник
    global agent_9_opponent_series
    
    if observation.step > 0:
        lastOpponentAction = observation.lastOpponentAction
        #Запишем ход противника
        agent_9_opponent_series[lastOpponentAction] =+ 1
        #Получим часто используемый ход противника
        often_actions = agent_9_opponent_series.most_common(1)[0][0]
        return often_actions
    else:
        return random.randint(0, 2)

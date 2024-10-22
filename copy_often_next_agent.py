import random
from customers_functions import *

agent_11_opponent_series = list()

def copy_often_next_agent(observation, configuration):
    #Список ходов противника
    global agent_11_opponent_series
            
    if observation.step > 0:
        lastOpponentAction = observation.lastOpponentAction
        #Запишем ход противника
        agent_11_opponent_series.append(lastOpponentAction)
        #Получим часто используемый следующий ход противника
        often_next_action = get_possible_next_actions(agent_11_opponent_series, lastOpponentAction)
        if often_next_action != None:
            #Если было получено значение
            return often_next_action
        else:
            #Если значение не было получено, возвращаем случайное число
            return random.randint(0, 2)
    else:
        return random.randint(0, 2)

        

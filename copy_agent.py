import random
def copy_agent(observation, configuration):
    step = observation.step
    if step > 0:
        lastOpponentAction = observation.lastOpponentAction
        return lastOpponentAction
    else:
        return random.randint(0, 2)

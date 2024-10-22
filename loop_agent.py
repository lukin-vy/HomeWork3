def loop_agent(observation, configuration):
    step = observation.step
    result = int(step % 3)
    return result

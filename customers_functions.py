
from collections import Counter

def get_win(opponent_actions):
    #Добавляем 1, так как следующее число бьет предыдущее
    #Остаток от деления на 3, для того что бы не выйти ща рамки 0, 1, 2, где
    # 0 - камень
    # 1 - бумага
    # 2 - ножницы
    return (opponent_actions + 1) % 3

#Функция для получения самого частого хода после текущего
def get_possible_next_actions(opponent_series, last_actions):
    #Объявим счетчик
    counter_steps = Counter()
    #В цикле пройдемся по всем ходам оппонента
    for index, value in enumerate(opponent_series):
        #Если проверяемый ход такой же как предыдущий ход
        #и это не последний элемент списка
        if value == last_actions and index != len(opponent_series) - 1:
            #То запишем следующий по индексу ход
            counter_steps[opponent_series[index+1]] =+1
    #Определим самый частый следующий ход оппонента
    often_next_actions = counter_steps.most_common(1)
    if len(often_next_actions) != 0:
        #Если нашли значение
        return often_next_actions[0][0]
    else:
        #Если ничего не нашли
        return None

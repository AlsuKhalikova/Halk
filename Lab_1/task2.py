list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count = len(list_players)
index_of_medium_player = int(count / 2)
team_1 = list_players[:index_of_medium_player]
team_2 = list_players[index_of_medium_player:]
print(team_1)
print(team_2)

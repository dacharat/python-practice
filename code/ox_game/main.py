from player import Player
from table import Table

size = int(input('Enter table size: '))
nb_of_players = int(input('Enter number of players: '))
sym_list = [input(f'Enter player{i+1} symbol: ') for i in range(nb_of_players)]
table = Table(size, nb_of_players, sym_list)

who_win = table.play()
print(f'Player"{who_win}" win!!')
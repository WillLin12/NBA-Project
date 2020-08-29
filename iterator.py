import csv
import player.py as player
players = []

with open('players.csv') as player_stats:
    csv_reader = csv.reader(player_stats, delimiter=',')
    line_count = 0
    for row in csv_reader:
        player = player(row[0], row[1], ...)

        
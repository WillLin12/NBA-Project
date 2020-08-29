import csv
import player as player

with open('playerstats.csv') as player_stats:
    csv_reader = csv.reader(player_stats, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)

     
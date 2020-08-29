import csv
import player as player


dict = {}

with open('playerstats.csv') as player_stats:
    csv_reader = csv.reader(player_stats, delimiter=',')
    line_count = 0
    for row in csv_reader:
        p = player.Player(row[0], row[1], row[29], row[23], row[24], row[25], row[26], row[11], row[8], row[18], row[27], row[9], row[19])
        dict[p.get_id()] = p

    for key, value in dict.items():
        print (key, value.get_name())
import csv
import player as player
import operator


dict = {}

with open('playerstats.csv') as player_stats:
    csv_reader = csv.reader(player_stats, delimiter=',')
    next(csv_reader, None)
    line_count = 0
    for row in csv_reader:
        p = player.Player(int(row[0]), row[1], float(row[29]), float(row[23]), float(row[24]), float(row[25]), float(row[26]), float(row[11]), float(row[8]), float(row[18]), float(row[27]), float(row[9]), float(row[19]))
        dict[p.get_id()] = p
        #print(dict.keys())


for value in (sorted(dict.values(), key=operator.attrgetter("pts"))):
    print(value.get_name(), value.get_pts(), value.calculate_pct(), value.calculate_ftpct)


# for key, value in dict.items():
#     pid = float(key)
#     if pid < 100:
#         print (key, value.get_name(), value.get_pts())
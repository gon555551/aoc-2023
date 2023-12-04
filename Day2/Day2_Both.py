with open("day2.txt", "r") as f:
    inp = f.readlines()
shown_list = [shown.split(";") for shown in [data.split(":")[1].strip() for data in inp]]
for i, game in enumerate(shown_list):
    for j, event in enumerate(game):
        shown_list[i][j] = [s.strip().split(" ") for s in event.split(",")]
aggr, res = [], []
for i, game in enumerate(shown_list):
    red, green, blue = 0, 0, 0
    for event in game:
        for pair in event:
            if pair[1] == "red":
                    if int(pair[0]) > red:
                        red = int(pair[0])
            if pair[1] == "green":
                if int(pair[0]) > green:
                    green = int(pair[0])
            if pair[1] == "blue":
                if int(pair[0]) > blue:
                    blue = int(pair[0])       
            if int(pair[0]) > 14:
                if i + 1 not in aggr:
                    aggr.append(i + 1)
            if (int(pair[0]) > 12 and pair[1] != "blue") and (int(pair[0]) > 12 and pair[1] != "green"):
                if i + 1 not in aggr:
                    aggr.append(i + 1)
            if int(pair[0]) > 13 and pair[1] != "blue":
                if i + 1 not in aggr:
                    aggr.append(i + 1)
    res.append(red*green*blue)
print(f"part1 {sum(range(len(shown_list) + 1)) - sum(aggr)}, part2 {sum(res)}")
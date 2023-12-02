def main():
    with open("day2.txt", "r") as f:
        inp = f.readlines()

    # Get shown_list in format [games: [events: [pairs: [number, colour]]]]
    just_shown = [data.split(":")[1].strip() for data in inp]
    shown_list = [shown.split(";") for shown in just_shown]
    for i, game in enumerate(shown_list):
        for j, event in enumerate(game):
            shown_list[i][j] = [s.strip().split(" ") for s in event.split(",")]

    # Start at 0 (ultimate minimum) and simply check and replace if a bigger number appears, for each colour
    aggr = []
    for game in shown_list:
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

        aggr.append(red * green * blue)

    result = sum(aggr)
    print(result)
    return result


if __name__ == "__main__":
    main()

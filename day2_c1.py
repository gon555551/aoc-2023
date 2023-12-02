# 12 red, 13 green, 14 blue


def main():
    with open("day2.txt", "r") as f:
        inp = f.readlines()

    # Get shown_list in format [games: [events: [pairs: [number, colour]]]]
    just_shown = [data.split(":")[1].strip() for data in inp]
    shown_list = [shown.split(";") for shown in just_shown]
    for i, game in enumerate(shown_list):
        for j, event in enumerate(game):
            shown_list[i][j] = [s.strip().split(" ") for s in event.split(",")]

    # Go through the pairs and find games that AREN'T possible
    aggr = []
    for i, game in enumerate(shown_list):
        for event in game:
            for pair in event:
                if int(pair[0]) > 14:
                    if i + 1 not in aggr:
                        aggr.append(i + 1)

                if (int(pair[0]) > 12 and pair[1] != "blue") and (
                    int(pair[0]) > 12 and pair[1] != "green"
                ):
                    if i + 1 not in aggr:
                        aggr.append(i + 1)

                if int(pair[0]) > 13 and pair[1] != "blue":
                    if i + 1 not in aggr:
                        aggr.append(i + 1)

    # Remove the sum of IMPOSSIBLE games from the sum of total games
    result = sum(range(len(shown_list) + 1)) - sum(aggr)
    print(result)
    return result


if __name__ == "__main__":
    main()

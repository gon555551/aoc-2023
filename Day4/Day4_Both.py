from math import log2


with open("day4.txt", "r") as f:
    inp = f.readlines()


inp = [
    [a.strip().split(" "), b.strip().split(" ")]
    for a, b in (line.split(":")[1].strip().split("|") for line in inp)
]


class Card:
    points: int
    won: list[int]
    idt: int

    def __init__(self, idt: int, points: int):
        self.idt = idt
        self.points = points
        self.won = self.get_won()

    def get_won(self):
        if self.points == 0:
            return []
        return [
            i for i in range(self.idt + 1, self.idt + 1 + int(log2(self.points) + 1))
        ]


def main():
    # Get all the cards
    cards = []
    for i, game in enumerate(inp):
        result = 0
        for win in game[0]:
            if win == "":
                continue
            if int(win) in [int(n) for n in game[1] if n != ""]:
                if result == 0:
                    result += 1
                else:
                    result *= 2
        cards.append(Card(i, result))

    # Calc part 2
    check = [1 for card in cards]
    for card in cards:
        for i in card.won:
            check[i] += check[card.idt]

    print(sum([c.points for c in cards]), sum(check))


if __name__ == "__main__":
    main()

# Better way to do day3!

with open("day3.txt", "r") as f:
    inp = f.readlines()

for i, line in enumerate(inp):
    mat = []
    for char in line.strip():
        mat.append(char)
    inp[i] = mat


# Number class which handles the position and value of every number
class Number:
    ind: list[(int, int)]
    inp: list[list]
    sur: list[(int, int)]
    value: int
    eng: bool = False

    def __init__(self, ind: list[(int, int)], inp: list[list]):
        self.ind = ind
        self.inp = inp
        self.sur = self.get_sur()
        self.value = self.get_value()

    def get_value(self) -> int:
        n = ""
        for i in self.ind:
            n += self.inp[i[0]][i[1]]
        return int(n)

    # A bit redundant as it returns more than the surrounding indeces. It's fine though.
    def get_sur(self) -> list[(int, int)]:
        _temp = []
        for i in self.ind:
            var = [-1, 1]
            for v in var:
                _temp.append((i[0] + v, i[1]))
                _temp.append((i[0] + v, i[1] + v))
                _temp.append((i[0] + v, i[1] - v))
                _temp.append((i[0], i[1] + v))
        return _temp


nstr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ponctuation = [
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
]


def main():
    ilst = []
    nlst = []
    
    # Gets all numbers into nlst
    for i, line in enumerate(inp):
        for j, char in enumerate(line):
            if char in nstr:
                ilst.append((i, j))
                if j == len(line) - 1:
                    nlst.append(Number(ilst, inp))
                    ilst = []
                continue
            if ilst != []:
                nlst.append(Number(ilst, inp))
                ilst = []

    # Checks if the number touches a symbol (c1)
    for n in nlst:
        for i in n.sur:
            try:
                if inp[i[0]][i[1]] in ponctuation:
                    n.eng = True
            except IndexError:
                pass

    # Gets the gear ratio number pairs (c2)
    gear = []
    for i, line in enumerate(inp):
        for j, char in enumerate(line):
            if char == "*":
                count = []
                for n in nlst:
                    if (i, j) in n.sur:
                        count.append(n)
                if len(count) != 2:
                    continue
                gear.append(count)

    print(
        sum([n.value for n in nlst if n.eng]),
        sum([i[0].value * i[1].value for i in gear]),
    )


if __name__ == "__main__":
    main()

# First attempt, it's rather bad and it didn't look easy to solve c2 using this code, so I made it a different way

with open("day3.txt", "r") as f:
    inp = f.readlines()

for i, line in enumerate(inp):
    mat = []
    for char in line.strip():
        mat.append(char)
    inp[i] = mat

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
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def main():
    touch = []
    cont = []
    for i, line in enumerate(inp):
        for j, char in enumerate(line):
            if char in numbers:
                if (i, j - 1) in cont:
                    cont.append((i, j))
                if i == 0:
                    if j == 0:
                        if (
                            inp[i][j + 1] in ponctuation
                            or inp[i + 1][j] in ponctuation
                            or inp[i + 1][j + 1] in ponctuation
                        ):
                            cont.append((i, j))
                            if (i, j - 1) not in cont:
                                touch.append((i, j))
                                continue
                    if j == len(line) - 1:
                        if (
                            inp[i][j - 1] in ponctuation
                            or inp[i + 1][j] in ponctuation
                            or inp[i + 1][j - 1] in ponctuation
                        ):
                            cont.append((i, j))
                            if (i, j - 1) not in cont:
                                touch.append((i, j))
                                continue
                    if (
                        inp[i][j + 1] in ponctuation
                        or inp[i + 1][j] in ponctuation
                        or inp[i][j - 1] in ponctuation
                        or inp[i + 1][j + 1] in ponctuation
                        or inp[i + 1][j - 1] in ponctuation
                    ):
                        cont.append((i, j))
                        if (i, j - 1) not in cont:
                            touch.append((i, j))
                            continue
                    continue
                if i == len(inp) - 1:
                    if j == 0:
                        if (
                            inp[i][j + 1] in ponctuation
                            or inp[i - 1][j] in ponctuation
                            or inp[i - 1][j + 1] in ponctuation
                        ):
                            cont.append((i, j))
                            if (i, j - 1) not in cont:
                                touch.append((i, j))
                                continue
                    if j == len(line) - 1:
                        if (
                            inp[i][j - 1] in ponctuation
                            or inp[i - 1][j] in ponctuation
                            or inp[i - 1][j - 1] in ponctuation
                        ):
                            cont.append((i, j))
                            if (i, j - 1) not in cont:
                                touch.append((i, j))
                                continue
                    if (
                        inp[i][j + 1] in ponctuation
                        or inp[i][j - 1] in ponctuation
                        or inp[i - 1][j] in ponctuation
                        or inp[i - 1][j - 1] in ponctuation
                        or inp[i - 1][j + 1] in ponctuation
                    ):
                        cont.append((i, j))
                        if (i, j - 1) not in cont:
                            touch.append((i, j))
                            continue
                    continue
                if j == 0:
                    if (
                        inp[i][j + 1] in ponctuation
                        or inp[i + 1][j] in ponctuation
                        or inp[i - 1][j] in ponctuation
                        or inp[i + 1][j + 1] in ponctuation
                        or inp[i - 1][j + 1] in ponctuation
                    ):
                        cont.append((i, j))
                        if (i, j - 1) not in cont:
                            touch.append((i, j))
                            continue
                    continue

                if j == len(line) - 1:
                    if (
                        inp[i + 1][j] in ponctuation
                        or inp[i][j - 1] in ponctuation
                        or inp[i - 1][j] in ponctuation
                        or inp[i - 1][j - 1] in ponctuation
                        or inp[i + 1][j - 1] in ponctuation
                    ):
                        if (i, j) not in touch and (i, j) not in cont:
                            if (i, j - 1) in touch:
                                cont.append((i, j))
                                continue
                            touch.append((i, j))
                            continue
                    continue

                if (
                    inp[i][j + 1] in ponctuation
                    or inp[i + 1][j] in ponctuation
                    or inp[i][j - 1] in ponctuation
                    or inp[i - 1][j] in ponctuation
                    or inp[i + 1][j + 1] in ponctuation
                    or inp[i - 1][j - 1] in ponctuation
                    or inp[i + 1][j - 1] in ponctuation
                    or inp[i - 1][j + 1] in ponctuation
                ):
                    if (i, j) not in touch and (i, j) not in cont:
                        if (i, j - 1) in touch:
                            cont.append((i, j))
                            continue
                        touch.append((i, j))
                        continue

    n = []
    for index in touch:
        right_j = index[1]
        left_j = index[1]
        while True:
            if inp[index[0]][right_j] in numbers and right_j < len(inp[index[0]]):
                right_j += 1
            if inp[index[0]][left_j] in numbers and left_j > 0:
                left_j -= 1
            if (
                right_j == len(inp[index[0]]) or inp[index[0]][right_j] not in numbers
            ) and (left_j == 0 or inp[index[0]][left_j] not in numbers):
                break

        temp_n = inp[index[0]][left_j:right_j]
        temp_ = ""
        for i in temp_n:
            if i not in numbers:
                continue
            temp_ += i
        n.append(int(temp_))

    print(sum(n))


if __name__ == "__main__":
    main()

import string


with open("day1.txt", "r") as f:
    inp = f.readlines()


alnum = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for i, o in enumerate(inp):
    num = ""
    for j, l in enumerate(o):
        if l in string.digits:
            num += l
            break
        
        # Word search
        ind = 1
        found = False
        while True:
            if o[j : j + ind] in alnum.keys():
                num += alnum[o[j : j + ind]]
                found = True
                break
            if o[j : j + ind] not in [n[0:ind] for n in alnum.keys()]:
                break
            ind += 1

        if found:
            break
    
    # Backward search
    for j, l in enumerate(o):
        if o[-j - 1] in string.digits:
            num += o[-j - 1]
            break

        ind = 1
        found = False
        while True:
            if o[-j - 1 : -j - 1 + ind] in alnum.keys():
                num += alnum[o[-j - 1 : -j - 1 + ind]]
                found = True
                break
            if o[-j - 1 : -j - 1 + ind] not in [n[0:ind] for n in alnum.keys()]:
                break
            ind += 1

        if found:
            break

    inp[i] = num

result = sum([int(n) for n in inp])
print(result)

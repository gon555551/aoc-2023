import string


with open("day1.txt", "r") as f:
    inp = f.readlines()

for i, o in enumerate(inp):
    num = ""
    for l in o:
        if l in string.digits:
            num += l
            break
        
    # Backwards search
    for l in reversed(o):
        if l in string.digits:
            num += l
            break
    inp[i] = num

result = sum([int(n) for n in inp])
print(result)

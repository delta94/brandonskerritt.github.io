def accum(s):
# list generator for every x in s times x by current position (1 for 0, 2 for 2) etc
    tuples = list(map(lambda x: (x[0]+1, x[1]), list(enumerate(s))))
    to_string = []
    for x in tuples:
        num = x[0]
        num -= 1
        x = (x[1] * x[0]).capitalize()
        to_string.append(x)
    return "-".join(to_string)

print(accum("EvidjUnokmM"))
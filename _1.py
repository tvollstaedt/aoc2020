def solve(input):
    for i in input:
        for j in input:
            if int(i) + int(j) == 2020:
                return int(i) * int(j)
    return 0

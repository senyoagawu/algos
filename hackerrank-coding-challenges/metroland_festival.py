def minimizeCost(numPeople, x, y):
    # Write your code here
    from math import inf

    c1 = []
    c2 = []
    numrows = x[1] - x[0] + 1
    numcols = y[1] - y[0] + 1

    for xi in range(numrows):
        row = []
        for yi in range(numcols):
            row.append(xi + yi)
        c1.append([cost * numPeople[0] for cost in row])
        revers = list(row.__reversed__())
        c2.insert(0, [cost * numPeople[1] for cost in revers])

    cummin = [inf, (-1, -1)]
    for i in range(len(c1)):
        for j in range(len(c1[0])):
            cost = c1[i][j] + c2[i][j]
            if cost < cummin[0]:
                cummin = [cost, (i, j)]

    return cummin[0]


numPeople = [1, 1]
x = [1, 2]
y = [1, 2]

print(minimizeCost(numPeople, x, y))
print(minimizeCost([1, 1], [1, 3], [1, 1]))

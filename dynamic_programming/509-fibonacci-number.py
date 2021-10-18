def fib(n):
    tab = [0, 1, 1]
    while n > len(tab) - 1:
        tab.append(tab[-2] + tab[-1])
    return tab[-1]

def climbStairs(self, n: int) -> int:
    tab = [1, 2]
    while True:
        if n <= len(tab):
            return tab[-1]
        tab.append(tab[-1] + tab[-2])

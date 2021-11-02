    from math import sqrt


    class k_smallest_holder:
        def __init__(self, k):
            self.k = k
            self.max = None
            self.points = []
            self.length = 0

        def dist(self, pos):
            return sqrt(pos[1] ** 2 + pos[0] ** 2)

        def add(self, pos):
            temp = self.points.copy()
            temp.append((self.dist(pos), pos))
            temp.sort(key=lambda x: x[0])
            self.points = temp[: self.k]
            # print(self.points)

        @property
        def answer(self):
            return [pos[1] for pos in self.points]


    k = k_smallest_holder(k)
    positions = [[1, 3], [-2, 2]]
    for pos in points:
        k.add(pos)

    return k.answer

import json
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
        d = self.dist(pos)
        if self.length == 0:
            self.points.append(pos)
            self.length += 1
            self.max = d
            return
        if self.max and self.k == len(self.points) and d >= self.max:
            return
        for i in range(self.length):
            print("here", pos, self.points)
            if self.max is not None and d > self.max:
                return
            if i == self.length - 1:
                self.points.append(pos)
                self.length += 1
                self.max = d
                return
            elif d < self.dist(self.points[i]):
                self.points.insert(i, pos)
                self.length += 1
                if self.length > self.k:
                    self.points.pop()
                    self.length -= 1
                    self.max = self.dist(self.points[-1])
                return

        # print(self.points)

    @property
    def answer(self):
        return [pos for pos in self.points]


def kClosest(points, k):

    k = k_smallest_holder(k)
    for pos in points:
        k.add(pos)

    return k.answer


file = json.load(open("failing-test-cases.json"))["3"]

print(kClosest(file["points"], file["k"]))

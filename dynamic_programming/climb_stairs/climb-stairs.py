def split_path(way):
    # keep all the previous paths!
    print(way)
    all_ways = [way, way + [1], way + [2]]
    return [path for path in all_ways if len(path) > 0]


def br(var):
    return var


def unique(arrays):
    uniq = set()
    print("in unique")
    for array in arrays:
        uniq.add("_".join(array))
    arr = [el.split("_") for el in list(uniq)]
    return arr


def generate_paths(n, paths=[[]], i=0, dic={"0": [[]]}):
    if n == i:
        return dic
    dic[str(i + 1)] = [split_path(p) for p in dic[str(i)]]

    print(dic)
    return generate_paths(n, paths, i + 1, dic)

    paths
    paths = [[1]]
    for step in range(n):
        br(paths)
        print("step", step)
    # filter out paths that are too long or short

    print("paths", paths)
    # correct_subset = [
    #     possible_path for possible_path in paths if sum(possible_path) == n
    # ]
    # # grab unique ones
    # uniq_subset = unique(correct_subset)

    # return uniq_subset
    return paths


generate_paths(2)


class Ways:
    def __init__(self, ways):
        self.ways = ways

    def split_way(self):
        self.ways = []

    def count(self):
        str_reps = self.ways.map(lambda x: str(x))  # map them to string
        uniq_str_reps = set(str_reps)  # remove duplicates
        return len(uniq_str_reps)


class Path:
    def __init__(self, path):
        self.path = path
        self.length = len(path)

    def split_path(self):
        split_paths = [self.path + [1], self.path + [2]]
        return [Path(p) for p in split_paths]

    def __str__(self):
        return "".join(self.path)

    def __repr__(self):
        return f"<path {''.join(self.path)} />"


# def climb_stairs(n, ways=[[]]):
#     """brute force:
#     to get to step 5 taking 1 or 2 steps, it will take 5 or less steps.
#     upper bound of n steps.
#     so lets generate all the other possible paths that created in n steps.
#     note: we generate extra, and then get rid of ones past desired step.
#     """
#         brute_paths = generate_paths(n)

#         brute_paths.filter(lambda x: sum(x) == target_steps)# filter out paths that are too long
#         climb_stairs([[1], [2]])
#     for _ in range(n):
#         temp = []
#         for way in ways:
#             t1 = [way].append(1)
#             t2 = way.append(2)
#             print("way", way, "temp", temp, "new ways", t1, t2)
#             # temp.extend([way.append(1), way.append(2)])
#             print("temp", temp)
#         ways += temp
#     return ways


# climb_stairs(1)
"""
memoize it
"""

"""
solve with tabulation
"""

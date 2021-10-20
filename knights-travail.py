def next_posis(list_of_positions):
    positions = []fasdfasdfas
    for x, y in list_of_positions:
        positions.extend(
            [
                (x + 1, y + 2),
                (x + 1, y - 2),
                (x - 1, y + 2),
                (x - 1, y - 2),
                (x + 2, y + 1),
                (x + 2, y - 1),
                (x - 2, y + 1),
                (x - 2, y - 1),
            ]
        )
    return positions

def knights_travail(curr_pos, target_pos, visited=set(), count=0):
    stack = [[curr_pos]]
    while len(stack) > 0:
        lvl = stack.pop()
        if target_pos in lvl:
            return count
        visited = visited.union(lvl)
        stack.append([p for p in next_posis(lvl) if p not in visited])
        count += 1

    return [None, "impossible is nothing"]


print(dfs((4, 4), (6, 8)))

def subsets(some_set):
    if len(some_set) == 0:
        return [[]]
    firstEntity, subs = some_set[0], subsets(some_set[1:])
    new_subsets = [[firstEntity, *s] for s in subs]
    return subs + new_subsets


def combinations(some_set, pick_num):
    if not some_set: return [[]]
    firstEntity = some_set[0]
    subs = subsets(some_set[1:])
    new_subsets = [[firstEntity, *s] for s in subs]
    return [sub for sub in subsets if len(sub) == pick_num]




def flatten_epic_fail(unflattened_array):
    output = []
    for el in unflattened_array:
        if type(el) == list:
        else:
            output + [el]
    else:
        return unflattened_array
    return output


# print(subsets([1,2,5,6,4,9]))
# print(combinations([1,2,5,6,4,9], 3))
# print(combinations([1,2,5,6,4,9], 5))

unflattened_arr = [ 1, [2,3,4],[[5, [[6]]]],7, [[8]]]


class FlattenLists: 
    def init(self, arr):
        self.arr = arr

    def w1(self):
        _copy = self.arr1.copy

        flat_list = list()
        for sub_list in _copy:
            flat_list += sub_list
            print(flat_list)
        return(flat_list)

    def w2(self): 
        _copy = self.arr2.copy() 
# def list_comp_flatten(list_of_lists):
        flat_list = list()
        return [flat_list + sub_list for sub_list in _copy]
        # return flat_list

fl1 = FlattenLists([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
fl2 = FlattenLists([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(fl1.w1())
print(fl2.w2())
print(fl1, fl2)

print(fl1, fl2)
a1, a2 = fl1.w2)
# Returns: [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# list_comp_flatten(list_of_lists)
def my_each(arr, callback):
    [callback(thing) for thing in arr]


def my_select(arr, callback):
    return [a for a in arr if callback(a)]


def my_reject(arr, callback):
    return [a for a in arr if callback(a) == False]


arr = [1, 2, 3, 4]

my_each(arr, print)
filtered = my_select(arr, lambda x: x % 2 == 0)
print(filtered)
rejected = my_reject(arr, lambda x: x % 2 == 0)
print(rejected)


def any(arr, callback):
    for a in arr:
        if callback(a):
            return True
    return False


def my_flatten(arr):
    if type(arr) != list:
        return arr
    flattend = []
    for thing in arr:
        if type(thing) == list:
            flattend.extend(my_flatten(thing))
        else:
            flattend.append(thing)
    return flattend


arr = [1, 2, 3, [4, [5, 6]], [[[7]], 8]]

print(my_flatten(arr))


def help_out_of_range(arr, idx):
    if idx >= len(arr):
        return None
    return arr[idx]


def my_zip(arr1, *other_arrays):
    zipped = []
    for idx, num in enumerate(arr1):
        arr = [num]
        arr_other = [help_out_of_range(arr, idx) for arr in other_arrays if id]
        arr.extend(arr_other)
        zipped.append(arr)
    print(zipped)
    return zipped


a = [4, 5, 6]
b = [7, 8, 9]

my_zip([1, 2, 3], a, b)  # => [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
my_zip(a, [1, 2], [8])  # => [[4, 1, 8], [5, 2, nil], [6, nil, nil]]
my_zip([1, 2], a, b)  # => [[1, 4, 7], [2, 5, 8]]

c = [10, 11, 12]
d = [13, 14, 15]
my_zip([1, 2], a, b, c, d)  # => [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14]]


def my_rotate(arr, rots):
    simplified_rots = rots % len(arr)
    ans = arr[simplified_rots:]
    ans.extend(arr[:simplified_rots])
    print(ans)
    return ans


def my_join(arr, sep):
    s, rest = str(arr[0]), arr[1:]
    for thing in rest:
        s += sep + thing
    print(s)
    return s


def my_reverse(arr, sep=""):
    return [arr[i - 1] for i in range(len(arr), 0, -1)]


a = ["a", "b", "c", "d"]
my_join(a, sep="")  # => "abcd"
my_join(a, sep="$")

print(my_reverse([1, 2, 3, 4, 5, 6]))


a = ["a", "b", "c", "d"]
my_rotate(a, 1)  # => ["b", "c", "d", "a"]
my_rotate(a, 2)  # => ["c", "d", "a", "b"]
my_rotate(a, -3)  # => ["b", "c", "d", "a"]
my_rotate(a, 15)  # => ["d", "a", "b", "c"]

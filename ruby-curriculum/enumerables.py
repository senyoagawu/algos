def my_each(arr, callback):
    [callback(thing)for thing in arr] 

def my_select(arr, callback):
    return  [a for a in arr if callback(a) ]
    
def my_reject(arr, callback):
    return [a for a in arr if callback(a) == False]
arr = [1,2,3,4]

my_each(arr, print)
filtered = my_select(arr, lambda x:x%2 == 0)
print(filtered)
rejected = my_reject(arr, lambda x:x%2 == 0)
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
        
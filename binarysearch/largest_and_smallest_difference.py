def largest_and_smallest_difference(self, nums: List(num), k):
    def minmaxdiff(arr):
        return arr[-1] - arr[0]


    def insertInOrder(minimized, num):
        for idx, el in enumerate(minimized):
            if num <= el:
                minimized.insert(idx, num)
        print(minimized)
        return minimized
        
    minimized = nums[:k]
    minimized.sort()

    for num in nums[k:]:
        prev_range = minmaxdiff(minimized)
        left_range = minmaxdiff(minimized[:-2])
        right_range = minmaxdiff(minimized[1:])
        if left_range < right_range:
            minimized = minimized[:-2]
        else:
            minimized = minimized[1:]



def pop_or_shit(arr, length):
    if len(arr) > length:
        return
    if arr[-1] - arr[1] < arr[-2] - arr[0]:
        arr = arr[1:]
    else:
        arr = arr[:-2]

    return arr

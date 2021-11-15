def binary_search(nums, target):
    """
    704. Binary Search
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity."""

    def recurse(nums, target, currIdx):
        # print(nums, target, currIdx)
        # if nums empty return -1
        if len(nums) == 0:
            return -1
        # find mididx
        midIdx = (len(nums) / 2).__floor__()
        # print("midIdx", midIdx)
        # check <=>
        candidate = nums[midIdx]
        #    if > return bsearch with array roght of idx, targrt, midIdx + curidx
        if candidate < target:
            return recurse(nums[midIdx + 1 :], target, currIdx + midIdx + 1)
        #    if < return bsearch(areay kedr of target, target curIdx)
        elif candidate > target:
            return recurse(nums[:midIdx], target, currIdx)
        #    else teturn mididx
        else:
            return midIdx + currIdx

    return recurse(nums, target, 0)


print(binary_search([-1, 0, 3, 5, 9, 12], 9))
print(binary_search([-1, 0, 3, 5, 9, 12], 2))

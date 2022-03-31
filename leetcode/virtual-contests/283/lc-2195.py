def minimalKSum(nums, k):
    ans = []
    n = 1
    pointer = 0
    while len(ans) < k and pointer < len(nums):
        print(ans)
        num = nums[pointer]
        if n < num:
            ans.append(n)
        else:
            pointer += 1
        n += 1
    if pointer > len(nums):  # out of range
        ans.append(n)
        n += 1
    for _ in range(k - len(nums) - 2):
        print(ans)
        ans.append(n)
        n += 1
    return sum(ans)


# print(minimalKSum([1,4,25,10,25], 2))
print(minimalKSum([5, 6], 6))

def minimalKSum(nums, k):
    ans = []
    n = 1
    pointer = 0
    while len(ans) < k: 
        while pointer < len(nums):
            num = nums[pointer]
            if n < num:
                ans.append(n)
            else:
                pointer += 1
            n += 1
        if pointer >= len(nums):
            ans.append(n)   
            n+=1
    return sum(ans)    


 
print(minimalKSum([1,4,25,10,25], 2))
# print(minimalKSum([5,6], 6))
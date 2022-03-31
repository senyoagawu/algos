def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for idx, num in enumerate(nums):
        if num in hashmap:
            return [hashmap[num], idx,]
        hashmap[target - num] = idx  ≤≤
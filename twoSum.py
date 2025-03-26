def twoSum(nums, target):
    prevMap = {}  # val : index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return
#example
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target)) # [0, 1]
def containsDuplicate(nums):
    hashmap = set()
    for i in nums:
        if i in hashmap:
            return True
        hashmap.add(i)
    return False
# Time complexity: O(n)

#example
nums = [1, 2, 3, 4, 5, 6, 1, 7]

print(containsDuplicate(nums))
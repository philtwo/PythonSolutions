def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1
    
# Example
arr = [2, 3, 10, 40, 50]
target = 40
result = binary_search(arr, target, 0, len(arr) - 1)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array") 
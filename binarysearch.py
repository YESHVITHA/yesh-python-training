def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Input
n = int(input())

arr = []
for i in range(n):
    num = int(input())  
    arr.append(num)
x = int(input())

# Output
print(binary_search(arr, x))
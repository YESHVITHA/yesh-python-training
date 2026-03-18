def insertionSort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = []
n = int(input("Enter number of words: "))

for i in range(n):
    arr.append(input("Enter word: "))
insertionSort(arr)
print("Sorted list:", arr)
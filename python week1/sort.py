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

def removeduplicates(arr):
    unique=[]
    for i in arr:
        if i not in unique:
            unique.append(i)
    return unique

arr = []
n = int(input("Enter number of words: "))

for i in range(n):
    arr.append(input("Enter word: "))
insertionSort(arr)
print("Sorted list:", arr)
without_duplicate=removeduplicates(arr)
print("the array after removing duplicates",without_duplicate)
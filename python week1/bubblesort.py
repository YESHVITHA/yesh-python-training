def bubble_sort_ascending(arr):
    print("the input array",arr)
    n=len(arr)
    swaps=0

    for i in range(n):
        swapped=False
        for j in range (0,n-i-1):
             if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped=True
                swaps+= 1
             
    return arr, swaps

def bubble_sort_descending(arr):
    n=len(arr)
    swaps=0
    
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped=True
                swaps+= 1
    return arr,swaps 

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

asc_order,asc_swaps = bubble_sort_ascending(arr)
print("Ascending:",asc_order)
print("Ascending swaps",asc_swaps)

desc_order,desc_swaps= bubble_sort_descending(arr)
print("Descending:",desc_order)
print("Descending swaps",desc_swaps)


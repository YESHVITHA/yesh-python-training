def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]

    left_half=merge_sort(left_half)
    right_half=merge_sort(right_half)

    return merge(left_half,right_half)

def merge(left,right):
    merged_list=[]
    i=0
    j=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged_list.append(left[i])
            i+=1
        else:
            merged_list.append(right[j])
            j+=1

    while i<len(left):
        merged_list.append(left[i])
        i += 1

    while j < len(right):
        merged_list.append(right[j])
        j += 1
    return merged_list

if __name__=='__main__':
    my_list=[12,11,13,5,6,7]
    print(f"Given list is: {my_list}")
    sorted_list = merge_sort(my_list)
    print(f"Sorted list is: {sorted_list}")
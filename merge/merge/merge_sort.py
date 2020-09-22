def merge_sort(unsorted_list):
    n = len(unsorted_list)
    if  n > 1 :
        mid = n//2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j  = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_list[k] = left[i]
                i += 1

            else:
                unsorted_list[k] = right[j]
                j += 1
            
            k +=  1

        while i < len(left): 
            unsorted_list[k] = left[i] 
            i += 1
            k += 1
            
        while j < len(right): 
            unsorted_list[k] = right[j] 
            j += 1
            k += 1

def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i], end =" ") 
    print() 
    return arr
if __name__ == '__main__': 
    arr1 = [8,4,23,42,16,15] 
    printList(arr1) 
    merge_sort(arr1) 
    printList(arr1) 

    print("*"*50)
    arr2 = [20,18,12,8,5,-2] 
    printList(arr2) 
    merge_sort(arr2) 
    printList(arr2) 
    print("*"*50)

    arr =[5,12,7,5,5,7] 
    printList(arr) 
    merge_sort(arr) 
    printList(arr) 
    print("*"*50)

    arr = [2,3,5,7,13,11]  
    printList(arr) 
    merge_sort(arr) 
    printList(arr) 
    print("*"*50)

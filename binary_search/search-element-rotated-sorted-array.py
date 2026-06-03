def search_element(arr, n, target):
    low=0
    high=n-1
    while low<= high:
        mid= (low+ high)//2
        if arr[mid]== target:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high= mid-1
            else:
                low= mid+1
        else:
            if arr[mid] <= target <= arr[high]:
                low= mid+1
            else:
                high= mid-1
    return -1

rotated_lst=[7,8,1,3,5]
print(search_element(rotated_lst, len(rotated_lst),3))


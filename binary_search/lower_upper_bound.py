def lower_bound(arr, target):
    low=0
    high= len(arr)-1
    ans= len(arr)
    while low<= high:
        mid= (low + high)//2
        if arr[mid]>= target:
            ans= mid
            high= mid-1
        else:
            low= mid+1
    return ans
def upper_bound(arr, target):
    low=0
    high= len(arr)-1
    ans= len(arr)
    while low<= high:
        mid= (low+ high)//2
        if arr[mid]> target:
            ans= mid
            high= mid-1
        else:
                low= mid+1
    return ans

lst = [1,2,4,5]
target=4
print(upper_bound(lst, target))

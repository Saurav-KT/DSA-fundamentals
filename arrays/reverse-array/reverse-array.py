def reverse_arr(arr: list)-> list:
    left=0
    right= len(arr)-1
    while left<=right:
        arr[left], arr[right]= arr[right], arr[left]
        left+=1
        right-=1
    return arr

arr= [4, 5, 2]
print(reverse_arr(arr))
def find_min_in_an_array(arr):
    if not arr:
        return None

    min_val= arr[0]
    for num in arr:
       if num < min_val:
           min_val= num
    print(min_val)


def find_max_in_an_array(arr):
    if not arr:
        return None

    min_val = arr[0]
    for num in arr:
        if num > min_val:
            min_val = num
    print(min_val)





lst=[2,5,10,98,7,45]
find_max_in_an_array(lst)
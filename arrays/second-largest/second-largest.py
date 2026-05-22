def get_second_largest(arr):
    largest = 0
    second_largest = 0
    for num in arr:
        if largest < num:
            second_largest = largest
            largest = num

        if second_largest < num < largest:
            second_largest = num

    if second_largest == 0:
        return -1
    else:
       return second_largest


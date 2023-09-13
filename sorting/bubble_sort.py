# Write a program to implement bubble sort
unordered_list = [6,5,3,1,8,7,2,4]

# Method-1
for i in range(len(unordered_list)):
    for j in range(i):
        if unordered_list[j] > unordered_list[j + 1]:
            unordered_list[j], unordered_list[j + 1] = unordered_list[j + 1], unordered_list[j]
print(unordered_list)


# Method-2
def bubble_sort(arr: list) -> list:
    swapped = False
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if not swapped:
                return
    return arr

print(bubble_sort(unordered_list))
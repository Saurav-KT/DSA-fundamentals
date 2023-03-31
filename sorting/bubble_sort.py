# Write a program to implement bubble sort
unordered_list = [30, 20, 45, 17, 38, 78]

# Method-1
for i in range(len(unordered_list) - 1):
    for j in range(len(unordered_list) - 1):
        if unordered_list[j] > unordered_list[j + 1]:
            unordered_list[j], unordered_list[j + 1] = unordered_list[j + 1], unordered_list[j]
print(unordered_list)


# Method-2
# def bubble_sort(arr: list) -> list:
#     swapped = False
#     for i in range(len(arr) - 1):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 swapped = True
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             if not swapped:
#                 return
#     return arr

# print(bubble_sort(unordered_list))
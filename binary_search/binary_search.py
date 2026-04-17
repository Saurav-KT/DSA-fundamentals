# elements and sequence should be in sorted order

# def binary_search(arr:list, element:int):
#     low =0
#     high= len(arr)-1
#     while low<= high:
#         mid= (low+high)//2
#         if arr[mid]== element:
#             print("element found at ", mid+1)
#             break
#
#         elif arr[mid] > element:
#             high= mid-1
#         else:
#             low= mid+1
#     else:
#         print(element ,"is not found")

# Recursion approach
def binary_search(arr,low,high,element):

    if low<=high:
        mid = (low + high) // 2
        if arr[mid]==element:
            print("element found at", mid+1)
            return
        elif arr[mid]> element:
                binary_search(arr,low, mid-1, element)
        else:
            binary_search(arr,mid+1,high,element)
    else:
        print(element, "not found")



input_arr=[17, 19, 21, 23, 25, 27, 29, 31]
binary_search(input_arr, low=0, high=len(input_arr)-1, element=25)



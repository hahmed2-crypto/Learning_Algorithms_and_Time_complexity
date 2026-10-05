def linear_search(my_list, target):
    """
    returns the index position of the target if found, else returns None
    """

    for i in range(0, len(my_list)): # This loop or iteration is gone through the whole length of the list from index 0 to the lenght of the list.
        if my_list[i]==target:
            return target
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

list_numbers= [2,3,4,5,6,7,1,8,9]
result= linear_search(list_numbers, 10)
verify(result)

result= linear_search(list_numbers, 8)
verify(result)

result= linear_search(list_numbers,3)
verify(result)

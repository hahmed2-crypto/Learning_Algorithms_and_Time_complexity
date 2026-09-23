def binary_search(list, target):
    left=0
    right=len(list)-1 

    while left <= right:
        midpoint= (left+right)//2
        if list[midpoint]==target:
            return midpoint
        elif list[midpoint] < target:
            left= midpoint + 1
        else:
            right= midpoint -1
            
    return None

list_numbers= [1,2,3,4,5,6]

result=binary_search(list_numbers,2)

print(result)
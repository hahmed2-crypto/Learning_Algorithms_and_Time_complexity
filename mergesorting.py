list= [2,1,6,4,7,9,0,3,8,5]
def merge_sort(list):
    if len(list)<=1:
        return list
    m= len(list)//2
    a= merge_sort(list[:m])
    b=merge_sort(list[m:])
    r= []

    while a and b:
        if a[0]<= b[0]:
            r.append(a.pop(0))
        else:
            r.append(b.pop(0))
    return r + a + b

print(merge_sort(list))

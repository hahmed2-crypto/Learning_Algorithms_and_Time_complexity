my_list= [1,2,3,4]


for i in my_list:
    if i == 2:
        print(True+ my_list[3])
    else:
        print("nothin is here")


list= []
list.append(2)
list.extend([5,6,7,8,9,])
print(list)

list.pop(3)# it is removing at the index not the number itself.
print(list)
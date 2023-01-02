list1 = [1,3,6,8,0,2,6]
print("list1: ",list1)
list1.append(23) #Add a single element to the end of the list
print("append : ",list1)
list1.clear() #Removes all Items from the List
print("clear : ",list1)
list2 = [6,7,9,0,3,2]
print("list2 : ",list2)
list3 = list2.copy()
print("copy - list3 : ",list3)
print("count : ",list3.count(9))
print("pop : ",list3.pop(0))
list3.remove(3)
print("remove : ",list3)
list3.reverse()
print("reverse : ",list3)
list3.sort()
print("sort : ",list3)



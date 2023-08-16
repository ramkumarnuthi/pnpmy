list1 = ["sai", "liki" , "ram"]
list2 = ["bravo", "honey", "pandu"]
list3 = list1 + list2
print(list3)


list1 = [11, 5, 17, 18, 23]
total = sum(list1)
print("Sum of all elements is : ", total)


list1 = [12, 20, 0, 45, 66, 99, 111]
for num in list1 :
    if num % 2 == 0:
        print(num)
    
    
list1 = [12, 20, 45, 66, 99, 111]
for num in list1 :
    if num % 2 != 0 :
        print(num)    
        
        
list1 = ["ram","liki","sai","bravo","pandu"]        
index = 3 
del list1[index]
print(list1)  
        
        
list = ['cheers', 'vamos', 'sad', 'drowsy']
list.insert(1, "energy")
print(list)


list1=["ram","akhil","sai"]
newlist = input("enter a name :")
list1.append(newlist)
print(list1)


list1 = [1,2,3,4]
list2 = [1,2,3,5,4]
list1.sort()
list2.sort()
if list1 == list2:
    print("THE LISTS ARE IDENTICAL")
else:
    print("THE LISTS ARE NOT IDENTICAL")

        
        
        
        







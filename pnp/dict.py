dict= {0:10, 1:20}
dict.update({2:30})
print(dict)

dict = {'1': 'ram', '2': 'pandu', '3': 'sai'}
for key, value in dict.items():
    print(key, value)
    
    
dict={}
for x in range(1,16):
    dict[x]=x*x
print(dict)  
 


str1 = 'marolix technology' 
dict = {}
for letter in str1:
    dict[letter] = dict.get(letter, 0) + 1
print(dict)

 
dict = {'1':222,'2':567,'3':111, '4':-456}
print(sum(dict.values()))



dict1 = {'a': 100, 'b': 200, 'c':300}  
dict2 = {'a': 300, 'b': 200, 'd':400} 
dict3= {}  
dict3.update(dict1)  
dict3.update(dict2)  
for i,j in dict1.items():  
    for x,y in dict2.items():  
        if i ==x:  
            dict3[i] = j+y  
print(dict3) 

num = {'physics': 99, 'math': 100, 'chemistry': 99}
print(list(num)[0])
print(list(num)[1])
print(list(num)[2])
 
 
dict = {'a':1,'b':2,'c':3,'d':4}
if 'a' in dict: 
    del dict['a']
print(dict)     

 
dict1 = {'a': 100, 'b': 200}
dict2 = {'x': 300, 'y': 200}
dict1.update(dict2)
print(dict1)

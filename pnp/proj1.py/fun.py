string='The quick Brow Fox'
upper=0
lower=0
for i in string:
      if(i.islower()):
            lower=lower+1
      elif(i.isupper()):
            upper=upper+1
print("The number of lowercase characters is:",lower)
print("The number of uppercase characters is:",upper)


list =[1,2,3,3,3,3,4,5]
def unique_list(l):
  x = []
  for i in list:
    if i not in x:
      x.append(i)
  return x
print(unique_list(list))



string = "The quick brown fox jumps over the lazy dog"
def ispangram(string):
    alphabets ="qwertyuiopasdfghjklzxcvbnm"
    for char in alphabets :
        if char not in string.lower():
            return False
    return True
if (ispangram(string)==True):
    print("this is a pangram string")
else:
    print("this is not a pangram string")
    
    
    
def function(n): 
    list1=[] 
    for i in range(1,11): 
        a=i*i 
        
    print(list1) 
function(10)

 
list = [8,2,3,0,7]
def sumoflist (*n) :
    total = sum(list)
    print(total)
sumoflist()


def add_num(*args):
   sum = 0
   for num in args:
      sum += num
   return sum
result = add_num(1, 2, 3)
print('Sum is', result)
result = add_num(10, 20, 30, 40)
print('Sum is', result)
result = add_num(5, 6, 7, 8, 9)
print('Sum is', result)

        


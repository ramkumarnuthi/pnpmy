s = 'virender sehwag'
print(s.replace('a', ''))

string=input("Enter string:")   
revstr ="" 
for i in string: 
    revstr=i+revstr 
print("Reversed string:",revstr)
if(string==revstr):
    print("The string is a palindrome.") 
else: 
    print("The string is not a palindrome.") 


character=input("enter a character :")
vowels=("a,e,i,o,u,A,E,I,O,U")
if character in vowels:
    print("the  given character is vowel")
else:
    print("the given character is consonant")
    
    
    string="viru maxi warner smith"
    ch="-"
    string=string.replace(" ",ch)
    print(string)
    
    
    

string = input("Enter a String : ")
alphabets=0
digits=0
specialChars=0
for i in string: 
    		if i.isalpha():
       			 alphabets+=1
    		elif i.isdigit():
        			digits+=1
    		else: 
        			specialChars+=1
print("alphabets =",alphabets,"digits =",digits,"specialChars =",specialChars)



str1="every one is like a demon"
str2=str1.replace(" ","")
print(str2)




String = "1234566789"
sum1 = 0
for i in String:
    if ord(i) >= 1 and ord(i) <= 10:
        sum1 = sum1 + int(i)
print('Sum is :' + str(sum1))


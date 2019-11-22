'''1'''##Make a calculator using Python with addition , subtraction , multiplication ,
##division and power.
def ADD(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)    
def SUB(*args):
    sub=0
    for i in args:
        sub-=i
    print(sum)
def MUL(*args):
    mul=0
    for i in args:
        mul*=i
    print(mul)
def DIV(*args):
    div=0
    for i in args:
        div/=i
    print(div)
'''2'''## Write a program to check if there is any numeric value in list using for loop    
l=['a','1','c','3']
n=0
for  i in l:
    
    if i.isdigit():
        i=int(i)
        n+=i
        print(i,'is num')
print(n)    
##'''3'''. Write a Python script to add a key to a dictionary        
d={1:'1',2:'2'}
key=input('enter a key')
value=input('enter a value')
d[key]=value
##'''4.''' Write a Python program to sum all the numeric items in a dictionary
dic={1:'A',2:'b','c':3}
x=list(dic.keys())
y=list(dic.values())
l=x+y
sum=0
for i in l:
    if type(i)==int:
        sum+=i
print(sum)
##5. Write a program to identify duplicate values from list
l=[1,2,3,2,4,4,5]
for y in range(len(l)):
    for z in range(y+1,len(l)-1):

        if l[y]==l[z]:
            l.pop(z)
print(l)
##6. Write a Python script to check if a given key already exists in a dictionary
dic={1:'A',2:'b',3:'c',2:'d'}
key1=list(dic.keys())
print(key1)
for y in range(len(key1)):
    for z in range(y+1,len(key1)-1):
        print('1')
        if key1[y]==key1[z]:
            print('duplicate exist of key',key1[y])

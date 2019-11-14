'''1'''##Write a program which takes 5 inputs from user for different subject’s
##marks, total it and generate mark sheet using grades ?
subj1=float(input('enter your subj1 marks out of 100:'))
subj2=float(input('enter your subj2 marks out of 100:'))
subj3=float(input('enter your subj3 marks out of 100:'))
subj4=float(input('enter your subj4 marks out of 100:'))
subj5=float(input('enter your subj5 marks out of 100:'))
totalmarks=subj1+subj2+subj3+subj4+subj5
print('You obtained',str(totalmarks),'out of 500')
if totalmarks==500:
    print('You got A+')
elif 450<=totalmarks<500:
    print('you got A')
elif 300<=totalmarks<450:
    print('you got B')
elif 200<=totalmarks<300:
    print('You got C')
else:
    print('You got D')
'''2.'''##Write a program which take input from user and identify that the given
##number is even or odd?
num=int(inpt('enter any number'))
if num%2==0:
    print('your given no is even')
else:
    print('the no is odd')
'''3'''##Write a program which print the length of the list?    
l=[1,2,3,4,5]
count=0
for i in l:
    count+=1
print(count)    
'''4'''##Write a Python program to sum all the numeric items in a list?
l1=[1,2,3,4,5]
sum=0
for i in l1:
    sum+=i
print(sum)
'''4'''##Write a Python program to get the largest number from a numeric list.
l2=[1,3,4,5,6]
largest=l2[0]
for i in range(len(l2)):
    if l2[i]>largest:
        largest=l2[i]
print(largest)
'''5'''##Take a list, say for example this one:
##a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##and write a program that prints out all the elements of the list that are
##less than 5.
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i<5:
        print(i)
    

    
    

##Write a Python program to print the following string in a specific format
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
##Write a Python program to get the Python version you are using.
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
##Write a Python program to display the current date and time.. 
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

##Write a Python program which accepts the radius of a circle from the user and compute the area.
radius=int(input('enter the radius'))
area=4*3.142*radius**2
print(area)
##Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
firstname=input('Enter your first name')
lastname=input('Enter your last name')
print(lastname + ' ' + firstname)

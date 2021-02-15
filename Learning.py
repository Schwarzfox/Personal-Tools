###BASIC OPERATIONS###
print ("B A S I C S :")
my_num = 5
str(my_num)
print(pow(2, 3))
print(max(4, 10))
print(round(3.5))

from math import *

print(floor(2.9))
print(ceil(2.9))
print(sqrt(22))

# your_name = raw_input ("enter your name here:") #Gets the input from userer
# print(your_name+" is bad")

###LISTS###
print ("L I S T S:")
my_list = [1, 3, 5, 100, 200, 800, 9000, -21, 6, 6, 100, "hoyoyo"]
name_list = ["Ad", "BC", "CD"]
# print(my_list[0])
# print(my_list[-1])
# print(my_list[2:])
# my_list[2]= "Gowje"
# print(my_list[1:4])

my_list.extend(name_list)  # Append a new list to the end
my_list.pop()  # Removes the last element
print(my_list)
# my_list.append("AppendEx!") #Append a new element to the list
# my_list.insert(0,"Start")         #Insert an element to the list, pushes everything one step
# my_list.remove(200)
# print(my_list)
print(my_list.index(100))  # Shows the location of the element 100
print(my_list.count(6))  # Counts how mnay 6 we have
# my_list.sort()                   #Sorts the list
my_list.reverse()
print(my_list)


###Functions###
print ("F U N C T I O N S :")
def say_hi(name, age):
    print("Hello " + name + "! You are " + str(age) + " years old!")
    return age            #return actually breaks the function

say_hi("Seti", 30)
my_age= say_hi("seti",2)
print(my_age)


###IF###
print("I F :")
user_age=15
if user_age<10:
    print("you are a kid")
elif user_age<18:
    print("you are a teenager")
else:
    print("you are an audlt")



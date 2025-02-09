
#import ascii_py
#output = ascii_py.from_image_file("profile.jpg",columns=200,char="#")
#ascii_py.to_terminal(output)


# If statement
jpa = 3
if jpa > 2:
    print("Welcome to the university of Northampton")
else: 
    print("your application is denied.")
    
# For loop
for x in range(1,6):
    print(x,"squared is", x*x)
#single line Loop
Nlist = [x*x for x in range(1,6)]
print("squared x is",Nlist)   
Nlist = [x*x for x in range(1,6) if x%2 == 0]
print("squared x completely dividing 2 is",Nlist) 


#list
myList = []
print(type(myList))
print(len(myList))
list = ['abc',789, 2.5, 'John']
tinyList = [123, 'John']
print(list)
print(list[0])
print(list[0:3])
print(list[2:])
print(list + tinyList)

# Split and Sort functions for String methods
split_list = 'this is just a test'.split()
print(split_list)
sortList = 'y x z a b c' .split()
sortList.sort()
print(sortList)
# tuples
# similar to list but the elements can not be modified
tuple = ('start',87,12,'end')
for T in tuple:
    print(T)
# array
# arrays are homogeneous, while lists are heterogeneous
# Size of array is fixed, whereas lists are dynamic


# numpy
import numpy as np
array = np.array([212,144,224,999])
print (array)
print (type(array))


# 2-dimension 
print("2D array")
arr = np.array([[11 ,22 ,33 ,44 ], [11 ,22 ,33 ,44]])


arr = np.array([[987,422,773,957], [236,144,518,853], [122,344,728,232]])
print(arr)

# 3-dimension array
print("3D array:")
arr = np.array([
    [[144, 223, 312], [144, 526, 689] , [144, 532, 678]],
    [[111, 245, 325], [222, 589, 609] , [333, 325, 116]],
    [[237, 899, 911], [101, 121, 122] , [133, 115, 126]]]      
    )
print(arr)
#Py exercise
print('exercise2:')
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True

# Define the range within which you want to find prime numbers
start = 10
end = 50
# Find and print prime numbers within the specified range
print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)
        
print('exercise3:')
i = int(input('input the number:'))
for j in range(1,i+1):  
    if i%j == 0:
        print('The factors:',int(i / j))
    else:
        continue
#print(div)
#div = [i/j for j in range(i+1)]
#    print(j)             
#Py exercise:
# Pillow
# open CV
    

    
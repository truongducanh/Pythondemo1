import sys

greeting = "Hello Henderson, "
wish = "Have a lovely day"
print(sys.version)

#string and variables
print(greeting + wish)

#operator
x = 8
y = x+2
print(x,y)

#array
numbers = [1,2,3,4,5,6,7,8,9,10]
names = ["Henderson","Aimee","Irving"]


# "in" to check whether the array has that value or not
# append() to add values to the array
# len() is the number of elements in the array

numbers.append(11)
print (10 in numbers)
print (names)
print(numbers)
print(len(numbers))



# if/else statements
a = 1 
if a > 0:
  print ("Python syntax is so simple, compared to another")
else:
  print ("OH, Python is not that simple")


# While and For loop
i = 10
while i < 30:
    print ("this is a brilliant While loop")
    i = i+1
print('For loop:')
social_media = ["Facebook","Instagram","Snapchat"]
for socM in social_media :
  print(socM)
for x in range(2, 30, 3):
  print(x)
# Define a range within which you want:
#start = 1
#end = 100
#for num in range(start, end + 1):
#    if is_prime(num):
#        print(num)
#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

# function
# sum of numbers from 1 to N
def Sum(n):
    summ = 0
    i = 1
    while i <= n:
        summ = summ + i
        i = i + 1 

    return summ 

print(Sum(4))    



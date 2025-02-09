# print 3 elements from  array[0] by ":"
information = [1,2,3,'uk']
print(information[0:3])


#data types: Dictionary 
# dictionary type includes keys and values, placed in '{}'
info2 = {'grade': 4,
         'results':[24,33,45],
         'nationality':['UK'],}
# str() to convert data types to "string"
print('student grade:' + str(info2['grade']))

# logic
comparison = 3 < 4
print(comparison)  

# Loop
# The variable 'n' runs from 1 to 10
for n in range(1,10):
    print(info2)

Number = 2000
for n in range(0,10):
    print(Number)
    Number = Number + 1




#demo fortuneTeller programme
#lower() is a built-in function of Py for Strings
#char() is characters
def fortuneTeller(name1,name2):
    name1 = name1.lower()
    name2 = name2.lower()
    count = 0
    for charac in range(ord('a'), ord('z') +1):
        #print (chr(alphabet))
        # name similarity checking
        # In python: (character 'in' string) to check if that character in the string
        if (chr(charac) in name1) and (chr(charac) in name2):
            count = count+1
        
   
    if count == 0 :
        result = "strangers"
    elif 0<count<3:
        result = "friends"    
    else:
        result =  "matched"

    return result
print(fortuneTeller("duc","zzz"))
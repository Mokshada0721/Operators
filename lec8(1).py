#membership operator:
'''a = "python"
print('y' in a )
print('y' not in a)'''

#identity
'''a = ["python","java"]
b = ["java","python"]
c = a
print(a is c) #there is address/object is different (true)
print(a is b)  #false
print(a is not c)   #false
print(a is not b)    #true'''

#day 8 assessment
'''Suppose you are building a program to check if a person is 
eligible for a discount. 
The person must be either a student or a senior citizen. 
Write logical operator'''

#if he is senior critizen then discount otherwise not eligible
# we can use any one of them
#if person is not senior and not student then diccount not eligible
#age limit
'''age = int(input("Enter the age :- "))

isStundent = (age <= 25)
isSenior = (age >= 65)

if(isStundent or isSenior):
    print("You are Eligible for discount")
else:
    print("You are not Eligible")'''





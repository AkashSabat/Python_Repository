#Numbers in python
from builtins import round

#Add 
print(3+4)
print(type(3+4))
  
#subtract
print(3-4)
  
#Multiplication
print(3*4)
  
#Division
print(8/7)

#Math functions in Python

#Round
print(round(4.9))
print(round(4.5))
print(round(4.1))

#abs
print(abs(-4.5))
 
# #Variable in python 
name = input("What is your name?")
print("Hi "+name)

#Augemented assignment operator
some_value = 5
some_value += 2
print(some_value)


#String
user_name = 'akash'
pass_word = 'secret'
long_string ='''
        WoW
        ---
        '''
print(long_string)
full_name =user_name + ' ' +pass_word
print("Hi  "+full_name)


#Type Conversion
print("Hi"+ str(5))

#Escape characters
weather = "\t It\'s \"kind of\" sunny \n\t hope you have a good day"
print(weather)

#formatted Strings
name = 'Johny'
age = 55
print(type(age))
print("Hello "+name+".you are "+str(age)+' years old')
print(f'Hello {name}.you are {age} years old')

#String indexes
name='akashdjdhfhfh'
print(name[1:5:2])
print(name[1:])
print(name[:1])
print(name[::1])

#Immutability Concept
name ='hjdhdshdud'
#name[1]='l'
print(name)

#Exercise

#question is find your age
birth_year = int(input("What year were you born?")) 
print(type(birth_year))
print(birth_year)
age = 2020-birth_year
print(type(age))
print(age)
print(f" Your are {age} years old ")






first = input("First num: ")
second = input("Second num: ")
sum = float(first) + float(second)
print("Sum: "+ str(sum))
print("Sum: ",sum)

course = "Python for Beginners"
print(course.upper())
print(course.lower())
print(course.find('y'))
print(course.find('for'))
print(course.replace('for','4'))
print(course)

print('Python' in course)

weight = input("Weight: ")
lk = input("(K)g or (L)bs")
if lk.upper()=='K':
    converted = float(weight) / 0.45359
    print("Weight in lbs:", converted)
elif lk.upper()=='L':
    converted = float(weight) * 0.45359
    print("Weight in kg: ", converted)
else:
    print("Invalid input")

i = 1
while i<10:
    print(i*'*')
    i += 1

names = ["John", "Sam", "Mosh", "Allen"]
print(names[1])
print(names[0:3])
names.append("Anna")
print(names)
names.insert(0,"Bob")
print(names)
names.remove("Sam")
print(names)
print("Mosh" in names)
print(len(names))
names.clear()

for item in names:
    print(item)

i=0
while(i<len(names)):
    print(names[i])
    i +=1

numbers = range(5)
numbers = range(5,10,2) #start,end,jump
print(numbers)
for number in numbers:
    print(number)
for number in range(5,10,2):
    print(number)

numbers = (1,2,3)  #tuple

#FORMATTED STRING ----------------------------------
first = 'John'
last = 'Smith'
msg = f'{first} [{last}] is a coder'

#CAR GAME -------------------------------------------
command = ""
started = False
while True:
    command = input("> ").lower()
    if(command == "start"):
        if started:
            print("already started")
        else:
            started = True
            print("car started")
    elif(command == "stop"):
        if not started:
            print("already stopped")
        else:
            started = False
            print("car stopped")
    elif(command == "help"):
        print("""
start -> to start car
stop -> to stop car
quit -> to end 
        """)
    elif (command == "quit") :
        break

#EXCEPTION--------------------
try:
    age = int(input("Enter age"))
    income = 20000
    risk = 20000/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid value")

#CLASS-------------------------
class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John Smith")
john.talk()

#random----------------------------------------

import random
for i in range(3):
    print(random.random())
    print(random.randint(10,20))

members = [bob, cat, matt, abel]
leader = random.choice(members)

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second

a = Dice()
print(a.roll())
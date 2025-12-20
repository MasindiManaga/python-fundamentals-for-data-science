#----------------------------------
#Lession 1 - Variable and Basic Types

"""
1. What is a variable?
- It is a name or label
- It points to a value somewhere in memory
- That value has a type

Variables reference objects!!! [Specific to python]

Example:
x = 10
→ 10 is an integer object that is stored in memory.
→ x is the label pointing to the object.

If you change the value from 10 to 20, in python it simply makes
x reference to a different object in memory.


2. Data types - The Pillars

Numeric types:
 - int: whole numbers
 - float: decimals
 - complex: real and imaginary numbers

Example:
 a = 7
 b = 3.14
 c = 2 + 5j

 Text type:
 - str: string (sequence of characters)

Example:
 name = "Masindi"

 Boolean type:
- bool: true or false

Example:
is_done =  False

Special type:
- NoneType: None (represents empty object)

Example:
result = None

3. Immutability vs Mutability:

Immutable types (cannot change):
- int
- float
- str
- bool
- tuple

When you "modify" an immutable object, Python actually creates a new one.

Mutable types (can change):
- list
- dict
- set

Example:
→ x = 10
→ x += 1 ...new int object is created
=> 11

vs

nums = [1,2,3]
nums.append(4) ...modifies existing list
=> nums = [1,2,3,4]

4. Inspecting types

=> Use type() to ask python what an object really is

Example:
x = 10
print(type(x)) ... <class 'int'>
print(type(3.14)) ... <class 'float'>
print(type("Hi")) ... <class 'str'>

5. Printing & Output Formatting :

Python prints using the print() function

Example:
Basic printing:
-> print("Hello world")

Print multiple values:
-> print("Age:", 21, "Height:", 1.65)

F-strings:
name = "Masindi"
age = 21

print(f"Hello, {name}. You are {age} years old")


6. Memory and Identity:
Every python object:

- a value (what it stores)
- a type (what kind of thing it is)
- an identity (location in memory)

Inspect identity with id():
a = 10
b = 10
print(id(a), id(b))

"""

#Coding starts below ⇩
print("===Printing and Output formating===")
x = "Hello"
print(type(x))
print (type(2.15))
print(type(2))

#Memory and Identity
a = 10
b = 10
print(id(a), id(b))

print("\n")

print("===Exercise A - variables ===")

#variables
name = "Masindi"
birth_year = 2004
present_year = 2025
is_student = True


#calculations
age = present_year - birth_year

#f-string
print(f"Hi, I am {name}. I was born in the year {birth_year} and this is the year {present_year}, can you guess my age? I am {age}")

#multiple lines
print(name, birth_year, present_year, is_student)

print("\n")


print("===Exercise B -Types===")

c = 10
d = 10.0
f = True
g = None

print(type(c))
print(type(d))
print(type("10"))
print(type(f))
print(type(False))
print(type(g))

print("\n")

print("===Exercise C- Reassignment===")
x = 5
print("1st assignment:", x)
x = x + 3
print("2nd assignment:", x)
x = "Now I am a string"

print(x)

"""This is possible because python is dynamically typed. Variables don't have a fixed data type, they point to objects of different types as needed."""

print("\n")

print("===Exercise D- Identity===")

x = 1000
y = 1000

print(type(x), type(y))
print("\n")


#My Playground -------------------
print("===PROJECT 1 — “Student Identity Card Generator”===")
"""
Prints a realistic student card layout
"""

object_name = "Campus Card Student"
name = "Masindi"
surname = "Managa"
qualification_id = "Bsc IT DS"
student_no = "EDUV4840983"
barcode_student = "| |||||| || || | | ||| |||| || |"

print(f"""
object {object_name} 
name:  {name}
surname: {surname}
qualification: {qualification_id}
student_no: {student_no}
barcode: {barcode_student}
""")

print("\n")

print("===PROJECT OPTION 2 — “Age & Life Stats Calculator”")
"""
Calculates your age and how long you have been on earth.
"""

#calculator for age
pres_year = int(input("What is the year today?"))
bir_year = int(input("What is your birth year?"))

individual_age = pres_year - bir_year

#calculator for life
months = individual_age * 12
days = individual_age * 365

print(individual_age)
print(f"You have lived for {months} months and {days} number of days")

print("\n")

print("===Project 3: ID Card===")

title = "Republic of South Africa National Identity card"
surname = "Smith"
name = "Sam"
sex_symbol = "M"
nationality = "RSA"
id_no = 32415243628383238
dob = "12 Jan 1993"
birth_country = "RSA"
status = "citizen"

print(f"""
title: {title}
surname: {surname}
name: {name}
sex: {sex_symbol}
nationality: {nationality}
id_no: {id_no}
dob: {dob}
birth_country: {birth_country}
status: {status}
""")

print("\n")

print("===PROJECT OPTION 3 — “Python Object Inspector”===")
"""A fun tool: you assign values and print their type and identity (memory address).
This helps deepen your understanding of Python’s data model."""

black = "black"
num = 1
is_child = True
r = [1,2,3,4]
o = None
com_num = 2 + 5*num

print(type(black), id(black))

print(type(12.46), id(12.46))
print(type(num), id(num))
print(type(is_child),id(is_child))
print(type(r), id(r))
print(type(o), id(o))
print(type(com_num), id(com_num))
print("\n")
"""Types can be used for debugging"""

print("===FINAL PROJECT FOR THIS LESSON===")
print("Personal Profile System v1.0")
"""A personal profile system is a very small, beginner-friendly software idea whose purpose is to represent a person in a structured way using data, and then present that data meaningfully.

Think of it as the digital equivalent of a paper profile — not a database yet, not an app yet — just a program that knows who someone is."""

full_names = input("What is your full name?")
present_age = input("How old are you?")
id_number = int(input("What is your id?"))
job_des = input("What is your job?")

print(f"""
full_names: {full_names}
present_age: {present_age}
id_number: {id_number}
job_des: {job_des}
""")
#--------------------------
"""
Lesson 2 - Operators and Input

Everything here revolves around expressions:
- Inputs → processed by operators → outputs

1. Input: how programs talk to humans
What input() really does

example:
value = input('Prompt: ')

→ pauses the program
→ displays a message
→ waits for the user to type
→ returns text a 'str' - always

even if the user types:
42

python receives:
"42" ...a string not a number

2. Type conversion - teaching Python meaning

converting input:
age = int(input("How old are you?"))

→ input() ...returns a string
→ int() ....converts the string to a number

Core conversions:
int() ...whole numbers
float() ...decimal numbers
str() ...text
bool() ...true or false, 1 or 0

3. Operators - the language of logic and math
=> they are verbs for data.

Arithmetic operators:
+ ... add
- ...subtract
* ...multiply
/ ...divide (always float)
// ...floor division/ integer division
% ...remainder/ mod
** ...power

Why % matters:
it lets you answer questions like:
- is a number even?
- does something fit evenly?
- is an ID divisible by something?

example:
10 % 2 == 0 # even

Comparison operators:
== ...equal?
!= ...not equal?
< ...less than?
> ...greater than?
<= ...less or equal?
>= ...greater or equal?

example:
age = 20
age >= 18 #True

5. Boolean logic - combining decisions
and ...both must be true
or ...at least one true
not ...flip value

example:
age >= 18 and has_id
 => Age is at least 18 and has an ID.


6. Expressions - the real mental model
=> anything python can evaluate to a value.

Examples:
10 + 5
age >= 18
(x + y) * 2

Python:
-Evaluates expressions
-Produces a result
-Assigns or uses the result

7. Operator precedence (order matters)
1. Parenthesis
2. Powers
3. Multiply/ Divide
4. Add/ Subtract
5. Comparisons
6. Logical operators

example:
10 + 2 * 3 # 16 ...BODMAS

Use parenthesis for clarity 10 + (2 * 3)



"""

#---------------------------
print("===Code starts here====")
#Examples
total = 10 + 3
remainder = 10 % 3

print(total, remainder)

print("===Project 1: Decision based profile system===")
"""
A decision-based profile system that:
-Asks for values
-Converts them
-Performs comparisons
-Produces meaningful output
"""

value_1 = int(input("Please enter a value: "))
value_2 = int(input("Please enter a value: "))
comparisons = value_1 >= value_2

print(comparisons)
print("\n")

print("===Project 2: Access Eligibility Checker===")
"""This system determines whether a person is allowed access to something (a building, service, or event) based on conditions.

The program’s responsibility is to:
- Collect information from a user
- Interpret that information correctly
- Evaluate logical conditions
- Produce a clear decision outcome
"""

#data collection for event
guest_age = int(input("How old are you?"))
guest_id = (input("Do you have your id? (Use capital letter Y or N)"))

if guest_age >= 18 and guest_id == "Y":
    print("You may enter")
else:
    print ("You may not enter.")


print("\n")

print("===Project 3: Personal Expense Reasoner===")
"""
This system takes financial information and produces reasoned feedback, not just calculations.
It doesn’t manage money — it interprets it.

The program:
- Accepts numeric inputs related to money
- Performs calculations
- Compares values
- Explains the outcome in plain language
"""

#calculate my balance after each purchase
balance = float(input("Please enter the balance in your account: "))
purchase_price = float(input("How much did you spend? "))

remaining_balance = balance - purchase_price

if remaining_balance < 1000:
    print(f"You are on a low balance: {remaining_balance}")
else:
    print(f"You are on a good balance: {remaining_balance}")
print("\n")
"""
Lesson 2: Operators and Input

This lesson focuses on how Python evaluates expressions by combining:
- User input
- Type conversion
- Operators
- Boolean logic

The goal is to understand how raw input becomes
meaningful decisions in a program

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

#Examples
total = 10 + 3
remainder = 10 % 3

print(total, remainder)

# Project 1: Decision based profile system
def run_value_comparison():
    value_1 = int(input("Please enter a value: "))
    value_2 = int(input("Please enter a value: "))
    result = compare_values(value_1, value_2)
    print(result)

def compare_values(value_1: int, value_2: int) -> bool:
    """
       Compares two integer values and returns True
       if the first is greater than or equal to the second.
       """
    return value_1 >= value_2

print("\n")

# Project 2: Access Eligibility Checker

def run_access_checker():
    guest_age = int(input("How old are you? "))
    guest_id = input("Do you have your ID? (Y/N):")

    if is_eligible_for_access(guest_age, guest_id):
        print("You may enter")
    else:
        print("You may not enter")

def is_eligible_for_access(age: int, has_id: str) -> bool:
    """
    Determines access eligibility based on age and ID possession.
    """
    return age >= 18 and has_id == "Y"

print("\n")

# Project 3: Personal Expense Reasoner
def run_expense_reasoner():
    balance = float(input("Please enter your account balance: "))
    purchase_price = float(input("How much did you spend? "))

    remaining_balance = evaluate_balance(balance, purchase_price)

    if remaining_balance < 1000:
        print(f"You are on a low balance: {remaining_balance}")
    else:
        print(f"You are on a good balance: {remaining_balance}")

def evaluate_balance(balance: float, purchase_price: float) -> float:
    """
    Calculates remaining balance after a purchase.
    """
    return balance - purchase_price

if __name__ == "__main__":
    run_value_comparison()
    # run_access_checker()
    # run_expense_reasoner()
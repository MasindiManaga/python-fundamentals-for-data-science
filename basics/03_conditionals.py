#--------------------
"""
Lesson 3 - Conditionals and Decision-Making

Conditionals are the decision engine of all software:
- Games
- Elevators
- Banking systems
- AI logic
- User interfaces

1. What a conditional reality is (mental model)
A conditional is:
- a question
- that evaluates to true or false
- and determines which block of code runs

The program does not “understand meaning” — it only reacts to truth values.

2. The 'if' statement - one decision

if condition:
    # code runs only if condition is True

Example:
if temperature > 30:
    print("It's hot")

3. else - the fallback path

if condition:
    do_this
else:
    do_that

This guarantees:
- One path will run
- The program always has a defined outcome

Think of 'else' as:
"if everything above failed."

4. elif - multiple competing paths

if condition_1:
    path_1
elif condition_2:
    path_2
else:
    fallback
"""
#---------------------

print("""===Project 1: Role Classification System===""")
#A system that classifies a person into one role based on rules.

role = input("What is your role in a department?(one word ans) ->>").lower() #makes input case-sensitive

if role == "hire":
    print("Your role is HR")
elif role == "calculate":
    print("Your role is Finance")
elif role == "market":
    print("Your role is Marketing")
else:
    print("Unable to assign you a role, contact the company!")

print("\n")

print("""===Project 2: Smart Feedback Generator===""")
#A program that gives feedback based on performance ranges.

is_student = input("Are you a student? (Y/N)->>").lower().strip()
#.strip() ...removes accidental spaces

if is_student == "y":
    print("Proceeding to evaluation:")
    performance = int(input("What is your grade average? "))

    if performance < 50:
        print("Pull up your socks!")
    elif performance <=70:
        print("You can do better than this.")
    elif 0<= performance > 100:
        print("Invalid range!")
    else:
        print("You are a star- Keep it up!")
else:
    print("Cannot evaluate your performance.")


print("\n")


print("""===Project 3: Simple Elevator Decision Logic===""")
#A system that decides what an elevator should do based on state.

num = 0
num += 1







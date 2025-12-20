#----------------------
"""
Lesson 4 - Loops and repetition thinking

Loops are about control over repetition.

1. Why loops exist(real reason)
without loops:
- programs run once and stop
- every repeated action must be rewritten
- systems like elevators, games, and apps are impossible

with loops:
- programs stay alive
- decisions are re-evaluated
- state changes over time

!Loops are the heartbeat of software

2. Two loop families in python:
- 'while' ...repeat while a condition is true.
- 'for' ...repeat for each item in a sequence.

They solve different mental problems.

3. 'While' loops - condition-controlled repetition
Mental model
A 'while' loop asks:
    "Should I keep going?"

It:
- Checks a condition
- Runs the body if True
- rechecks the condition
- stops when false

This makes 'while' loops ideal for:
- Waiting
- Monitoring
- user-driven systems
- elevator logic
- games

4. The danger of infinite loops (Important):
A loop that never becomes False never ends.

This happens when:
- The condition never changes
- The variable controlling it isn't updated

Good loop design always answers:
    "What makes this stop?"

5. 'for' loops - sequence-controlled repetition
Mental model
A 'for' loop asks:
    "What do I need to do for each item  in this group?"

It:
- Takes items one by one
- Stops automatically at the end

This makes 'for' loops ideal for:
- Lists
- Ranges
- Text
- Data processing

6. range() - controlled counting
range() ...generates numbers on demand, not all at once.

It defines:
- a start
- a stop (exclusive)
- an optional step

Key idea:
range () ... describes how to count, not a list of numbers.

This is why it works efficiently.

7. Loop variables are temporary
In:
- for x in range(5):

x:
- Exists only to represent the current iteration.
- Changes value each cycle.
- Should not control loop logic unless intentional.

This prevents accidental coupling.
If changing one thing forces you to change many other things, your code is tightly coupled.
If you can change one thing without breaking others, your code is loosely coupled.

"Coupling is about dependency strength."

8. Loop control keywords (decision inside repetition)
'break'
    "Stop the loop immediately."

Used when:
- A condition is met early.
- Continuing is pointless or unsafe.

'continue'
    "Skip the rest of this cycle and move on."

Used when:
- One case should be ignored.
- The loop should keep running.

9. Nested loops
A loop inside a loop means:
- The inner loop runs fully for each outer cycle.

This can explode in runtime.

Mental rule:
One loop = repetition
Two loops = combinations

Use sparingly and intentionally.

10. Loops + conditionals = real systems
Most real programs look like:
- Loop  →  check state
- If condition → act
- Else  →  wait or adjust
- Repeat

This is the structure of:
- Elevators
- Menus
- Games
- Chatbots
- Operating systems

11. Loop design checklist
Before writing a loop, answer:
- What starts the loop?
- What keeps it going?
- What stops it?
- What changes each cycle?
- What must never happen?

"""


print("===Project 1: Menu-Based System===")
print("\n")

#menu and menu selection
while True:
    print("Menu: Appetizers")
    print("1. Coke")
    print("2. Fanta Orange")
    print("3. Sprite")
    print("4. Granadilla")
    print("5. Stone")
    print("6. Exit")

    appetizers = input("Which appetizer would you like?")

    if appetizers == "1":
        print("Coke\n")

    elif appetizers == "2":
        print("Fanta Orange\n")

    elif appetizers == "3":
        print("Sprite\n")

    elif appetizers == "4":
        print("Granadilla\n")

    elif appetizers == "5":
        print("Stone\n")

    elif appetizers == "6":
        print("Exiting the menu\n")
        break

    else:
        print("No option picked!")
        break

print("\n")


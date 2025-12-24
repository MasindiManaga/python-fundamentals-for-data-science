#--------------------------------------
"""
Lesson 6 - Functions (Expanded, System Thinking)

1. What a function really is
A function is:
- A named block of logic
- That performs one responsibility
- Can receive information
- Can return a result
- Can be reused safely

Think of a function as:
A small machine inside a bigger machine.

You don't care how it works once you trust it, only:
- What it needs
- What it gives back
- What it guarantees

2. Why do functions exist?
Functions solve three deep problems:

a. Repetition
Avoid writing the same logic again and again.

b. Complexity
Break big problems into understandable pieces.

c. Repetition
Separate what happens from where it is used.

Real systems collapse without functions.

3. Functions as contracts
Every function is a contract:
"If you give me X, I promise to give you Y."

This means:
- Inputs must be expected.
- Outputs must be predictable.
- Side effects must be intentional.

!!!If you can't explain a function in one sentence, it's doing too much.

4. Parameters vs arguments
- Parameter  → placeholder inside the function
- Argument  → actual value passed in

Why this matters:
You are separating definition from use.

This supports reuse and testing.

5. Return values - the heart of functions
A function should:
- Do work
- Produce a result
- Hand control back

Key insight:
'return' sends data back and ends the function immediately.

This allows:
- Composition (functions using other functions)
- Decision-making based on results
- Clean flow of logic

Printing is not returning

6. Printing vs returning
Printing:
- Shows information to the user
- Is side effect driven
- cannot be reused by logic

Returning:
- Sends data back to the program
- Enables decision-making
- Supports composition

Rule of thumb:
Functions should return values, not print them - unless they exist purely for output.

This reduces coupling.

7. Scope - where variables live
Variables have scope:
- Local (inside function)
- Global (outside)

Key rule:
Functions should not depend on globals unless explicitly designed to.

Why?
- Predictability
- Testability
- Safety

Functions create safe bubbles.

8. Default parameters (controlled flexibility)
Defaults allow:
- Optional behavior
- Safer calls
- Cleaner APIs

But:
- Defaults should be simple.
- Never use mutable objects as defaults.

This is a subtle but critical rule.

9. Function composition (system emerge here)
Functions shine when they work together.

One function:
- Gets data
Another
- Processes data
Another
- Decides outcomes

This is how:
- Pipelines
- Engines
- Simulations
- Business logic
are built.

10. Single responsibility principle
A function should:
- DO one thing
- Do it well
- Do it completely

if you say "and" while describing a function:
 → split it.

This keeps the logic clean.

11. Coupling and functions
Bad coupling:
- Function modifies things it didn't receive
- Function prints + returns + mutates state
- Function relies on hidden globals

Good coupling:
- Inputs are explicit
- Outputs are explicit
- Side effects are documented

Teaching-level insight:
Functions reduce chaos when designed properly.

12. Functions and trust
Once tested, a function becomes trusted infrastructure.

You stop thinking about:
- Loops inside it
- Conditions inside it

You think about:
What does this function give me?

That's abstraction.

13. Functions and testing
Functions:
- Can be tested independently
- Can be reused safely
- Can be reasoned about logically

This prepares you for:
- Debugging
- Automation
- Data Science pipelines
- Software engineering

Before functions:
I write steps.

After functions:
I design behaviors.
"""
#----------------------------------------
"""
Create a function that, when given two positive integers a b,
returns the string "a" if integer a took fewer steps to reach 1
than b when passed through the Collatz sequence, or "b" if
integer b took fewer steps to reach 1 than a.
"""

def collatz_counter(num):

    steps = 0

    while num > 1:

        num = (num/2) if num%2 == 0 else (num*3 + 1)
        steps += 1

    return steps

def collatz(a,b):

    num_a = collatz_counter(a)
    num_b = collatz_counter(b)

    return "a" if num_a < num_b else "b"

print(collatz(10,15))
print(collatz(13,16))
print(collatz(53782, 72534))

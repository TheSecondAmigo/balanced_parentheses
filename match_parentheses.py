#!/usr/bin/env python3

"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.

You're given a string consisting solely of (, ), and *.
* can represent either a (, ), or an empty string.
Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.

"""

def matchparen(string):
    stack = list()

    for ch in string:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if len(stack) == 0:
                return False
            if stack[-1] == "(":
                stack.pop()
            else:
                # '*' could also be a ')', so we can't pop on it
                stack.append(ch)
        elif ch == "*":
            stack.append(ch)

    if len(stack) == 0:
        return True

    lcount = stack.count("(")
    rcount = stack.count(")")
    starcount = stack.count("*")
    count = starcount - abs(lcount - rcount)
    return  count >= 0


if __name__ == "__main__":

    tests = [("(()*", True), ("(*)", True),
             (")*(", False),
             ("((((*)**)*", True),
             ("(**()))", True)
            ]

    for string, exp in tests:
        rc = matchparen(string)
        print(f"string = {string}, exp = {exp}, rc = {rc}, {exp == rc}")


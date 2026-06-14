# Project 2 - Expense Tracker
 
Second project for the DecodeLabs Python internship (2026 batch).
 
## What it does
 
A small program that keeps asking you for expense amounts and adds them all up. Type 'done' when you're finished and it shows you a total along with a list of everything you entered.
 
## What I learned
 
- the accumulator pattern, basically total = total + new_value, just written as total += new_value
- why you have to put total = 0 outside the loop and not inside (otherwise it resets every time, took me a while to understand this)
- input() always gives you a string, so you need float() or int() to actually do math with it
- try/except so the program doesn't crash if someone types something that's not a number
- using a "sentinel value" (typing 'done') to break out of a while True loop
- splitting the code into functions for adding expenses and showing the report

"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *



# Your code goes here

def calc_functions(tokens):
	if tokens[0] == "q":
		return
	elif tokens[0] == "+":
		return add(int(tokens[1]), int(tokens[2]))
	elif tokens[0] == "-":
		return subtract(int(tokens[1]), int(tokens[2]))


def get_input():
	print("Hello!")

	input_string = input("")

	tokens = input_string.split(" ")
	print(calc_functions(tokens))

	

get_input()

   
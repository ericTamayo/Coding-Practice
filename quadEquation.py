#!/usr/bin/env python
import math

#quadraticpy
# quadratic formula: (-b + or - sqrt(b^2 - 4ac)) / 2a
# define constant
# output is limited to 2 decimal places, can be changed below

dp = "%.2f"

def quadratic(a,b,c):

	discRoot = math.sqrt((b * b) - 4 * a * c) # first pass
	root1 = (-b + discRoot) / (2 * a) # solving positive
	root2 = (-b - discRoot) / (2 * a) # solving negative

	return root1,root2
	
if __name__ == '__main__':
	quadratic()
else:
	pass
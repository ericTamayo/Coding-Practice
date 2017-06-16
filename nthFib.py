def nthFib(n):
	if n < 0:
		print "Integer can not be negative"
		exit()
		
	if n <= 1:
		return n 

	prev_result = 0
	current_result = 1

	for i in range(0,n+1):

		if i <= 1:
			continue

		result = current_result + prev_result
		prev_result = current_result
		current_result = result
		# print "Pre: %s"%prev_result
		# print "Cur: %s"%current_result
	return result

try:
	n = input("Enter Integer: ")
	print "Fibonacci Number: %s"%nthFib(n)

except KeyboardInterrupt:
	print "\n"

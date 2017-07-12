def bracket_validator(codeString):
	#Check to see if there are an even number of backets
	if len(codeString)%2 != 0:
		print "Odd number of Openers and Closers, must at least have even amount to be valid."
		return False

	openArray = [None] * (len(codeString)/2)
	closedArray = [None] * (len(codeString)/2)

	closedBracket = ']'
	closedParenthesis = ')'
	closedCurly = '}'

	count = 0 
	openIndex = 0
	closedIndex = 0
	for i in codeString:
		if i == '[' or i == '(' or i == '{':
			openArray[openIndex] = i
			openIndex += 1
		if i == ']' or i == ')' or i == '}':
			closedArray[closedIndex] = i
			closedIndex += 1
	print "Open:"	
	print "\t%s"%openArray
	print "Closed:"
	print "\t%s"%closedArray 

	for i, char in enumerate(openArray):
		# Define Matches
		if char == '[':
			charToSeek = ']'
		elif char == '(':
			charToSeek = ')'
		elif char == '{':
			charToSeek = '}'
		
		#See if Closed Bracket is in closed array and in the correct order
		if charToSeek == closedArray[len(closedArray) - 1 - i]:
			print char, closedArray[len(closedArray) - 1 - i]
			continue 
		else:
			print "Openers and Closers not properly nested."
			return False

	return True


try:
	codeString = '[' + '{'+ '}' + ']'
	print codeString
	print bracket_validator(codeString)
	
	codeString = '['+'{'+']'+'}'
	print'\n'
	print codeString
	print bracket_validator(codeString)
	
	codeString = '[' + '{' + '}' + ']'+']'
	print'\n'
	print codeString
	print bracket_validator(codeString)


except KeyboardInterrupt:
	print "\n"
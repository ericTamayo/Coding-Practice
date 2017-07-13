def bracket_validator(codeString):
	#Check to see if there are an even number of backets
	#chose stack because we only care about the most recent element at a given time
	stack = []

	for char in codeString:
		if char == '[' or char == '(' or char == '{':
			#any opener we see, we add to the stack
			stack.append(char)
			
		elif char == ']' or char == ')' or char == '}':
			#check most recently seen opener
			mostRecent = stack.pop()
			#look up correct closer
			if mostRecent == '[':
				charToSeek = ']'
			elif mostRecent == '(':
				charToSeek = ')'
			elif mostRecent == '{':
				charToSeek = '}'
			
			#make sure closer matches the most recent opener
			if char == charToSeek:
				continue 
			else:
				return False
	#if stack is empty, all openers have a closer
	return stack == []


try:
	codeString = '[{}]'
	print codeString
	print bracket_validator(codeString)
	
	codeString = '[{]}'
	print'\n'
	print codeString
	print bracket_validator(codeString)
	
	codeString = '[{}]()'
	print'\n'
	print codeString
	print bracket_validator(codeString)


except KeyboardInterrupt:
	print "\n"
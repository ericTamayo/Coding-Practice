def reverse_words(message):
	wordArr = []
	returnMe = ""
	word = ""
	for i in message:
		if i == " ":
			wordArr.append(word)
			word = ""
		else:
			word = word + i
	
	lenWordArr = len(wordArr)

	for j in range(lenWordArr-1, -1, -1):
		returnMe = returnMe + wordArr[j] + " "

	return returnMe
message = 'find you will pain only go you recordings security the into if'

print reverse_words(message)
# returns: 'if into the security recordings you go only pain will you find'
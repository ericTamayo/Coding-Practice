import random 
import numpy

def merge_lists(listA, listB):
	lenOfMergedList = len(listA)+len(listB)
	megeredList = [None]*(lenOfMergedList)
	
	indexA = 0
	indexB = 0
	duplicateIndex = False 
	endOfListA = False
	endOfListB = False
	didYouUseLastElementA = False
	didYouUseLastElementB = False

	for i in xrange(lenOfMergedList):

		#Check if we are at the end of a list
		if indexA == len(listA) - 1:
			endOfListA = True
		if indexB == len(listB) - 1:
			endOfListB = True
	
		#Duplicate Index
		if duplicateIndex:
			duplicateIndex= False 
			megeredList[i] = listB[indexB]
			
			if indexB < len(listB) - 1:indexB += 1

		elif listA[indexA] == listB[indexB]:
			megeredList[i] = listA[indexA]
			
			if indexA < len(listA) - 1:indexA += 1
			
			duplicateIndex = True

		#End of merged list
		elif i == lenOfMergedList - 1:
			megeredList[i] = max(listA[indexA],listB[indexB]) 
		
		#Sorting 
		#A > B
		elif listA[indexA] > listB[indexB] and endOfListB == False:
			megeredList[i] = listB[indexB]
			
			if indexB < len(listB) - 1:
				indexB += 1
		
		#B > A
		elif listA[indexA] < listB[indexB] and endOfListA == False:
			megeredList[i] = listA[indexA]
			
			if indexA < len(listA) - 1:
				indexA += 1

		#End of list A
		elif endOfListA == True:
			if didYouUseLastElementA == False:
				megeredList[i] = min(listA[indexA],listB[indexB])
				if megeredList[i] == listA[indexA]:
					didYouUseLastElementA = True
			else:
				megeredList[i] = max(listA[indexA],listB[indexB]) 
				if indexB < len(listB) - 1:
					indexB += 1
		#End of list B		
		elif endOfListB == True:
			if didYouUseLastElementB == False:
				megeredList[i] = min(listA[indexA],listB[indexB])
				if megeredList[i] == listB[indexB]:
					didYouUseLastElementB = True 
			else:
				megeredList[i] = max(listA[indexA],listB[indexB]) 			
				if indexA < len(listA) - 1:
					indexA += 1

		#print megeredList
	return megeredList

def merge_multiList(bigList):
	lenOfBigList = len(bigList)
	for i in xrange(lenOfBigList-1):

		#store the most recently mered list in the current elemet
		if i == lenOfBigList - 1:
			bigList[i] = merge_lists(bigList[i], bigList[i+1])
		else:
			bigList[i+1] = merge_lists(bigList[i], bigList[i+1])
	
	return bigList[i+1]

try:
	my_list     = [3, 4, 6, 8, 11, 15, 18]
	alices_list = [1, 5, 8, 12, 14, 19]
	third_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	print merge_lists(my_list, alices_list)

	bigList = [my_list, alices_list,third_list]

	print merge_multiList(bigList)
except KeyboardInterrupt:
	print "\n"
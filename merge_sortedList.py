import random 
import numpy

def merge_lists(listA, listB):
	lenOfMergedList = len(listA)+len(listB)
	megeredList = [None]*(lenOfMergedList)
	
	indexA = 0
	indexB = 0
	duplicateIndex = False 


	for i in xrange(lenOfMergedList):
		# print indexA,indexB
		# print listA[indexA], listB[indexB]

		print i
		print megeredList

		if duplicateIndex:
			duplicateIndex= False 
			megeredList[i] = listB[indexB]
			indexB += 1
		elif listA[indexA] > listB[indexB]:
			megeredList[i] = listB[indexB]
			if indexB < len(listB) - 1:
				indexB += 1
		elif listA[indexA] < listB[indexB] and indexA < len(listA):
			megeredList[i] = listA[indexA]
			if indexA < len(listA) - 1:
				indexA += 1
		elif listA[indexA] == listB[indexB]:
			megeredList[i] = listA[indexA]
			indexA += 1
			skipIndex = True
		
		if i == lenOfMergedList - 1:
			megeredList[i] = max(listA[indexA],listB[indexB]) 

	return megeredList

# def merge_multiList(theList):
# 	lenOfTheList = len(theList)
# 	for i in xrange(lenOfTheList-1):
# 		merge_lists(theList[i], theList[i+1])
		
try:
	my_list     = [3, 4, 6, 8, 11, 15,18]
	alices_list = [1, 5, 8, 12, 14, 19]

	print merge_lists(my_list, alices_list)

	# theList = [my_list, alices_list]
	# print theList
	# print merge_multiList(theList)
except KeyboardInterrupt:
	print "\n"
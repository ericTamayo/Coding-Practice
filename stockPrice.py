import random 
import numpy
def get_max_profit(arr = []):
	buyIndex = 0
	sellIndex = 0
	maxProfit = 0
	###O(N^2)
	###Brute Force Method
	# for i in xrange(len(arr)):
	# 	for j in xrange(len(arr)-1):
	# 		if i == len(arr):
	# 			break
	# 		if arr[i] > arr[j+1]:
	# 			continue 
	# 		if arr[j+1] > arr[i]:
	# 			profit = arr[j+1] - arr[i]
	# 			if profit > maxProfit:
	# 				buyTime = i
	# 				sellTime = j+1
	# 				maxProfit = profit
	# return maxProfit,buyTime,sellTime
	
	###Can reduce cost by tracking the minimum price
	###since you have to buy befor you can sell 
	###only have to iterate through array once 
	###O(N) Solution 
	minPrice = arr[0]
	#enumerate syntax
	#returns indexc and value or array

	#edgeCase 
	if len(arr) < 2:
		raise ValueError("Need at least 2 values to compute profit!") 

	potentialBuyIndex = 0
	sellIndex = 0
	for i, currentPrice in enumerate(arr):
		###Skip 1st Index. Can not buy and sell at the same time  
		if i == 0:
			continue 
		###Check for a new max profit

		potentialProfit = currentPrice - minPrice 
		
		###Track the min price 
		if currentPrice < minPrice:
			minPrice = currentPrice
			potentialBuyIndex = i
		
		###Check for a new max profit
		if maxProfit < potentialProfit:
			maxProfit = currentPrice - minPrice 
			sellIndex = i
			buyIndex = potentialBuyIndex
		

	return maxProfit, buyIndex, sellIndex

def indexToTime(index = 0):
	if index == 0:
		hours = 9
		minutes = '30'
	elif index == 1:
		hours = 10
		if index%2 == 0: 
			minutes = '30'
		else:
			minutes = '00'
	elif index > 0:
		hours = index/2 + 9
		if index%2 == 0: 
			minutes = '30'
		else:
			minutes = '00'
	else:
		raise ValueError("Index Can Not Be Negative!")
	return "%s:%s"%(hours,minutes)

try:
	stock_prices_yesterday = [100, 70, 50, 80, 110, 90]
	print('\n')
	print "Yesterday's Stock Prices(Fixed Array):"
	print stock_prices_yesterday
	print "If stock market opens at 9:30am"
	maxProfit,buyIndex,sellIndex = get_max_profit(stock_prices_yesterday)
	buyTime = indexToTime(buyIndex)
	sellTime = indexToTime(sellIndex)
	print "You can earn a max of %s$ per a share"%maxProfit
	print "By buying at: %s"%(buyTime)
	print "Then selling at: %s"%sellTime
	# returns 6 (buying for $5 and selling for $11)

	#create random array
	#30 min increments
	#Market Open (9:30) Market Close(16:00)
	randomArr = [0] *13
	for i in xrange(13):
		randomArr[i] = random.randrange(10,1000)
	print("\n")
	print "Yesterday's Stock Prices(Random Array):"
	print randomArr
	maxProfit,buyIndex,sellIndex = get_max_profit(randomArr)
	buyTime = indexToTime(buyIndex)
	sellTime = indexToTime(sellIndex)
	print "You can earn a max of %s$ per a share"%maxProfit
	print "By buying at: %s"%(buyTime)
	print "Then selling at: %s"%sellTime

except KeyboardInterrupt:
	print "\n"
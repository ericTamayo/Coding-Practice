def get_max_profit(arr = []):
	buyTime = 0
	sellTime = 0
	maxProfit = 0
	for i in xrange(len(arr)):
		for j in xrange(len(arr)-1):
			if i == len(arr):
				break
			if arr[i] > arr[j+1]:
				continue 
			if arr[j+1] > arr[i]:
				profit = arr[j+1] - arr[i]
				if profit > maxProfit:
					buyTime = i
					sellTime = j+1
					maxProfit = profit
	return maxProfit,buyTime,sellTime

def indexToTime(index = 0):
	if index == 0:
		hours = 9
		minutes = '30'
	if index > 0:
		hours = index/2 + 9
		if index%2 == 0: 
			minutes = '30'
		else:
			minutes = '00'
	return "%s:%s"%(hours,minutes)

try:
	stock_prices_yesterday = [100, 70, 50, 80, 110, 90]

	print "If stock market opens at 9:30am"
	maxProfit,buyIndex,sellIndex = get_max_profit(stock_prices_yesterday)
	buyTime = indexToTime(buyIndex)
	sellTime = indexToTime(sellIndex)
	print "You can earn a max of %s$ per a share"%maxProfit
	print "By buying at: %s"%(buyTime)
	print "Then selling at: %s"%sellTime
	# returns 6 (buying for $5 and selling for $11)

except KeyboardInterrupt:
	print "\n"
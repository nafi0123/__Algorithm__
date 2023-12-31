# A Dynamic Programming based Python 
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can 
# be put in a knapsack of capacity W 


def knapSack(W, wt, val, n): 
	K = [[0 for x in range(W + 1)] 
	  for x in range(n + 1)] 

	# Build table K[][] in bottom up manner 
	for i in range(n + 1): 
		for w in range(W + 1): 
			if i == 0 or w == 0: 
				K[i][w] = 0
			elif wt[i-1] <= w: 
				K[i][w] = max(val[i-1] 
							+ K[i-1][w-wt[i-1]], 
							K[i-1][w]) 
				print(w-wt[i-1])
			else: 
				K[i][w] = K[i-1][w] 

	return K[n][W] 


# Driver code 
if __name__ == '__main__': 
	profit = [4,3,6,5] 
	weight =[3,2,5,4] 
	W = 5
	n = len(profit) 
	print(knapSack(W, weight, profit, n)) 

# This code is contributed by Bhavya Jain 

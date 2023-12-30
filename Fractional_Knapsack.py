class ITEM:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight
def fractionalKnapsack(W,arr):
    arr.sort(key=lambda x:(x.profit/x.weight),reverse=True)
    final_value=0.0
    for item in arr:
        if item.weight<W:
            W-=item.weight
            final_value+=item.profit
        else:
            final_value+=item.profit*W/item.weight
            break
    return final_value
if __name__ == "__main__":
	W = 50
	arr = [ITEM(60, 10), ITEM(100, 20), ITEM(120, 30)]
	print(arr)

	# Function call
	max_val = fractionalKnapsack(W, arr)
	print(max_val) 
        

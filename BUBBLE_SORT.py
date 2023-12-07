class BUBBLE_SORT:
    def __init__(self,arr) :
        self.arr=arr
    
    def _sort__(self,array):
        for i in range(0,len(array)-1):
            for j in range(0,len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j],array[j+1]=array[j+1],array[j]
        return array
arr=[10,60,50,80,50,0]
obj=BUBBLE_SORT(arr) 
print(obj._sort__(arr))  

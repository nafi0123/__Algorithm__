class Quick_Sort:
    def __init__(self,array) -> None:
        self.arr=array

    def partition(self,low,high):
        pivot=self.arr[high]
        i=low-1
        for j in range(low,high):
            if self.arr[j]<=pivot:
                i=i+1
                self.arr[i],self.arr[j]=self.arr[j],self.arr[i]
        self.arr[i+1],self.arr[high]=self.arr[high],self.arr[i+1]
        return i+1


    def _sort__(self,low,high):
        if low<high:

            pi=self.partition(low,high)
            self._sort__(low,pi-1)
            self._sort__(pi+1,high)
        return self.arr

if __name__ == "__main__":
    input_array = [12, 11, 13, 5, 6, 7]
    obj=Quick_Sort(input_array)
    size=len(input_array)-1

    sorted_list=obj._sort__(0,size)
    print(sorted_list)

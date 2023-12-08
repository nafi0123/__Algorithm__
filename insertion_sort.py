class insertion_sort:
    def __init__(self,arr) -> None:
        self.arr=arr
    def _sort__(self):
        for i in range (1,len(self.arr)-1):
            value=i
            hole=i
            while hole>0 and self.arr[hole-1]>value:
                self.arr[hole]=self.arr[hole-1]
                hole=hole-1
            self.arr[hole]=value
        return self.arr
        

if __name__ == "__main__":
    arr=[1,50,3,2,0,800,300]
    ob=insertion_sort(arr)
    print(ob._sort__())

class Bubble_sort:
    def __init__(self,arr) -> None:
        self.arr=arr
    def sort_(self):
        for i in range(len(self.arr)-1):
            for j in range(len(self.arr)-i-1):
                if self.arr[j]>self.arr[j+1]:
                    self.arr[j],self.arr[j+1]=self.arr[j+1],self.arr[j]
        return self.arr
if __name__ == "__main__":
    array=[1,5,6,0,8,0,100,200]
    ob=Bubble_sort(array)
    print(ob.sort_())

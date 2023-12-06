def binarySearch(arr,l,r,num):
    while (l<=r):
        mid=(l+r)//2
        if arr[mid]==num:
            return mid
        if arr[mid]<num:
            l=mid+1
        else:
            r=mid-1
    


arr=[1,5,8,10,14,20,25,60,80,90]
arr.sort()
print(arr)
print(binarySearch(arr,0,len(arr)-1,80))

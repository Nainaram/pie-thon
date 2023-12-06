arr = [12,23,34,34,23,12,21,50]
def binary_search(arr , target):
    low = 0
    high = len(arr)-1
    mid = (low+high)//2
    while(low <= high):
        if(arr[mid] ==target):
            return mid
        elif(arr[mid] < target):
            low == mid+1
            
        else:
            high == mid-1
    return -1

search = binary_search(arr,12)
print(search)
            
            
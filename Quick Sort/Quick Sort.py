def partitionFunc(data, low, high):
    pivot = data[low]
    i = low+1
    j = high
    issorted = False

    while not issorted:
        while i <= j and data[i] <= pivot:
            i += 1
        while j >= i and data[j] >= pivot:
            j -= 1
        if j < i:
            issorted = True
        else:
            data[i],data[j] = data[j],data[i] 
    data[low],data[j] = data[j],data[low] 
    return j

def QuickSort(data, low, high):
    if low < high:
        split = partitionFunc(data, low, high)
        QuickSort(data, low, split-1)
        QuickSort(data, split+1, high)

    return data

A = [99,45,23,6576,1345,7,2,5]
print("Sorted List:",QuickSort(A,0,len(A)-1))



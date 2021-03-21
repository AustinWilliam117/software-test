def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

if __name__ == '__main__':
    list = [1,5,8,9,123,22,56,342,36,22]
    print("List source is:", list)
    result = bubbleSort(list)
    print("List sort is:", result)
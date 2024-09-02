def insertionSort(num):
    n = len(num)  
      
    if n <= 1:
        return  
 
    for i in range(1, n):  
        key = num[i]  
        j = i-1
        while j >= 0 and key < num[j]:  
            num[j+1] = num[j]  
            j -= 1
        num[j+1] = key 
  

num = [10,24,18,6,34]
insertionSort(num)
print(num)


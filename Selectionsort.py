def selectionSort(num, size):
   
    for step in range(size):
        min = step

        for i in range(step + 1, size):
         
            
            if num[i] < num[min]:
                min= i
         
        
        (num[step], num[min]) = (num[min], num[step])


num = [12, 45, 6, 5, 18]
size = len(num)
selectionSort(num, size)
print('Sorted Array in Ascending Order:')
print(num)

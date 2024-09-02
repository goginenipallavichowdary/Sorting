def bubbleSort(num):
    

  for i in range(len(num)):

    
    for j in range(0, len(num) - i - 1):

      
      if num[j] > num[j + 1]:

        
        temp = num[j]
        num[j] = num[j+1]
        num[j+1] = temp


num = [2,32,24,6,12]

bubbleSort(num)

print('Sorted Array in Ascending Order:')
print(num)

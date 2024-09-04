Selection Sort:
In the selection sort it list array by selecting smallest element in unsorted portion of arrary and exchanging it with element at the begining of the unsorted list.In Selection Sort it is a basic sorting algorithm that relies on comparisons. It functions by repeatedly choosing the smallest (or largest, based on the order of sorting) element from the list's unsorted section and shifting it to the start (or finish) of the sorted section.

1.Initialization: The subarray array[0...-1] is empty prior to the first iteration (i = 0), which can be easily sorted.
2.Maintenance: Assume that for the first i iterations, the loop invariant holds true. In the iteration that is i:

The unsorted segment array[i..n-1] minimal element is found via the algorithm.
Next, it replaces the element at array[i] with this minimum element.
array[0...i] is sorted as a result, and the smallest i+1 elements of the original array are found in it.
As a result, the loop invariant is preserved.

3.Termination: The loop comes to an end when i = n-1, where n is the array's length. At this point, the loop invariant indicates that array[0..n-1] has been sorted and contains all of the original array's contents in sorted order
Since the loop invariant holds at the end of the loop, the entire array is sorted correctly.

4.Arguing Termination
The algorithm terminates when the outer loop completes its iterations. Since the loop runs from i = 0 to i = n-1, it performs a finite number of iterations (n-1), where n is the length of the input array. Each iteration reduces the size of the unsorted portion of the array by one element, ensuring that the loop will eventually terminate.

5.Conclusion
Selection sort is correct because:The loop invariant proves that, if the algorithm terminates, it produces a sorted array.
Termination: The algorithm terminates after a finite number of steps.
Thus, selection sort is a correct sorting algorithm.

System Information CPU: 
Processor- Apple M1, Ram- 16GB.

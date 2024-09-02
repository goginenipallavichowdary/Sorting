import random
import timeit



def selectionSort(num, size):
    for step in range(size):
        min_index = step
        for i in range(step + 1, size):
            if num[i] < num[min_index]:
                min_index = i
        (num[step], num[min_index]) = (num[min_index], num[step])


def bubbleSort(num):
    for i in range(len(num)):
        for j in range(0, len(num) - i - 1):
            if num[j] > num[j + 1]:
                temp = num[j]
                num[j] = num[j + 1]
                num[j + 1] = temp


def insertionSort(num):
    n = len(num)
    if n <= 1:
        return
    for i in range(1, n):
        key = num[i]
        j = i - 1
        while j >= 0 and key < num[j]:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = key


def benchmark_sort(sort_function, arr):
    timer = timeit.Timer(lambda: sort_function(arr.copy(), len(arr)) if sort_function == selectionSort else sort_function(arr.copy()))
    times = timer.repeat(repeat=3, number=1)
    return min(times)


sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

algorithms = {
    'Selection Sort': selectionSort,
    'Bubble Sort': bubbleSort,
    'Insertion Sort': insertionSort
}


def run_benchmarks():
    results = {name: [] for name in algorithms}

    for size in sizes:

        arr = [random.randint(0, 100000) for _ in range(size)]
        print(f"Running benchmarks for size: {size}")


        for name, algorithm in algorithms.items():
            print(f"  Benchmarking {name}...")
            time_taken = benchmark_sort(algorithm, arr)
            results[name].append(time_taken)
            print(f"  {name} took {time_taken:.5f} seconds.")


   

if __name__ == "__main__":
    run_benchmarks()

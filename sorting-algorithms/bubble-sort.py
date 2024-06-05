def bubble_sort(array):
    n = len(array)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(n-i-1):
            comparisons+=1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swaps+=1
    return array, comparisons, swaps
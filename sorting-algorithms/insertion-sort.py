def insertion_sort(array):
    n = len(array)
    comparisons = 0
    swaps = 0
    for i in range(1, n):
        key = array[i]
        j = i - 1
        if array[j] <= key:
            comparisons += 1
            continue
        while j >= 0 and array[j] > key:
            comparisons+=1
            array[j+1] = array[j]
            j -= 1
            swaps += 1
        array[j+1] = key
        if j>=0:
            comparisons += 1
    return array, comparisons, swaps
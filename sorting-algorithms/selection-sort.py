def selection_sort(array):
    n = len(array)
    comparisons = 0
    swaps = 0

    for i in range(n):
        smallest = i
        for j in range(i+1, n):
            if array[j]<array[smallest]:
                smallest = j
                comparisons += 1
        if smallest != i:
            array[i], array[smallest] = array[smallest], array[i]
            swaps += 1

    return array, comparisons, swaps

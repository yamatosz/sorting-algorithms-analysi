def quick_sort(arr):
    comparisons = [0]
    swaps = [0]

    def _quick_sort(items, low, high):
        if low < high:
            pi = partition(items, low, high)
            _quick_sort(items, low, pi - 1)
            _quick_sort(items, pi + 1, high)

    def median_of_three(items, low, high):
        mid = (low + high) // 2
        if items[low] > items[mid]:
            items[low], items[mid] = items[mid], items[low]
            swaps[0] += 1
        if items[low] > items[high]:
            items[low], items[high] = items[high], items[low]
            swaps[0] += 1
        if items[mid] > items[high]:
            items[mid], items[high] = items[high], items[mid]
            swaps[0] += 1
        return mid

    def partition(items, low, high):
        median_index = median_of_three(items, low, high)
        items[median_index], items[high] = items[high], items[median_index]
        swaps[0] += 1
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if items[j] < pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                swaps[0] += 1
        items[i + 1], items[high] = items[high], items[i + 1]
        swaps[0] += 1
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
    return comparisons[0], swaps[0], arr

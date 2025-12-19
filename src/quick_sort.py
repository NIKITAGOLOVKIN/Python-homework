def quick_sort(arr):
    if len(arr) <= 1:
        return list(arr)
    return _quick_sort(list(arr), 0, len(arr) - 1)


def _quick_sort(arr, low, high):
    if low < high:
        pivot_index = _separation(arr, low, high)
        _quick_sort(arr, low, pivot_index - 1)
        _quick_sort(arr, pivot_index + 1, high)
    return arr


def _separation(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


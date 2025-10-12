# Быстрая сортировка (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

# Сортировка выбором (Selection Sort)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Сортировка вставками (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Самая используемая сортировка в Python — Timsort (через встроенную sorted())
def timsort(arr):
    return sorted(arr)

# Пример использования:
if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    # SORTING COPIED DATA LIST USING data.copy(), ORIGINAL data list remains unsorted
    print("Quick Sort:", quick_sort(data.copy()))
    print("Selection Sort:", selection_sort(data.copy()))
    print("Insertion Sort:", insertion_sort(data.copy()))
    print("Timsort (built-in):", timsort(data.copy()))
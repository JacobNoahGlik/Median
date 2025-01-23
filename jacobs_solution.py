from typing import List

def find_median(array: List[float]) -> float:
    n = len(array)
    if n % 2 == 1:
        return array[n // 2]
    else:
        return (array[n // 2 - 1] + array[n // 2]) / 2

def binary_search_closest(array: List[float], value: float) -> int:

    left, right = 0, len(array) - 1

    while left < right:
        mid = (left + right) // 2
        if array[mid] < value:
            left = mid + 1
        else:
            right = mid

    if left == 0:
        return 0
    if left == len(array):
        return len(array) - 1

    if abs(array[left - 1] - value) <= abs(array[left] - value):
        return left - 1
    else:
        return left

def kth_element(array1, array2, k: int) -> float:
    i, j = 0, 0
    while True:
        if i == len(array1):
            return array2[j + k]
        if j == len(array2):
            return array1[i + k]
        if k == 0:
            return min(array1[i], array2[j])

        step = (k - 1) // 2

        new_i = min(i + step, len(array1) - 1)
        new_j = min(j + step, len(array2) - 1)

        if array1[new_i] <= array2[new_j]:
            k -= (new_i - i + 1)
            i = new_i + 1
        else:
            k -= (new_j - j + 1)
            j = new_j + 1

def find_median_of_two_sorted_arrays(array1: List[float], array2: List[float]) -> float:
    total_length = len(array1) + len(array2)
    merged_median_index = (total_length - 1) // 2
    if total_length % 2 == 1:
        return kth_element(array1, array2, merged_median_index)
    else:
        return (kth_element(array1, array2, merged_median_index) + kth_element(array1, array2, merged_median_index + 1)) / 2


if __name__ == "__main__":
    array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    array2 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    median = find_median_of_two_sorted_arrays(array1, array2)
    print(f"The median of the combined arrays is: {median}")

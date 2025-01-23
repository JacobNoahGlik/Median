from typing import List
def find_median(arr1: List[float], arr2: List[float]) -> float:
    len1 = len(arr1)
    len2 = len(arr2)
    len3 = len1 + len2

    i1 = len1 // 2
    i2 = len2 // 2
    c1, c2 = i1, i2
    if arr1[i1] > arr2[i2]:
        while c1 > 0 and arr1[c1] > arr2[i2]:
            c1 -= 1
        while c2 < len(arr2) and arr2[c2] < arr1[i1]:
            c2 += 1
        res1 = arr1[c1:i1]
        res2 = arr2[i2:c2]
        offset = c1 + i2
    else:
        while c1 < len1 and arr1[c1] < arr2[i2]:
            c1 += 1
        while c2 > 0 and arr2[c2] > arr1[i1]:
            c2 -= 1
        res1 = arr1[i1:c1]
        res2 = arr2[c2:i2]
        offset = c2 + i1
    resulting_array: List[float] = merge(res1, res2)
    median_index = len3 // 2 - offset
    if len3 % 2 == 0:
        return (resulting_array[median_index] + resulting_array[median_index - 1] ) / 2
    else:
        return resulting_array[median_index]
        


def merge(arr1: List[float], arr2: List[float]) -> List[float]:
    c1, c2 = 0, 0
    resulting_arr: List[float] = []
    while c1 < len(arr1) and c2 < len(arr2):
        if arr1[c1] < arr2[c2]:
            resulting_arr.append(arr1[c1])
            c1 += 1
        else:
            resulting_arr.append(arr2[c2])
            c2 += 1
    return resulting_arr + arr1[c1:] + arr2[c2:]


    
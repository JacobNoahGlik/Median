from typing import Tuple, List

def find_median(arr1: List[float], arr2: List[float]) -> float:
    _, i1 = median(arr1)
    _, i2 = median(arr2)
    arr_result: List[float] = []
    c1, c2 = i1, i2
    while c1 == i1 or c2 == i2:
        if arr1[c1] < arr2[c2]:
            arr_result.append(arr1[c1])
            c1 += 1
        else:
            arr_result.append(arr2[c2])
            c2 += 1
    # print(arr_result)
    resulting_median, _ = median(arr_result)
    return resulting_median

def median(array: List[float]) -> Tuple[float, int]:
    if len(array) % 2 == 1:
        return (array[len(array) // 2], len(array) // 2)
    return (
        (array[len(array) // 2] + array[len(array) // 2 - 1] )/ 2,
        len(array) // 2
    )

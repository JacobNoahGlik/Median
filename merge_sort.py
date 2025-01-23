from typing import Tuple, List
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
def find_median(arr1: List[float], arr2: List[float]) -> float:
    merged_arr = merge(arr1, arr2)
    # print(f'median@index={len(merged_arr) / 2 - 0.5}, {merged_arr=}')
    resulting_median, _ = median(merged_arr)
    return resulting_median

def median(array: List[float]) -> Tuple[float, int]:
    if len(array) % 2 == 1:
        return (array[len(array) // 2], len(array) // 2)
    return (
        (array[len(array) // 2] + array[len(array) // 2 - 1] )/ 2,
        len(array) // 2
    )
import merge_sort
import michaels_solution

arr1 = [1, 2, 3, 4, 5, 10, 15, 22, 532, 684]
arr2 = [103, 106, 145, 175, 397, 576, 598, 625, 897, 407]

print(merge_sort.find_median(arr1, arr2))
print(michaels_solution.find_median(arr1, arr2))
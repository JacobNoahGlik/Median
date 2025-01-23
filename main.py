import merge_sort
import michaels_solution

arr1 = [2, 3, 4, 5, 10, 15, 22, 532, 684]
arr2 = [103, 106, 145, 175, 397, 576, 598, 625, 897] 
####                |                                 |
#### [1, 2, 3, 4, 5, 10, 15, 22, 103, 106, 145, 175, 397, 576, 598, 625, 897]
####                                  ***
print('')
print(f'{arr1=}')
print(f'{arr2=}')
print(merge_sort.find_median(arr1, arr2))
print(michaels_solution.find_median(arr1, arr2))
print('')
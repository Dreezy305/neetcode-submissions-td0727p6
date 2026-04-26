import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    my_list: List[str] = [] 
    
    for element in strings:
         heapq.heappush(my_list, element)
    return my_list


def heapify_integers(integers: List[int]) -> List[int]:
    my_x:List[int] = []

    for element in integers:
        heapq.heappush(my_x, element)
    return my_x


def heap_sort(nums: List[int]) -> List[int]:
    my_x:List[int] = []

    for element in nums:
        heapq.heappush(my_x, element)

    new_list:List[int] = sorted(my_x)
    return new_list


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))

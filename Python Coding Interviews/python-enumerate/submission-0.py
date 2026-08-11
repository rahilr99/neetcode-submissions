from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i, number in enumerate(nums):
        if number==7:
            return i
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    count_seven = 0
    index_first, index_second = 0, 0
    for i, number in enumerate(nums):
        if number ==7 :
            count_seven+=1
            if count_seven<=1:
                index_first = i
            else: 
                return i-index_first
    return -1


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))

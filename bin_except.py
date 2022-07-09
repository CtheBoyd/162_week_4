# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/8/2022
# Description: Returns lemonade stand sales and profits
#
class TargetNotFound(Exception):
    """exception class"""
    pass



def bin_except(a_list, target):
    """Binary search function with call for exception class when target not on list."""

    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1

    return TargetNotFound

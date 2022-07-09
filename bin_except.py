# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/8/2022
# Description: Returns lemonade stand sales and profits
#
class TargetNotFound(Exception):
    """exception class"""
    pass

class BinarySearch:


    def __init__(self, binary_search):
        self.binary_search = binary_search


    def bin_except(a_list, target):

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

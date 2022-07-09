# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/9/2022
# Description: Case-insensitive string insertion sort
#

#a_list = ['Zebra', 'apple', 'maRker', 'marble']
def string_sort():
    """
    Sorts a_list in ascending order
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and value < a_list[pos]:
            a_list[pos + 1] = a_list[pos]
            pos = pos - 1
        a_list[pos + 1] = value
        a_list.sort(key=lambda x: x.lower())

    print(a_list)

#string_sort()

# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/9/2022
# Description: Case-insensitive string insertion sort
#

a_list = ['Zebra', 'apple', 'maRker', 'marble']
#a_list = ['zebra', 'apple', 'marker', 'marble']
def string_sort():
    """
    Sorts a_list in ascending order
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos].lower() > value.lower():
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


    print(a_list)

string_sort()

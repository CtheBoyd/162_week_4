# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/9/2022
# Description: calculates box volume and returns box list sorted by volume.
#


def bubble_count(a_list):
    comparisons = 0
    exchanges = 0
    """
    Sorts a_list in ascending order
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            comparisons += 1
            if a_list[index] > a_list[index + 1]:
                exchanges += 1
            temp = a_list[index]
            a_list[index] = a_list[index + 1]
            a_list[index + 1] = temp

    return comparisons, exchanges


def insertion_count(a_list):
    comparisons = 0
    exchanges = 0

    """
    Sorts a_list in ascending order
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        comparisons += 1
        while pos >= 0 and a_list[pos] > value:
            comparisons += 1
            a_list[pos + 1] = a_list[pos]
            exchanges += 1
            pos -= 1
            exchanges += 1
        a_list[pos + 1] = value

    return comparisons, exchanges




#a_list =[8, 7, 9, 4]
#print(bubble_count(a_list))
#print(insertion_count(a_list))
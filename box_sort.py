# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 7/9/2022
# Description: calculates box volume and returns box list sorted by volume.
#


class Box:
    """box class takes three perameters and returns box dimensions"""

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height


    """getters"""
    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_volume(self):
        return self.volume

    def volume(self):
        volume = (self._height() * self._length() * self._width())

        return volume()


def box_sort(a_list):

    """
    Sorts a_list in ascending order
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value

    return a_list

b1 = Box(3.4, 19.8, 2.1)
b2 = Box(1.0, 1.0, 1.0)
b3 = Box(8.2, 8.2, 4.5)
a_list = [b1, b2, b3]
box_sort(a_list)

print(str(a_list))

#!/usr/bin/python3

for nums in range(0, 9):
    for nums1 in range(nums + 1, 10):
        if nums == 8 and nums1 == 9:
            print('{:d}{:d}'.format(nums, nums1))
        else:
            print("{}{},".format(nums, nums1), end=" ")

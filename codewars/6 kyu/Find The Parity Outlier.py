"""You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)"""

def find_outlier(integers):
    count = 0
    for i in range(3):
        if integers[i] % 2 == 0:
            count += 1
    if count > 1:
        for i in integers:
            if i % 2 == 1:
                return i
    else:
        for i in integers:
            if i % 2 == 0:
                return i
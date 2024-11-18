#https://cses.fi/problemset/task/1641
#1. feladat: kereses, rendezes, moho - Sum of Three Values
#minden tesztesetre mukodik

import sys

def three_nums(n, x, array):
    sorted_array = [(value, index) for index, value in enumerate(array)]
    sorted_array.sort()
    solution = False

    for i in range(n):
        a = sorted_array[i][0]
        target = x-a
        left = i+1
        right = n-1
        while left < right:
            b = sorted_array[left][0]
            c = sorted_array[right][0]
            if b + c == target:
                solution = True
                return (sorted([sorted_array[i][1]+1, sorted_array[left][1]+1, sorted_array[right][1]+1]))
            elif b + c < target:
                left += 1
            else:
                right -= 1

    if not solution:
        return "IMPOSSIBLE"

n = None
x = None
array = list()

with open("tests.txt", "r") as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            n = int(line.strip().split()[0])
            x = int(line.strip().split()[1])
        else:
            array = [int(i) for i in line.strip().split()]
            print(three_nums(n, x, array))






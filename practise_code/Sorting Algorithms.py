import time
import tracemalloc
import sys
import random
from timeit import Timer
import sys

import math

test = [18, 87, 45, 84, 24, 1, 5, 51, 50, 47, 12, 67, 17, 4, 97, 29, 25, 82, 66, 48, 10, 96, 54, 91, 19, 0, 33, 46, 98,
        43, 9, 15, 95, 37, 38, 55, 79, 53, 56, 49, 52, 76, 61, 90, 7, 2, 30, 85, 62, 63, 72, 65, 35, 99, 78, 27,
        23, 39, 42, 81, 31, 73, 32, 68, 20, 89, 86, 77, 6, 22, 41, 92, 88, 58, 13, 26, 83, 60, 69, 36, 44, 80, 21, 16,
        3, 40, 8, 57, 59, 28, 93, 11, 71, 64, 75, 74, 34, 14, 70, 94]
myrandom = random.sample(range(10000),10000)
newrandom = [12, 4, 8, 2, 15, 10]
sample = [1, 12, 9, 5, 6, 10]
new = [5, 10, 3, 1, 2]
rando = [1,2,0,3,4]
a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def simple_quicksort_rightmost_pivot(lst):
    n = len(lst)
    if n <= 1:
        return lst
    small = []
    big = []
    pivot = -1
    for i in range(n):
        if lst[i] < lst[pivot]:
            small.append(lst[i])

        if lst[i] == lst[pivot]:
            return simple_quicksort_rightmost_pivot(small) + [lst[i]] + simple_quicksort_rightmost_pivot(big)

        if lst[i] > lst[pivot]:
            big.append(lst[i])


def simple_quicksort_middle_pivot(lst):
    n = len(lst)
    if n <= 1:
        return lst
    small = []
    equal = []
    big = []
    pivot = int(n / 2)
    for i in range(n):
        if lst[i] < lst[pivot]:
            small.append(lst[i])

        if lst[i] == lst[pivot]:
            equal.append(lst[i])

        if lst[i] > lst[pivot]:
            big.append(lst[i])
    return simple_quicksort_middle_pivot(small) + equal + simple_quicksort_middle_pivot(big)


def simple_two_pointer_quicksort_middle_pivot(lst):
    n = len(lst)
    small = []
    equal = []
    big = []
    if n <= 1:
        return lst
    pivot = int(n / 2)
    for i in range(n):
        if lst[i] > lst[pivot]:
            big.append(lst[i])

    for j in range(n - 1, -1, -1):
        if lst[j] == lst[pivot]:
            equal.append(lst[j])

        if lst[j] < lst[pivot]:
            small.append(lst[j])

    return simple_two_pointer_quicksort_middle_pivot(small) + equal + simple_two_pointer_quicksort_middle_pivot(big)


def complex_quicksort_rightmost_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    pivot = -1
    for i in range(n):
        if lst[i] > lst[pivot]:
            for j in range(n - 1, -1, -1):
                if i > j:
                    lst[i], lst[pivot] = lst[pivot], lst[i]
                    return complex_quicksort_rightmost_sort(lst[:i]) + [lst[i]] + complex_quicksort_rightmost_sort(
                        lst[i + 1:])

                if lst[j] < lst[pivot]:
                    lst[i], lst[j] = lst[j], lst[i]
                    n = j
                    break

                if lst[j] == lst[0]:  # if nothing smaller than lst[pivot], j moves till lst[0], moves to last
                    lst[0], lst[pivot] = lst[pivot], lst[0]
                    return [lst[0]] + complex_quicksort_rightmost_sort(lst[0 + 1:])

        if lst[i] == lst[pivot]:  # if nothing bigger than lst[pivot], i moves till pivot, stays
            return complex_quicksort_rightmost_sort(lst[:pivot]) + [lst[pivot]]


def complex_quicksort_middle_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    pivot = int(n / 2)
    lst[pivot], lst[-1] = lst[-1], lst[pivot]  # pivot switcher
    pivot = -1
    for i in range(n):
        if lst[i] > lst[pivot]:
            for j in range(n - 1, -1, -1):
                if i > j:
                    lst[i], lst[pivot] = lst[pivot], lst[i]
                    return complex_quicksort_middle_sort(lst[:i]) + [lst[i]] + complex_quicksort_middle_sort(
                        lst[i + 1:])

                if lst[j] < lst[pivot]:
                    lst[i], lst[j] = lst[j], lst[i]
                    n = j
                    break

                if lst[j] == lst[0]:  # if nothing smaller than lst[pivot], j moves till lst[0], moves to last
                    lst[0], lst[pivot] = lst[pivot], lst[0]
                    return [lst[0]] + complex_quicksort_middle_sort(lst[0 + 1:])

        elif lst[i] == lst[pivot]:  # if nothing bigger than lst[pivot], i moves till pivot, stays
            return complex_quicksort_middle_sort(lst[:pivot]) + [lst[pivot]]


def find_max(i):
    if len(i) == 0:
        return print("Error, iteration is not iterable")
    else:
        curr_max = i[0]
        for num in i:
            if num > curr_max:
                curr_max = num
        return curr_max


def selection_sort(lst):
    sys.setrecursionlimit(10500)
    n = len(lst)
    if n <= 1:
        return lst
    else:
        curr_max = lst[
            0]  # must be placed outside the loop if not it will keep reverting the curr_max to the first element
        for i in range(n):
            if lst[i] > curr_max:
                curr_max = lst[i]  # finds the highest max till itself is the highest max
                if curr_max == lst[-1]:  # skips the swapping if curr_max is the last element
                    return selection_sort(lst[:-1]) + [lst[-1]]

            if lst[i] == lst[-1]:
                position_of_curr_max = lst.index(
                    curr_max)  # must use curr_max in terms of the lst to change the values in the lst
                lst[-1], lst[position_of_curr_max] = lst[position_of_curr_max], lst[-1]
                return selection_sort(lst[:-1]) + [lst[-1]]


def merge_sort(lst):
    n = len(lst)
    if n > 1:
        half = int(n / 2)
        left = lst[:half]
        right = lst[half:]

        merge_sort(left), merge_sort(right)

        # initalise counter on lst
        i = j = k = 0

        while i < len(left) and j < len(right):  # loop only terminates when i and j is bigger than the lst
            # this solves my problem where by right[i] > right[i+1] does not work
            if left[i] < right[j]:
                lst[k] = left[i]
                i = i + 1
            else:
                lst[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            lst[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            lst[k] = right[j]
            j = j + 1
            k = k + 1
        return lst


def bubble_up(lst, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    parent = i
    if l < n and lst[parent] < lst[l]:
        parent = l
    if r < n and lst[parent] < lst[r]:
        parent = r
    if parent != i:
        lst[i], lst[parent] = lst[parent], lst[i]
        return bubble_up(lst, n, parent)

def stopper(n):
    stop_pos_counter = 0
    for factorial in range(1,n):
        stop_pos_counter += 2**factorial
        if stop_pos_counter >= n:
            stopper = stop_pos_counter - 2**factorial
            return stopper


def heap_sort(lst):
    n = len(lst)
    for i in range(stopper(n),-1,-1):  # build phase
        bubble_up(lst, n, i)
    for j in range(n - 1, 0, -1):  # repeat phase
        lst[j], lst[0] = lst[0], lst[j]
        bubble_up(lst, j, 0)
    return lst


def insertion_sort(lst):
    n = len(lst)
    sorted = [lst[0]]
    for i in range(1, n, 1):
        for j in range(len(sorted) - 1, -1, -1):
            if lst[i] > sorted[j]:

                sorted.insert(j + 1, lst[i])
                break
            if j == 0:
                sorted.insert(0, lst[i])
    return sorted


def tester(func,number_of_loops,memory=False):
    timer = 0
    for x in range(number_of_loops):
        myrandom = random.sample(range(10000),10000)
        t = Timer(lambda: func(myrandom))
        time = t.timeit(number=1)
        timer = timer + time
    print(str(func), "took a average of", timer/number_of_loops , "s")
    if memory:
        tracemalloc.start()
        snapshot1 = tracemalloc.take_snapshot()
        func(lst)
        snapshot2 = tracemalloc.take_snapshot()
        top_stats = snapshot2.compare_to(snapshot1, 'lineno')
        print("[ Top 10 differences ]")
        for stat in top_stats[:10]:
            print(stat)
    pass

def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib((n - 1)) + fib((n - 2))

def upgradedfib(n):
    fiblst = list(range(n))
    for i in range(2,n):
        fiblst[i] = fiblst[i-1] + fiblst[i-2]
    return fiblst[-1]


def num_checker(lst):
    print(lst)
    for n in range(len(lst)-1):
        if lst[n] > lst[n+1]:
            print(lst[n])
    return lst

if __name__ == "__main__":
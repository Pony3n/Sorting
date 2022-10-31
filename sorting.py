
"""Сортировка!"""
def bubblesort(array):
    N = len(array)
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

print(bubblesort(array=[1, 2, 3, 10, 8, 7, 5, 2]))

def insertsort(array):
    N = len(array)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    return array
print(insertsort(array=[2, 10, 6, 5, 1, 3, 4]))

def selectionsort(array):
    N = len(array)
    for i in range(N - 1):
        m = array[i]
        p = i
        for j in range(i + 1, N):
            if m > array[j]:
                m = array[j]
                p = j
        if p != i:
            t = array[i]
            array[i] = array[p]
            array[p] = t
    return array

print(selectionsort(array=[3, 5, 1, 8]))

def merge_lists(array_1, array_2):
    result_list = []
    N = len(array_1)
    M = len(array_2)
    i = 0
    j = 0
    while i < N and j < M:
        if array_1[i] <= array_2[j]:
            result_list.append(array_1[i])
            i += 1
        else:
            result_list.append(array_2[j])
            j += 1
    result_list += array_1[i:] + array_2[j:]
    return result_list

def split_merge_lists(array):
    N1 = len(array) // 2
    array1 = array[:N1]
    array2 = array[N1:]
    if len(array1) > 1:
        array1 = split_merge_lists(array1)
    if len(array2) > 1:
        array2 = split_merge_lists(array2)
    return merge_lists(array1, array2)

print(split_merge_lists(array=[1, 2, 3, 10, 11, -7, -5, 4, -11]))
import random


def quick_sort(array):
    if len(array) > 1:
        x = array[random.randint(0, len(array) - 1)]
        low = [i for i in array if i < x]
        eq = [i for i in array if i == x]
        high = [i for i in array if i > x]
        array = quick_sort(low) + quick_sort(eq) + quick_sort(high)
    return array

print(quick_sort(array=[1, 2, 3, 10, 11, -7, -5, 4, -11]))





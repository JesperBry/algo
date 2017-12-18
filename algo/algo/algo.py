# -*- coding: utf-8 -*-

"""
Copyright 2017 JesperBry

https://github.com/JesperBry

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# imports
from sys import maxsize
from collections import defaultdict
from math import floor, log
from random import randint

# Help
def help():
    print('\n' + "-- List of function arguments --" + '\n' +
          "A = list/array" + '\n' +
          "p = start index (0)" + '\n' +
          "r = end index (len(A) - 1)" + '\n' +
          "B = min value of A (min(A))" + '\n' +
          "radix = Base of the number system or max value of A" + '\n' +
          "v = search value (bisect)" + '\n\n' +
          "All algorithms are based on the book; Introduction to algorithms by Cormen" + '\n'
          )

# Insertion-sort
def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A

# merge
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0]*(n1 + 1)
    R = [0]*(n2 + 1)
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]
    L[n1] = maxsize
    R[n2] = maxsize
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

# MERGE-Sort
def mergeSort(A, p, r):
    if p < r:
        q = (p + r)//2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)

# Bubble sort
def bubbleSort(A):
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A

# Bucket-Sort
def bucketSort(A):
    n = max(A)
    counts = [0]*(1+n)
    for i in A:
        counts[i] += 1
    sorted_A = []
    for j in range(0, len(counts)):
        sorted_A.extend([j]*counts[j])
    A[:] = sorted_A
    return sorted_A

# Counting-Sort
def countingSort(A, B, radix):
    count = defaultdict(int)
    for i in A:
        count[i] += 1
    result = []
    for j in range(B, radix+1):
        result += [j]*count[j]
    return result

# Heap-Sort
def heapSort(A):
    build_max_heap(A)

    for i in range(len(A) - 1, -1, -1):
        swap(A, 0, i)
        max_heapify(A, 0, i)

# -- START help functions --

def max_heapify(A, i, end):
    left = 2 * i + 1
    right = 2 * i + 2

    if left < end and A[left] > A[i]:
        largest = left
    else:
        largest = i

    if right < end and A[right] > A[largest]:
        largest = right

    if largest != i:
        swap(A, i, largest)
        max_heapify(A, largest, end)

def build_max_heap(A):
    for i in range(len(A) // 2 - 1, -1, -1):
        max_heapify(A, i, len(A))

def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

# -- END help functions --

# Quicksort
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

# Radix-Sort
def radixSort(A, radix):
    k = max(A)
    out = A
    d = int(floor(log(k, radix) + 1))
    for i in range(d):
        out = countingSort(out, i, radix)
    return out

# Randomized-Quicksort
def randomized_Partition(A, p, r):
    i = randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def randomized_Quicksort(A, p, r):
    if p < r:
        q = randomized_Partition(A, p, r)
        randomized_Quicksort(A, p, q - 1)
        randomized_Quicksort(A, q + 1, r)

# Binary search
def bisect(A, p, r, v):
    i = p
    if p < r:
        q = (p + r)//2
        if v <= A[q]:
            i = bisect(A, p, q, v)
        else:
            i = bisect(A, q + 1, r, v)
    return i

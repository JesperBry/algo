<p align="center"> 
  <img src="https://github.com/JesperBry/algo/blob/master/icon/Logo.png" width="400" height="150">
</p>

#

![:crocodile:](https://www.emojibase.com/resources/img/emojis/hangouts/1f40a.png) 

A Python package with the most common sorting algorithms.

All algorithms are based on the book: Introduction to algorithms by Cormen.

algo is based on the repo: [Algorithms from course TDT4120](https://github.com/JesperBry/-course-TDT4120---Algorithms)

| Algorithm             | WC             | AC/E      | Stable?   |
| --------------------- |:--------------:| ---------:| ---------:|
| [INSERTION-Sort](https://github.com/JesperBry/-course-TDT4120---Algorithms#insertion-sort)              | Θ(n^2)         | Θ(n^2)    | Yes |
| [MERGE-Sort](https://github.com/JesperBry/-course-TDT4120---Algorithms#merge-sort)                      | Θ(n lg n)        | Θ(n lg n)   | Yes |
| [Binary search](https://github.com/JesperBry/-course-TDT4120---Algorithms#binary-search)                | Θ(lg n)         | Θ(lg n)    | - |
| [Quicksort](https://github.com/JesperBry/-course-TDT4120---Algorithms#quicksort)                        | Θ(n^2)         | Θ(n lg n)*  | Usually not*** |
| [Randomized-Quicksort](https://github.com/JesperBry/-course-TDT4120---Algorithms#randomized-quicksort)  | O(n lg n)        | O(n lg n)   | Usually not*** |
| [Counting-Sort](https://github.com/JesperBry/-course-TDT4120---Algorithms#counting-sort)                | Θ(n+k)         | Θ(n+k)    | Yes |
| [Radix-Sort](https://github.com/JesperBry/-course-TDT4120---Algorithms#radix-sort)                      | Θ(d(n+k))      | Θ(d(n+k)) | Yes**** |
| [Bucket-Sort](https://github.com/JesperBry/-course-TDT4120---Algorithms#bucket-sort)                    | Θ(n^2)         | Θ(n)**    | Yes |
| [Heap-Sort](https://github.com/JesperBry/-course-TDT4120---Algorithms#heap-sort)                        | O(n lg n)        | O(n lg n)   | No |

*Expected, Randomized-Quicksort

**Average-case

***Most quicksort implementations are not stable, though stable implementations do exist.

****LSD requires stability, MSD does not

## Web-page
(https://jesperbry.github.io/algo/)

## Getting Started

### Installing

```
pip install algo
```

### Testing

```python
# -*- coding: utf-8 -*-

import algo.algo

algo.algo.help()

A = [27, 4, 15, 9, 110, 0, 13, 25, 1, 17, 802, 66, 25, 45, 97, 9]

algo.algo.mergeSort(A, 0, len(A)-1)
print(A)
```

Result:
```
-- List of function arguments --
A = list/array
p = start index (0)
r = end index (len(A) - 1)
B = min value of A (min(A))
radix = Base of the number system or max value of A
v = search value (bisect)

All algorithms are based on the book; Introduction to algorithms by Cormen

[0, 1, 4, 9, 9, 13, 15, 17, 25, 25, 27, 45, 66, 97, 110, 802]
```

## Built With
* [Python 3.5.2](https://www.python.org/)

## License
[LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

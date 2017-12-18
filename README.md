
# :crocodile: algo

A Python package with the most common sorting algorithms.
All algorithms are based on the book: Introduction to algorithms by Cormen.

## Web-page
```
https://jesperbry.github.io/algo/
```

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

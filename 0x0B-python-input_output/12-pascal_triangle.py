#!/usr/bin/python3
"""triangle pascale"""


def pascal_triangle(n):
    """pascal triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    for j in range(1, n):
        r = [1]
        for k in range(1, j):
            r.append(triangle[j-1][k-1] + triangle[j-1][k])
        r.append(1)
        triangle.append(r)

    return triangle

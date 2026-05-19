import math


def square(x):

    s = x ** 2

    return (s)


x = float(input())

result = square(x)

rounded = math.ceil(result)

print(rounded)

# Ian Fletcher
# CST-305
# 4/9/2023
# This is my own work

# imports necessary libraries
import numpy as np
import matplotlib.pyplot as plt


# function that takes in a value for x and returns results from part 1a
def part1a(x):
    return 1 - x - ((1/3) * x**3) + (-(1/12) * x**4)


# function that takes in a value for x and returns results from part 1b
def part1b(x):
    return (-(11/2) * (x-3)**2) + (34 * x) - (93/2)


# function that takes in values for a0, a1, and x and returns results from part 2
def part2(a0, a1, x):
    return a0 + (a1 * x) + (-(1/8) * a0 * x**2) + (-(1/24) * a1 * x**3) + ((1/128) * a0 * x**4) +\
        ((7/1920) * a1 * x**5) + (-(13/15360) * a0 * x**6) + (-(7/15360) * a1 * x**7) +\
        ((403/3440640) * a0 * x**8) + ((301/4423680) * a1 * x**9) + ((-22971/1238630400) * a0 * x**10)


# Generate 100 values for x between 0 and 100
x = np.linspace(0, 100, 100)

# sets y equal to results from part1a given x
y = part1a(x)
# plots results of part1a
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(3.5, -29.297, 'ro')
plt.title('Part 1a')
plt.show()

# sets y equal to results from part1b given x
y = part1b(x)
# plots results of part1b
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Part 1b')
plt.show()

# sets y equal to results from part2 given a0 = 1, a1 = 1, and x
y = part2(1, 1, x)
# plots results of part2
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Part 2')
plt.show()

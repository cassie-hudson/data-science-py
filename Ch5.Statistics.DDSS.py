from __future__ import division

#INTRODUCTION

#histogram of friend counts

from collections import Counter
from matplotlib import pyplot as plt
import math


num_friends = [23, 56, 47, 89, 45, 12, 13,5, 87, 14, 16,
               17, 65, 66, 89, 33, 47, 13, 24, 54, 17, 34, 100]
friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title('Histogram of Friend Counts')
plt.xlabel('# of friends')
plt.ylabel('# of people')
plt.show()

num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

#CENTRAL TENDENCIES

def mean(x):
    return sum(x)/len(x)

mean(num_friends)

def median(v):
    '''finds the middle value of v'''
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        #if odd, return the middle value
        return sorted_v[midpoint]
        print midpoint
    else:
        #if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        print (sorted_v[lo] + sorted_v[hi])/2



median(num_friends)

#DISPERSION

def vector_sum(vectors):
    '''sums all corresponding elements'''
    result = vectors[0] #start with the first vector
    for vector in vectors[1:]: #loops over all the other vectors
        result = vector_add(result, vector) #add the vectors to the result
    return result


def vector_sum(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    '''c is number, v is a vector'''
    return[c * v_i for v_i in v]

#compute means of a list of the same-sized vectors
def vector_mean(vectors):
    '''compute the vector whose ith element is the mean of the ith element of the input vectors'''
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

#dot product--sum of the componentwise product

def dot(v, w):
    '''v_1 * w_1 + v_n * w_n'''
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    '''v_1 * v_1...v_n * v_n'''
    return dot(v, v)

def data_range(x):
    return max(x) - min(x)

data_range(num_friends)

def de_mean(x):
    '''translate x by subtracting its mean (so the result has mean 0)'''
    x_bar = mean(x)
    return[x_i - x_bar for x_i in x]

def variance(x):
    '''assumes x has at least 2 elements'''
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations)/n - 1

print variance(num_friends)

def standard_deviation(x):
    return math.sqrt(variance(x))

standard_deviation(num_friends)
#def interquartile_range(x):
    #return quantile(x, 0.75) - quantile(x, 0.25)

#interquartile_range(num_friends)

#CORRELATION

daily_minutes = [27, 18, 93, 45, 12, 86, 14, 100, 77, 33, 23, 43, 56, 65, 56, 13, 86, 13, 15, 63, 91, 32, 1]

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)

covariance(num_friends, daily_minutes)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0

correlation(num_friends, daily_minutes)

#outliers

outlier = num_friends.index(100)
num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]

daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]

correlation(num_friends_good, daily_minutes_good)

#SIMPSON'S PARADOX
#the correlation is misleading because confounding variables are ignored


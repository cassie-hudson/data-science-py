#EXAMPLE: FLIPPING A COIN

import math

def normal_approximation_to_binomial(n, p):
    '''finds mu and sigma corresponding toa binomial(n, p)'''
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

#whenever a random variable follows a normal distribution we can use a normal_cdf to figure
#out the probability that it's realized value lies within a particular interval

#the normal_cdf is the probability the variable is below a threshold
normal_probability_below = normal_cdf

#it's above the threshold it it's not below the threshold

def normal_probability_above(lo, mu =0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

#it's between it it's less than hi, but not less than lo

def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

#it's outside if it's not between
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)
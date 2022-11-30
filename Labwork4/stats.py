# mystats.py : the module with the personal stats functions
import numpy as np
import matplotlib.pyplot as plt
# mean(x): returns the mean of the one-dimensional array x
def mean(x):
    return np.mean(x)


# variance(x): returns the variance of the one-dimensional array x
def variance(x):
    return np.var(x)


# covariance(x,y): returns the covariance of the one-dimensional array x and y
def covariance(x, y):
    return np.cov(x, y)


# median(x): returns the median of the one-dimensional array x
def median(x):
    return np.median(x)


# regression(x,y): returns a list [a,b] where y=ax+b is the linear regression of y on x
def regression(x, y):
    a = (len(x) * np.sum(x * y) - np.sum(x) * np.sum(y)) / (
        len(x) * np.sum(x * x) - np.sum(x) ** 2
    )
    b = (np.sum(y) - a * np.sum(x)) / len(x)
    return [a, b]


# Tests
w = np.asarray([0.0, 12.0, 13.0, 99.0])
print("Median = " + str(median(w)))
x = np.asarray([2.0, 6.0, 10])
print("Mean = " + str(mean(x)))
print("Variance = " + str(variance(x)))
print("Median = " + str(median(x)))
y = np.asarray([1.0, 20.0, 15.0])
print("Covariance of " + str(x) + " and " + str(y) + " =" + str(covariance(x, y)))
[a, b] = regression(x, y)
print(
    "The regression line of " + str(y) + "on " + str(x) + "has the equation :\n",
    "y=" + str(a) + "*x+" + str(b),
)

# Test to a random numpy array
x = np.random.random_sample(15)
print(x)
print("Mean = " + str(mean(x)))
print("Variance = " + str(variance(x)))
print("Median = " + str(median(x)))
y = np.random.random_sample(15)
print(y)
print("Covariance of " + str(x) + " and " + str(y) + " = " + str(covariance(x, y)))
[a, b] = regression(x, y)
print(
    "The regression line of" + str(y) + "on" + str(x) + "has the equation :\n",
    "y=" + str(a) + "*x+" + str(b),
)

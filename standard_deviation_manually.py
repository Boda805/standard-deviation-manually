from numpy import array
from numpy import std

#example data in a list
data = [86, 75, 76, 91, 65, 67, 80, 78, 86, 88]

#number of data points in list
n = 10

#calculating mean
mean = sum(data) / n

#getting relevant data into arrays
data_array = array(data)
mean_array = array(mean)

#steps to calculating variance/standard deviation
step1 = data_array - mean_array
step2 = step1 ** 2
step3 = sum(step2)

#var=variance, sd=standard deviation
var = step3 / n
sd = var ** .5

#sd calculated compared to std method
print(sd)
print(std(data))

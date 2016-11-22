# SoftMax
scores = [3.0, 1.0, 0.2]


# numpy is a library where math functions can be found
import numpy as np

def softmax(x):
	# finction np.exp() returns e in degree x
	# np.summ() returns the summ of all meanings in an array, axis = 0 means that the array has one dimention
	y = np.exp(x) / np.sum(np.exp(x), axis = 0) 
	return y



# Plot softmax curves
# matplotlib is a library for graphical representation of math functions
import matplotlib.pyplot as plt

# np.arange - returns spased values wothin a given interval, the first two args are the interval, the third is the step size 
x = np.arange(-2.0, 6.0, 0.1)

# np.ones_like(x) - returns an array, containing only 1s, which has the same value and shape as the given array
scores = np.vstack([x, np.ones_like(x), 0.2*np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth = 2)
plt.show

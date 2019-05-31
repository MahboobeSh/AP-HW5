import numpy as np

def func(input):
  print(np.unique(input[np.where(input & 6 == 0) and input % 6 == 0]))

a = np.array([3, 4, 1, 37, 21, 18, 23, 21, 27, 22, 43, 21])
func(a)

b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12])
func(b)
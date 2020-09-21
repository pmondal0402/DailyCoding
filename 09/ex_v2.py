import numpy as np
def isPossible(a):
  """
  Nondecreasing array by modifying atmost one element
  """
  print('min', min(abs(np.diff(a))))
  ind = 0
  for i in range(len(a)-1):
    if a[i] > a[i +1]:
      print(a[i])
      if (ind == 0):
        a[i] = a [i+1]-1
        ind = ind + 1
  # Figure out which element to replace and with what  
  # Compare with other two values and replace whichever has min difference
  if (sorted(a) == a):
    return True
  else:
    return False
  return False

a = [4, 2, 3]
# b = isPossible(a) 
# print(isPossible(a))
a2 = [5, 7, 1, 8]
print(isPossible(a2))
# The solution is incomplete
# Look at the link below for sol :
# https://www.geeksforgeeks.org/check-whether-an-array-can-be-made-strictly-decreasing-by-modifying-at-most-one-element/


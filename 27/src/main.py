from random import random
import numpy as np

N = 120000 # Total number of points

# The origin is chosen as center of circle
# Note Area of circle = pi r^2 and area of square is 4r^2.
# So ratio of area is pi/4.

r1 = 5 # Radius of circle

inside = 0 
for sample in range(N):
   # Choose a random point x,y
   x = r1*random()
   y = r1*random()
   
   # print(x, y)
   # Is the point inside the circle ? 
   random_dist = np.sqrt(x**2 + y**2)
   if random_dist < r1:
     inside += 1
     
# Compute pi = 4*ratio of points inside circle/total
pi_val = 4 * inside / N
print('Value of pi is', pi_val)
    

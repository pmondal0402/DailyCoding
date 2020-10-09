from math import sqrt
from itertools import count, islice
import numpy as np

class Solution:
   def countPrime(self, n):
      # Two different ways to find prime numbers
      # method 1 is accurate but slow
      # Method 2 is accurate and fast

      """
      # Method 1
      def isPrime(n):
          return n > 1 and all(n % i for i in islice(count(2), 
                                            int(sqrt(n) - 1))) 
      """
 
      # Method 2
      def isPrime(n):
          if n % 2 == 0 and n > 2: 
             return False
          return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))  

      def getPrimeList(n):
         # If n = 0, 1, return 0 
         if n  == 0 or n == 1:
            return 0
         else:
             # else count total prime numbers
             prime_num = []
             for i in range(2, n+1):
                if isPrime(i):
                   prime_num.append(i)
                   # print(i)
             return len(prime_num)
   
      return getPrimeList(n)

n1 = 1500000
sol = Solution()
print(sol.countPrime(n1))


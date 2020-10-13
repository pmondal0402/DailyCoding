from itertools import permutations

class Solution:
  def buddystring(self, A, B):
         # Get all possible permutations of sting A
         permA = list(set(permutations(A)))   
         permA_v2 = []
         for ii in range(len(permA)):
             s=""
             s = s.join(permA[ii])
             permA_v2.append(s)
   
         # Remove element A from permA     
         permA_v2.remove(A)
         
         return any( item == B for item in permA_v2) 
   
# A = "aa"
# B = "aa"
# Ans : True

# A = "aaaaaaabc"
# B = "aaaaaaacb"
# Ans. True

# A=""
# B = "aa"
# Ans. False

# A="ab"
# B = "ba"
# Ans. True

A = "ab"
B = "ab"

sol = Solution()
print(sol.buddystring(A, B))

import primefac

class Solution:
  def isUgly(self, num):
    fac_list = [2, 3, 5]
    # Is the number positive
    if num > 0 :
      # 1 is typically treated as an ugly number.
      if num == 1:
         return True
      else:
         # Get prime factors of the num
         pfactors =  list(primefac.primefac(num))
         # Remove any duplicate factors such as [2, 2] for num = 4
         pfactors = list(set(pfactors))
         # Remove 2, 3, 5 and check if the list has 
         # any other element left 
         # If yes then return True
         for item in fac_list:
            if item in pfactors:
              print(str(item) + 'is a factor')
              pfactors.remove(item)

         if len(pfactors) == 0:
            print('This is an ugly number')
            return True

    return False
    

# num = 1
# num = 6
num = 14

sol = Solution()
print(sol.isUgly(num))

class Solution:

  def flowerbed(self, lst, n):
      """
      Find an empty spot and check if the site before 
      and after are empty and count such spots
      """
      empty = 0
      empty_detec = 0 
      for it, item in enumerate(lst):
         # Find an empty spot and check if spots on left and 
         # right are empty
         
         # Considering only sites from 1 to N-1
         if empty_detec ==1:
            empty_detec = 0 
            # If an empty spot was detected in previous spot pass
            continue
         print(it) 
         if it > 0 and it < len(lst)-1:
            if item == 0:
               if lst[it-1] == 0 and lst[it+1] == 0:
                  empty +=1
                  empty_detec = 1

         # Check for first and last site availability
         if it == 0:
            if item == 0 and len(lst) >=2:
               if lst[it+1] == 0:
                  empty +=1
                  empty_detec = 1
         if it == len(lst)-1:
            if item == 0:
               if lst[it -1] == 0:
                  empty +=1
                  empty_detec = 1
         if len(lst) == 1 and lst[it] == 0:
                 empty +=1
                 empty_detec = 1

      return ( n <= empty )

# lst = [1,0,0,0,1]
# lst = [1,0,0,0,0,1]
# lst = [1,0,0,0,1,0,0]
# lst = [0, 0, 0]
# lst = [0, 0]
lst = [0]
n = 1
sol = Solution()
print sol.flowerbed(lst, n)

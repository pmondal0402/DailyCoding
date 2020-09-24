class Solution:
  def convertToTitle(self, n):
    
    capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    # out : ['A', 'B', 'C', 'D', 'E', 'F', ... ]
    results = []
    while n > 0:
      # append capitals[ind] where ind is remainder(ind/26) --> ind % 26 
      results.append(capitals[(n-1)%len(capitals)])
      # Truncate the loop when num reaches len(capitals)
      n = (n-1)//26 # returns bhagfol of bhag
    results.reverse()
    # Returns BA --> AB 
    return ''.join(results)

sol = Solution()
print(sol.convertToTitle(2))
print(sol.convertToTitle(28))

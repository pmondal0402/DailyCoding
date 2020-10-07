class Solution:
    def ThirdHighestNum(self, num_lst):
        # Remove duplicate 
        num_lst = list(set(num_lst))
        
        if len(num_lst) > 2 :
            # Get highest num and remove from list 
            for ii in range(2):
                num_lst.remove(max(num_lst))
            return max(num_lst)
        else:
            print "The third maximum does not exist,"\
                   " so the maximum is returned "\
                   "instead.", max(num_lst)    

            return max(num_lst)
    
num = [3, 2, 1] 
test = Solution().ThirdHighestNum(num)
num = [ 2, 1] 
test = Solution().ThirdHighestNum(num)
num = [2, 2, 3, 1] 
test = Solution().ThirdHighestNum(num)

print(test)

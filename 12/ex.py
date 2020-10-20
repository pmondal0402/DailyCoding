from itertools import groupby
import numpy.random as rnd

class Solution:
  def strongpassword(self, s):
    """
      s : inpit stirng
    """
    # It has at least 6 characters and at most 20 characters.
    def charlen(s):
      """
      Returns True if string has character min char
      of 6 and max char of 20
      """
      # print("len char : ", len(s))
      if len(s) >= 6 and len(s) <= 20 :
        return True
      else:
        print("Password must be atleast 6 char")
        return False

    def mod_charlen(s):
        # Add random integer between 0-9 to make it six character
        # An alternate would be to pick a random char from the string and add
        # in the end

        for ii in range(6-len(s)):
          s = s + str(rnd.randint(0, 9, size=1)[0])
        print("suggested password : ", s)
        return s

    def chkletter(s):
      """
      It must contain at least one lowercase letter, 
      at least one uppercase letter, and at least one digit
      """
      # Check if any char is lower case
      lw_wrd = any(l.islower() for l in s)

      # Check if any char is upper case
      up_wrd = any(u.isupper() for u in s)

      # Check if any char is digit
      dig = any(d.isdigit() for d in s)
     
      # Return true if all above conditions are satisfied
      if lw_wrd & up_wrd & dig:
        return True
      else:
        return False
       
       
    def chkrepeat(s):
      """
      It must NOT contain three repeating characters in a row
      Note : The function can differentiate between upper and lower cases
      """
      groups = groupby(s)
      result = [(label, sum(1 for _ in group)) for label, group in groups]
      repeat_char_len = [result[ii][1] for ii in range(len(result))]
      repeat_char_pos = any(i-2>0 for i in repeat_char_len)
      # print(repeat_char_pos)
      return repeat_char_pos

    def strngInptPsswrd(s):
      """
      returns 0 if all strong password requirements are met 
      """
      
      if charlen(s): 
           if chkletter(s) and not chkrepeat(s):
              # TODO
              # modify_chkletter 
              # modify_chkrepeat
              # print('You have a strong password')
              return "You have a strong password"
      else:
           return mod_charlen(s)


    return strngInptPsswrd(s)

# Test example
# Works for strong password check
# TODO
# Need to work on modification part 
string = "Gr2s61"# "grrree2Ss"
sol = Solution().strongpassword(string)
print(sol)
    

class Solution(object):

#Understand
# special character?
# time/space constraint?
# empty string?

#Match
# Two pointer

#Plan
# if character is non-alphanumeric then skip it
# compare left and right to see if same
# if not same return false
# if while loop ends return true

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        s=s.lower()
        print(s)
        while left < right :
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].isalnum() and s[right].isalnum() and s[left] != s[right]:
                return False
            left += 1
            right -=1
        return True
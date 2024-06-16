class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        low = 0
        high = len(s)-1
        while low < high:
            temp=s[low]
            s[low]=s[high]
            s[high]=temp
            low += 1
            high -= 1
        

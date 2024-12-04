class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        j = 0
        l1 = len(str1)
        l2 = len(str2) 
        if l2 >l1:
            return False
        while i < l1 and j < l2:
            
            ch1 = ord(str1[i])-ord('a')
            ch2 = ord(str2[j])-ord('a')
            if ch1 == ch2 or (ch1+1)%26 == ch2:
                i += 1
                j += 1
            else:
                i+=1
            

        if j == l2:
            return True
        return False
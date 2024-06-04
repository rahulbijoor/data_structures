class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht={}
        for i in range(0,len(s)):
            if s[i] in ht.keys():
                ht[s[i]]+=1
            else:
                ht[s[i]]=1
        sum=0
        isOdd = False
        for ky in ht.keys():
            if ht[ky] % 2 == 0 :
                sum+=ht[ky]
            else  :
                isOdd = True
                sum+=(ht[ky]-1)
        if isOdd is True:
            return sum+1
        return sum
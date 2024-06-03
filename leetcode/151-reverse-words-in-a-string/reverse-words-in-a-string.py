class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        reverse=words[::-1]
        result=''
        for w in reverse:
            result+=(w+' ')
        result=result.strip()
        return result
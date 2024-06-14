class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        i=0
        while i < len(s): 
            if s[i] == 'M':
                sum += 1000
            elif s[i] == 'D':
                sum += 500
            elif s[i] == 'C':
                if i+1 < len(s):
                    if s[i+1] == 'D':
                        sum += 400
                        i=i+1
                    elif s[i+1] == 'M':
                        sum += 900
                        i=i+1
                    else:
                        sum += 100
                else:
                    sum += 100
            elif s[i] == 'L':
                sum += 50
            elif s[i] == 'X':
                if i+1 < len(s):
                    if s[i+1] == 'L':
                        sum += 40
                        i+=1
                    elif s[i+1] == 'C':
                        sum += 90
                        i+=1
                    else:
                        sum += 10
                else:
                    sum += 10
            elif s[i] == 'V':
                sum += 5
            elif s[i] == 'I':
                if i+1 < len(s):
                    if s[i+1] == 'V':
                        sum += 4
                        i+=1
                    elif s[i+1] == 'X':
                        sum += 9
                        i+=1
                    else:
                        sum += 1
                else:
                    sum += 1
            i+=1
            
        return sum
            
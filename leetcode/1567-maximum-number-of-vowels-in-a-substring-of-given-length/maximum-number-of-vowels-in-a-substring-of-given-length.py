class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a', 'e', 'i', 'o', 'u'}
        numVowels=0

        for i in range(0,k):
            if s[i] in vowels:
                numVowels += 1

        maxNumVowels = numVowels
        i = 1
        while i <= len(s)-k:
            if s[i-1] in vowels:
                numVowels = numVowels - 1   
            if s[k+i-1] in vowels:
                numVowels = numVowels + 1
            if maxNumVowels < numVowels:
                maxNumVowels = numVowels
            i += 1    
        return maxNumVowels
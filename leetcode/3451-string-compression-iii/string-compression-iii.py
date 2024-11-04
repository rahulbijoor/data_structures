class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""
        
        result = ""
        count = 1
        lastc = word[0]
        
        for i in range(1, len(word)):
            if word[i] == lastc:
                count += 1
                if count == 10:
                    result += "9" + lastc
                    count = 1
            else:
                result += str(count) + lastc
                count = 1
                lastc = word[i]
            
        
        result += str(count) + lastc  # Append the last sequence
        return result

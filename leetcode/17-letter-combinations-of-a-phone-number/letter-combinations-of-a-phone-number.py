from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dictionary = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        res = ['']
        
        for digit in digits:
            temp_list = []
            for char in dictionary[digit]:
                for combination in res:
                    temp_list.append(combination + char)
            res = temp_list
        
        return res



class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split(" ")
        print(words)
        k = len(searchWord)
        for i in range(len(words)):

            if len(words[i]) >= k and searchWord == words[i][0:k]:
                return i+1
        return -1


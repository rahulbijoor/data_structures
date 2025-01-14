class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        count= 0
        for key,values in freq.items():
            if values%2 == 1:
                count += 1
            else:
                count += 2
        return count

        
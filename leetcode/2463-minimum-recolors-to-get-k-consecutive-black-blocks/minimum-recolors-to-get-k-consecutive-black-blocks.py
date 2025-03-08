class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countW=0
        i = 0
        while i<k:
            if blocks[i] == 'W':
                countW += 1
            i += 1
        minW = countW
        while i < len(blocks):
            if blocks[i] == 'W':
                countW += 1
            if blocks[i-k] == 'W':
                countW -= 1
            minW = min(minW, countW)
            i += 1
        return minW

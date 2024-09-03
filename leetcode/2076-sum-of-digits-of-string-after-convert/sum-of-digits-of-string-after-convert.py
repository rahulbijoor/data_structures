class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st=""

        for i in range(len(s)):
            st = st + str(ord(s[i])-ord("a")+1)
        print(st)
        while k > 0:
            sum = 0
            for ch in st:
                sum += int(ch)
            st = str(sum)
            k -= 1
        return int(st)

        
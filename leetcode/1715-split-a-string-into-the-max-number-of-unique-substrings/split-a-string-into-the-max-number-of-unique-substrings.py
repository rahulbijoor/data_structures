class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        sstr = set()

        def dfs(i, cur_set):
            if i == len(s):
                return 0
            
            res = 0
            for j in range(i,len(s)):
                curr = s[i:j+1]
                if curr not in sstr:
                    cur_set.add(curr)
                    res = max(res,1+dfs(j+1,cur_set))
                    cur_set.remove(curr)
            return res
        return dfs(0,sstr)

    
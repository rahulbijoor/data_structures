class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        curr = 1
        while len(res) < n:
            res.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr == n or curr%10 == 9:
                    curr = curr // 10
                curr += 1
        return res
        def dfs(cur):
            if cur > n:
                return 
            res.append(cur)
            cur *= 10
            for i in range(10):
                dfs(cur + i)
        
        #for i in range(1,10):
        #    dfs(i)
        return res
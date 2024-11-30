class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        n = len(arr) # size of array.

        pre, suff = 1, 1
        ans = float('-inf')
        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre *= arr[i]
            suff *= arr[n - i - 1]
            ans = max(ans, max(pre, suff))
        return ans
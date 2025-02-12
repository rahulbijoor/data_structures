class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        def sumdigits(num):
            sum_of_digits = 0
            while num > 0:
                digit = num % 10
                num //= 10
                sum_of_digits += digit
            return sum_of_digits
        
        for n in nums:
            sum_of_digits = sumdigits(n)
            d[sum_of_digits].append(n)
        res = -1
        for k in d.keys():
            if len(d[k]) <= 1:
                continue
            d[k].sort()
            res = max(res,d[k][-1]+d[k][-2])
        return res
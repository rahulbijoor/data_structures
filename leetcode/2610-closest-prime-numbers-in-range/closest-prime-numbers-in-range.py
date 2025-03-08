class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:


        def prime_range(left, right):
            is_prime = [True]*(right+1)
            is_prime[0] = is_prime[1] = False
            for n in range(2, int(sqrt(right))+1):
                if not is_prime[n]:
                    continue
                for m in range(n+n, right+1, n):
                    is_prime[m] = False
            primes = []
            for i in range(len(is_prime)):
                if is_prime[i] and i >= left:
                    primes.append(i)
            return primes
        diff =right - left +1
        res = [-1, -1]
        prime = prime_range(left,right)
        for i in range(1,len(prime)):
            if prime[i] -prime[i-1] <diff:
                diff =  prime[i] -prime[i-1]
                res = [prime[i-1], prime[i]]
        return res
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        numTrust = [0] * (n + 1)

        # Increase trust value of trustee and decrease trust value of truster for each pair
        for person1, person2 in trust:
            numTrust[person1] -= 1
            numTrust[person2] += 1
        
        # Check if anyone achieves n-1 trust. This person is the town judge
        for i in range(1, len(numTrust)):
            if numTrust[i] == n - 1:
                return i
        
        # If no one achieves n-1 trust, then there is no town judge
        return -1
            
            
        
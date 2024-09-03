class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtrack(k, n, start, path):
            # Base case: if k is 0 and n is 0, add the current path to result
            if k == 0 and n == 0:
                result.append(path[:])
                return
            
            # If k or n goes out of bounds, or start goes beyond 9, stop exploring
            if k <= 0 or n <= 0 or start > 9:
                return
            
            # Explore further numbers from `start` to 9
            for i in range(start, 10):
                path.append(i)  # Choose the number i
                backtrack(k - 1, n - i, i + 1, path)  # Explore with reduced k and n
                path.pop()  # Backtrack: remove the number i

        # Start backtracking with initial conditions
        backtrack(k, n, 1, [])
        return result
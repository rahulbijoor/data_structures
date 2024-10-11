class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count  = 0
        for l in logs:
            cmd = l.split("/")
            if cmd[0] == ".." :
                if count > 0:
                    count -= 1
                else:
                    continue
            elif cmd[0] == ".":
                continue
            else:
                count += 1

        return count
        

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for d in details:
            st = d[11:13]
            if int(st) > 60:
                count += 1
            print(st)
        return count
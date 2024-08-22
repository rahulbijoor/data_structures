class Solution:
    def findComplement(self, num: int) -> int:
        binNum = bin(num).replace("0b", "")
        print(binNum)
        result = ""
        for i in range(len(binNum)):
            if binNum[i] =="1":
                result += "0"
            else:
                result += "1"
        print(result)
        return int(result,2)
        
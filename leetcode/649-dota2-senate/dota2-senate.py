class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant=[]
        dire=[]
        for i in range(0,len(senate)):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while len(radiant) > 0 and len(dire) > 0:
            if radiant[0] < dire[0]:
                radiant.append(radiant.pop(0)+len(senate))
                dire.pop(0)
            else:
                dire.append(dire.pop(0)+len(senate))
                radiant.pop(0)

        if len(radiant) > 0:
            return "Radiant" 
        return "Dire"
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
                    dire.pop(0)
                    l=radiant.pop(0)
                    radiant.append(l+len(senate))
            else:
                    radiant.pop(0)
                    l=dire.pop(0)
                    dire.append(l+len(senate))
        
        if len(radiant) > 0:
            return "Radiant"
        else:
            return "Dire"
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        print(skill)
        left, right = 0, len(skill)-1
        total_sum = sum(skill)
        skill_sum = 0
        if total_sum % (len(skill)/2) != 0:
            return -1
        while left < right:
            if (skill[left]+skill[right]) != (total_sum / (len(skill)/2)):
                return -1
            skill_sum += (skill[left]*skill[right]) 
            left += 1
            right -= 1
        return skill_sum
class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        sum = 0
        for i in range(0,len(seats)):
            sum+=abs(seats[i]-students[i])
        return sum
        
        
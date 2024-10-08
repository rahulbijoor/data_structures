class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        numOnes = 0
        numZeros = 0
        for i in students:
            if i == 0:
                numZeros += 1
            else:
                numOnes += 1
        for j in sandwiches:
            if j == 1:
                if numOnes > 0:
                    numOnes -= 1
                else:
                    return numOnes+numZeros
            else:
                if numZeros > 0:
                    numZeros -= 1
                else:
                    return numOnes+numZeros
        return 0

        
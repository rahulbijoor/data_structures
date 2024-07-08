class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        i=1

        st=[num for num in range(1,n+1)]
        print(st)
        while len(st) > 1:
            i=(i+(k-2))%len(st)
            st.remove(st[i])
            i=(i+1)%len(st)
            
        return st[0]
        

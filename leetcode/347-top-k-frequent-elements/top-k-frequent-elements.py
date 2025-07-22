class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        fq = Counter(nums)
        r = sorted(fq.items(),key=lambda x: x[1], reverse=True)
        top_k = [item[0] for item in r[:k]]
        lst = [("a", 3), ("b", 1),("bc",2), ("c", 2)]
        print(sorted(lst, key=lambda x: len(x[0]),reverse = True))
        return top_k
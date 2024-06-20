class Solution(object):
    # Understand
    # Time / Space Complexity?
    # Empty Lists?
    # Non Decreasing order?

    # Match
    # Two sperarate pointers

    # Plan
    # traverse through the arrays
    # if array1[ele1] < array2[ele1]  array1 will be same ele1 += 1
    # else insert array2[ele2] into array1 at index ele1 ele2 += 1

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index1 = m - 1
        index2 = n-1
        insertIndex = m + n - 1
        while index2 >= 0:
            if index1 >= 0 and nums1[index1] > nums2[index2]:
                nums1[insertIndex] = nums1[index1]
                index1 -= 1
            else:
                nums1[insertIndex] = nums2[index2]
                index2 -= 1
            insertIndex -= 1
        return nums1

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
        ele1=0
        ele2=0
        while ele1 < m and ele2 < n :
            print(ele1 , ele2)
            if nums1[ele1] <= nums2[ele2]:
                ele1 += 1
                continue
            else:
                temp=nums1[ele1]
                nums1[ele1]=nums2[ele2]
                nums2[ele2]=temp
                ele1 += 1
        
        while ele2 < n:
            nums1[ele1]=nums2[ele2]
            ele1 +=1
            ele2 +=1
        
        nums1.sort()
        return nums1

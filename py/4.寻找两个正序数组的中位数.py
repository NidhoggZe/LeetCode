class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def findKthofArrays(nums1, nums2, k):
            k += 1
            head1 = 0
            head2 = 0
            while (True):
                if head1 == nums1.__len__():
                    return nums2[head2 + k-1]
                if head2 == nums2.__len__():
                    return nums1[head1 + k-1]
                if k == 1:
                    return min(nums1[head1], nums2[head2])

                deleten = k//2
                k1 = head1 + deleten - 1 
                if k1 >= nums1.__len__():
                    k1 = nums1.__len__() - 1
                k2 = head2 + deleten - 1
                if k2 >= nums2.__len__():
                    k2 = nums2.__len__() - 1

                if nums1[k1] < nums2[k2]:
                    k -= k1 - head1 + 1
                    head1 = k1 + 1
                else:
                    k -= k2 - head2 + 1
                    head2 = k2 + 1


        sum = nums1.__len__() + nums2.__len__()
        if sum%2 == 0:
            return (findKthofArrays(nums1, nums2, sum//2) + findKthofArrays(nums1, nums2, sum//2-1))/2

        else:
            return findKthofArrays(nums1, nums2, sum//2)

a = [1,2]
b = [3,4]
print(Solution().findMedianSortedArrays(a,b))
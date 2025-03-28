"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""

 
def medianA(nums1,nums2):
    merge=nums1+nums2
    merge.sort()
    n=len(merge)
    left=0
    right=len(merge)-1
    mid= (left+right) //2
    if n% 2==1:
        return float(merge[mid])
    else:
        m1=merge[mid+1]
        m2=merge[mid]
        return float((m1+m2)/2)

nums1=[1,3]
nums2=[2]
print(medianA(nums1,nums2))

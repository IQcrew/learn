def findMedianSortedArrays( nums1: list[int], nums2: list[int]) -> float:
    nums1 = sorted(nums1+nums2)
    nums2 = len(nums1)
    return (nums1[int(nums2/2-0.5)]+nums1[int(nums2/2+0.5)])/2 if nums2 %2 == 0 else nums1[int(nums2/2)]

print(findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4,4]))
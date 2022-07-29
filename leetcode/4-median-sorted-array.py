# https://leetcode.com/problems/median-of-two-sorted-arrays/

def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        out = []
        i = 0
        j = 0
        while (i < len(nums1) and j < len(nums2)):
            print(i,j)
            if nums1[i] < nums2[j]: 
                out.append(nums1[i])
                i += 1
            else: 
                out.append(nums2[j])
                j += 1
        
        while (i < len(nums1)):
            out.append(nums1[i])
            i += 1
        
        while (j < len(nums2)):
            out.append(nums2[j])
            j += 1
        
        # print(out, not len(out) % 2, (out[int(len(out) / 2)] + out[int(len(out) / 2) - 1]) / 2 )
        mid = int(len(out) / 2)
        return (out[mid] + out[mid-1]) / 2.0 if not len(out) % 2 else out[mid]

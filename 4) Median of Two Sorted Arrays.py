class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a1 = 0
        a2 = 0
        len1 = len(nums1)
        len2 = len(nums2)
        tot = len(nums1)+len(nums2)
        
        if tot % 2 == 0:
            # get the 2 middle nums
            ans = []
            for i in range(0,(tot//2)+1):
                # print(a1,a2)
                if a1 == len1:
                    # print("Enter 1")
                    if len(ans) == 2:
                        ans.pop()
                    ans.insert(0,nums2[a2])
                    a2 += 1
                elif a2 == len2:
                    # print("Enter 2")
                    if len(ans) == 2:
                        ans.pop()
                    ans.insert(0,nums1[a1])
                    a1 += 1
                elif nums1[a1] <= nums2[a2]:
                    # print("Enter 3")
                    if len(ans) == 2:
                        ans.pop()
                    ans.insert(0,nums1[a1])
                    a1 += 1
                else:
                    # print("Enter 4")
                    if len(ans) == 2:
                        ans.pop()
                    ans.insert(0,nums2[a2])
                    a2 += 1
                # print(a1,a2)
            # print(ans)
            return (ans[0]+ans[1])/2
            
        else:
            #get the middle number
            ans = -1
            for i in range(0,(tot//2)+1):
                if a1 == len1:
                    ans = nums2[a2]
                    a2 += 1
                elif a2 == len2:
                    ans = nums1[a1]
                    a1 += 1
                elif nums1[a1] <= nums2[a2]:
                    ans = nums1[a1]
                    a1 += 1

                else:
                    ans = nums2[a2]
                    a2 += 1
            return ans
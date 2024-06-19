""" 
https://leetcode.com/problems/merge-sorted-array/ 

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""

# this solution Runtime 119ms Beats 5.54%, Memory 16.82MB Beats 5.41%


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        print ("DEBUG - nums1:", nums1, "m:", m)
        print ("DEBUG - nums2:", nums2, " n:", n)
        print ("Total =", m+n)

        i = 0
        n2 = 0 


        del nums1[m:]
        print (nums1)

        while i <= m+n :
            
            print ("BEGIN", nums1, "/", nums2, "  i", i, end ="", )
            print (" - ",nums1, end =" ")
            print (" ",nums2, "m =", m, "n =", n, end =" ")

            if n == 0:
                print("Debug return n=0")
                return
             
            if len(nums1)<=i:
                print("len(nums1)<=i")
                nums1.insert(i,nums2[n2])
                nums2.pop(n2)

            elif nums1[i]>nums2[n2]:
                print (" ++ ", nums1[i], " > ",nums2[n2])
                nums1.insert(i,nums2[n2])
                nums2.pop(n2)
                m += 1
                n-= 1
 

            elif nums1[i]<nums2[n2]:
                print (" --  ", nums1[i], " < ",nums2[n2])

            else:
                print (" ?? else: ", nums1[i], " ? ",nums2[n2])
                nums1.insert(i+1,nums2[n2])
                nums2.pop(n2)
                m += 1
                n-= 1

            i +=1

            if i == m+n:
                print(" ---- i == m+n ----")
                return

        print("NORMAL EXIT AT THE END - while i <= m+n")
                       

        

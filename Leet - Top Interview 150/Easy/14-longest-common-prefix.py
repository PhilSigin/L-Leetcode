"""
14. Longest Common Prefix

https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

My stats:
Runtime 39ms  Beats 49.82%
Memory 16.92MB Beats 23.96%

One of elegant solutions:
    def longestCommonPrefix(self, v):
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 


Secret is to 
1) sort array
2) use only first and last cells as most different - but you have to remove all long strings first

"""



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        no_of_strs = len(strs)
        
        """
        max_l = 200
        for i in range (no_of_strs):
            cur_l = len(strs[i])
            if max_l > cur_l:
                max_l = cur_l
        """
        max_l = len(min(strs))
    

        if max_l == 0:
            return ""


        cur_l = 0
        
        newstrs  = []

        for i in range (1,(max_l+1)):
            newstrs = [x[0:i] for x in strs]
            print (newstrs)
            for test in range(1, no_of_strs) :
                if newstrs[0] != newstrs[test]:
                    prefix = newstrs[0]
                    return prefix[0:cur_l]
            cur_l +=1


        prefix = newstrs[0]
        return prefix[0:cur_l]
            



        

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        #loop through each character index of the first string
        for i in range(len(strs[0])):
            # check if this character is the same in all strings
            for s in strs[1:]:
                # if we reach the end of any string or the character doesn't match
                # we return the common prefix found so far
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]

# Example usage:
# sol = Solution()
# print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"    
# print(sol.longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""
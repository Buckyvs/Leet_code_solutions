class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]

# Example usage:
# sol = Solution()
# print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"    
# print(sol.longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""
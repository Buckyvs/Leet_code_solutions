class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        removeSpaces = s.strip()
        words = removeSpaces.split()

        if len(words) == 0:
            return 0
        else:
            return len(words[-1]) 
# Example usage:
# sol = Solution()
# print(sol.lengthOfLastWord("Hello World"))  # Output: 5
# print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
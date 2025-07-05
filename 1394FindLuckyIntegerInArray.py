class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        lucky = -1

        for num in freq:
            if num == freq[num]:
                lucky = max(lucky, num)

        return lucky 
# Example usage:
# sol = Solution()
# print(sol.findLucky([2, 2, 3, 4]))  # Output: 2
# print(sol.findLucky([1, 2, 3, 4]))  # Output: -1
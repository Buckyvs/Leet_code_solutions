class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 1
        while fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow+1] = nums[fast]
                fast += 1
                slow += 1
        return slow + 1
# Example usage:
# sol = Solution()
# print(sol.removeDuplicates([1, 1, 2]))  # Output: 2                   
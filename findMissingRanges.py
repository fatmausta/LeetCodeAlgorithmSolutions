# Leetcode #163 Easy - Missing Ranges

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if len(nums) == 0:
            if upper == lower:
                return ["{}".format(upper)]
            else:
                return ["{}->{}".format(lower, upper)]
        output = []

        if lower != nums[0]:
            nums.insert(0, lower-1)
        if upper != nums[-1]:
            nums.extend([upper + 1])

        diff_list = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        for ix, diff in enumerate(diff_list):
            if diff == 2:
                output.append("{}".format(nums[ix] + 1))
            elif diff > 2:
                output.append("{}->{}".format(nums[ix] + 1, nums[ix + 1] - 1))

        return output

sln = Solution()
# print(sln.findMissingRanges([1, 2, 4, 15], 0, 20))
print(sln.findMissingRanges([], 0, 0))
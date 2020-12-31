# LeetCode #1 Easy - Two Sum
class Solution:
    def twoSum(self, nums, target):
        hash_table = {}
        for i, num in enumerate(nums):
            dif = target - num
            keys = list(hash_table.keys())
            if dif in keys:
                return [i, hash_table[dif]]
            hash_table[dif] = i
        return [-1, -1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sln = Solution()
    result = sln.twoSum([1,3,5,7], 8)
    print(result)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

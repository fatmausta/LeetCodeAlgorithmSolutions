# Leetcode 266 - Easy - Palindrome Permutation
class Solution(object):
    def canPermutePalindrome(self, str):
        """
        :type str: str
        :rtype: bool
        """
        map = {}
        for s in str:
            if s in map:
                map[s] += 1
            else:
                map[s] = 1
        map_val = list(map.values())
        map_val = [m%2 for m in map_val]
        if sum(map_val) == 0 or sum(map_val) == 1:
            return True
        else:
            return False


sln = Solution()
print(sln.canPermutePalindrome("abccgaapba"))
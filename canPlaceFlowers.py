# LeetCode #605 Easy - Can Place Flowers

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        bed_size = len(flowerbed)
        # n can be at max size-1
        if bed_size == 1 and flowerbed[0] == 0:
            if n<=1:
                return True
        if n > bed_size:
            return False
        # count zeros in a row
        adjacent_zeros = 0
        n_allowed_places = 0
        for i, f in enumerate(flowerbed):
            if f == 0:
                if i == 0 or i == len(flowerbed)-1:
                    adjacent_zeros+=2
                    continue
                else:
                    adjacent_zeros += 1
                    continue
            if adjacent_zeros <= 2:
                adjacent_zeros = 0
                continue
            if adjacent_zeros % 2 == 1:
                n_allowed_places += (adjacent_zeros - 1) / 2
            else:
                n_allowed_places += (adjacent_zeros - 2) / 2
            adjacent_zeros = 0

        if i == len(flowerbed)-1 and adjacent_zeros!=0:
            if adjacent_zeros % 2 == 1:
                n_allowed_places += (adjacent_zeros - 1) / 2
            else:
                n_allowed_places += (adjacent_zeros - 2) / 2

        return int(n_allowed_places) >= n


sln = Solution()
print(sln.canPlaceFlowers([0], 1))
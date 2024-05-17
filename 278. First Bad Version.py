# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:

        low = 0
        high = n
        mid = 0

        while low < high:
            
            mid = (high + low) // 2

            # ignore right half if true
            if isBadVersion(mid) == True:
                high = mid
            # else ignore left half (first bad version could be mid)
            else:
                low = mid + 1

        return high


def isBadVersion(int):
    if int >= 4:
        return True
    else:
        return False


solution = Solution()
n = 5
print(solution.firstBadVersion(n))
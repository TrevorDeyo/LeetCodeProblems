class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))

        return score


solution_object = Solution()
if solution_object.scoreOfString("hello") == 13:
    print("Passed")

if solution_object.scoreOfString("zaz") == 50:
    print("Passed")
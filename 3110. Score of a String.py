class Solution:
    def scoreOfString(self, s: str) -> int:
        counter = 0
        score = 0
        ascii_values = []
        for char in s:
            ascii_values.append(ord(char))
            if counter > 0:
                score += abs(ascii_values[counter] - ascii_values[counter - 1])
            counter += 1

        return score


solution_object = Solution()
if solution_object.scoreOfString("hello") == 13:
    print("Passed")

if solution_object.scoreOfString("zaz") == 50:
    print("Passed")
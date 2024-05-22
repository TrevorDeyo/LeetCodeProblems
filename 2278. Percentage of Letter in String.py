class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        

        hitCounter = 0
        stringLength = len(s)
        for char in s:
            if char == letter:
                hitCounter += 1

        
        return int((hitCounter / stringLength) * 100)




solution = Solution()

if solution.percentageLetter(s='foobar', letter='o') == 33:
    print("Passed")

if solution.percentageLetter(s='jjjj', letter='k') == 0:
    print("Passed")
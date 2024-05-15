from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # for each num in array
        # find how many nums in the array are smaller
        answer = []
        # nums.sort()

        for num in nums:
            counter = 0
            for num2 in nums:
                if num > num2:
                    counter += 1
            answer.append(counter)

        return answer

solution = Solution()

if solution.smallerNumbersThanCurrent([8,1,2,2,3]) == [4,0,1,1,3]:
    print("Passed")
else:
    print("Failed")

if solution.smallerNumbersThanCurrent([6,5,4,8]) == [2,1,0,3]:
    print("Passed")
else:
    print("Failed")

if solution.smallerNumbersThanCurrent([7,7,7,7]) == [0,0,0,0]:
    print("Passed")
else:
    print("Failed")
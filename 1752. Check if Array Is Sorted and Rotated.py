from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:

        # Grab min number
        nums_min = min(nums)
        
        # find all indices of the min number in the nums list
        indices = [i for i, x in enumerate(nums) if x == nums_min]
        
        # get the last occurence of the nums_min int
        nums_min_index = indices[-1]

        # rotate the list so that the last occurence of the min number starts the list
        nums_rotated = nums[nums_min_index:] + nums[:nums_min_index]

        # to keep track of the last num
        prev_num = 0

        # go through the list to see if they are in ascending order
        for num in nums_rotated:
            if prev_num <= num:
                prev_num = num
            
            elif num == nums_min:
                continue
            else:
                return False
        return True

solution = Solution()
if solution.check([3,4,5,1,2]):         # true
    print("Passed")
else:
    print("Failed")                   


if not solution.check([2,1,3,4]):        # false
    print("Passed")
else:
    print("Failed")          

if solution.check([1,2,3]):               # true
    print("Passed")
else:
    print("Failed")     

if solution.check([6,10,6]):              # true
    print("Passed")
else:
    print("Failed")     

if not solution.check([1,4,1,2,3,5]):     # false
    print("Passed")
else:
    print("Failed")     

if solution.check([7,9,1,1,1,3]):          # true
    print("Passed")
else:
    print("Failed")     
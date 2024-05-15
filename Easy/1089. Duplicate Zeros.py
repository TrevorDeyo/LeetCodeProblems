from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr2 = arr[:]
        counter = -1
        for element in arr:
            if counter <= len(arr):
                counter += 1
                if element == 0:
                    counter += 1
                    arr2.insert(counter, 0)

        arr[:] = arr2[:len(arr)]
        
solution = Solution()

arr = [1,0,2,3,0,4,5,0]

arr = [1,0,2,3,0,4,5,0]
solution.duplicateZeros(arr)
print(arr)
if arr == [1,0,0,2,3,0,0,4]: print("Pass")
else: print("fail")
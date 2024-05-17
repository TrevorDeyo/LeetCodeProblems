class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        
        return




sol = Solution()

if sol.vaildPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2):
    print("Passed")

if not sol.vaildPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5):
    print("passed")

from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:


        # Build adjList
        adjList = {}
        for a, b in edges:
            if a in adjList: adjList[a] += [b]
            else: adjList[a] = [b]
            if b in adjList: adjList[b] += [a]
            else: adjList[b] = [a]
        


        while(true):

        return 




sol = Solution()

if sol.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2):
    print("Passed")

if not sol.validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5):
    print("passed")


from typing import List
from collections import deque
import collections

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Build adjacency list
        graph = collections.defaultdict(list)  # Initialize an empty list for each node
        for a, b in edges:
            graph[a].append(b)  # Add b to the adjacency list of a
            graph[b].append(a)  # Add a to the adjacency list of b (since it's an undirected graph)

        # Perform BFS
        visited = set()  # Set to keep track of visited nodes
        queue = deque([source])  # Initialize the queue with the source node
        while queue:
            current_node = queue.popleft()  # Get the next node from the queue
            if current_node == destination:
                return True  # If we reach the destination, return True
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)  # Add unvisited neighbors to the queue
                    visited.add(neighbor)  # Mark the current node as visited
        return False  # If we didn't find a path to the destination, return False

sol = Solution()

if sol.validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2):
    print("Passed")

if not sol.validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5):
    print("Passed")

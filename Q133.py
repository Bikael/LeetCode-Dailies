from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        print(self.bfs(node))

    def bfs(self, node):
        if not node:
            return

        queue = deque()
        queue.append(node)

        visited = {}
        visited[node] = 

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return visited
        




# Create the nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Connect the nodes
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Create solution object
solution = Solution()

# Pass node1 into the function
result = solution.cloneGraph(node1)
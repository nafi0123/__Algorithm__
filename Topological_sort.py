from typing import List
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        adj=[[] for _ in range(numCourses)]


        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1

        topOrder=[]

        q=deque([i for i in range(numCourses) if indegree[i]==0] )

        while q:
            node=q.popleft()
            topOrder.append(node)

            for n in adj[node]:
                indegree[n]-=1
                if indegree[n] == 0:
                    q.append(n)
        if numCourses==len(topOrder):
            return topOrder
        else:
            return "Graph contains a cycle. Topological sort not possible."
s=Solution()
print(s.findOrder(2,[[1,0]]))
        

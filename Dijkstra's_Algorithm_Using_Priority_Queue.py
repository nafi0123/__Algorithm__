import heapq

class Solution:
    def dijkstra(self, V, adj, S):
        pq = []
        
        dist_to = [float('inf')] * V

        dist_to[S] = 0
        heapq.heappush(pq, (0, S))

        while pq:
            dis, node = heapq.heappop(pq)

            for neighbor in adj[node]:
                v, w = neighbor
                if dis + w < dist_to[v]:
                    dist_to[v] = dis + w
                    heapq.heappush(pq, (dist_to[v], v))

        return dist_to

if __name__ == "__main__":
    V, S = 3, 2
    adj = [[] for _ in range(V)]
    adj[0].append([1, 1])
    adj[0].append([2, 6])
    adj[1].append([2, 3])
    adj[1].append([0, 1])
    adj[2].append([1, 3])
    adj[2].append([0, 6])

    obj = Solution()
    res = obj.dijkstra(V, adj, S)
    print(" ".join(map(str, res)))

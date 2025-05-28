class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        m = len(edges1)+1
        n=len(edges2)+1

        adj1 = [[] for i in range(m)]
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        adj2 = [[] for i in range(n)]
        for u,v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        best_val = 0
        for i in range(n):
            connections = self.BFS(i,adj2,k-1)
            best_val = max(best_val, connections)
        
        result = []
        for i in range(m):
            connections = self.BFS(i,adj1,k)
            result.append(connections+best_val)
        return result

    def BFS(self, start, adj, k):
        q=deque()
        q.append((start,-1))
        count=0
        while q and k>= 0:
            count += len(q)
            for i in range(len(q)):
                u, parent = q.popleft()
                for v in adj[u]:
                    if v!= parent:
                        q.append((v,u))
            k-=1
        return count

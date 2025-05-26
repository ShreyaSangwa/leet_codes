class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        def dfs(cur, adj, vis, longest, colors):
            if vis[cur]==1:
                return float('inf')
            if vis[cur]==0:
                vis[cur]=1
                for i in adj[cur]:
                    ret_val = dfs(i, adj, vis, longest, colors)
                    if ret_val==float('inf'):
                        return float('inf')
                    for j in range(26):
                        longest[j][cur] = max(longest[j][cur], longest[j][i])
                longest[ord(colors[cur])-ord('a')][cur]+=1
                visited[cur]=2
            return longest[ord(colors[cur])-ord('a')][cur]
        
        n = len(colors)
        adj=[[] for i in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
        longest = [[0]*n for i in range(26)]
        max_len = 0
        visited = [0]*n
        for i in range(n):
            ret_val = dfs(i, adj, visited, longest, colors)
            if ret_val == float('inf'):
                return -1
            else:
                max_len = max(max_len, ret_val)
        return max_len
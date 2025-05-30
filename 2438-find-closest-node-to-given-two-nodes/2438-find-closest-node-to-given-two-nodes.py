class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist = [[-1, -1] for _ in range(n)]
        dist[node1][0] = 0
        dist[node2][1] = 0
        
        q = deque()
        q.append((node1, 0))
        q.append((node2, 1))
        
        while q:
            curr, typ = q.popleft()
            neighbor = edges[curr]
            if neighbor != -1 and dist[neighbor][typ] == -1:
                dist[neighbor][typ] = dist[curr][typ] + 1
                q.append((neighbor, typ))
        
        meeting_point = -1
        min_distance = float('inf')
        for i in range(n):
            if dist[i][0] != -1 and dist[i][1] != -1:
                curr_distance = max(dist[i][0], dist[i][1])
                if curr_distance < min_distance:
                    min_distance = curr_distance
                    meeting_point = i
        return meeting_point
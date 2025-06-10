class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows=grid
        column=[]
        a=[]
        n=0
        while n<len(grid[0]):
            a=[]
            for i in grid:
                a.append(i[n])
            column.append(a)
            n+=1
        count=0
        for i in rows:
            for j in column:
                if i==j:
                    count+=1
        return count
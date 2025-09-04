class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            a=[]
            for j in range(9):
                if board[i][j]==".":
                    continue
                else:
                    n=int(board[i][j])
                    if n in a:
                        return False
                    else:
                        a.append(n)
        for i in range(9):
            a=[]
            for j in range(9):
                if board[j][i]==".":
                    continue
                else:
                    n=int(board[j][i])
                    if n in a:
                        return False
                    else:
                        a.append(n)
        num1=0
        num2=0
        while num1<9:
            while num2<9:
                a=[]
                for i in range(3):
                    for j in range(3):
                        if board[num2+j][num1+i]==".":
                            continue
                        else:
                            n=int(board[num2+j][num1+i])
                            if n in a:
                                return False
                            else:
                                a.append(n)
                num2+=3
            num1+=3
            num2=0
        return True
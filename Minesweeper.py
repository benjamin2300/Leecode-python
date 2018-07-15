class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        X = click[0]
        Y = click[1]
        YB = len(board[0])
        XB = len(board)
        print X, Y
        if board[X][Y] == 'M':
            board[X][Y] = 'X'
            return board
        mine = 0
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if X+i >= 0 and X+i < XB and Y+j >= 0 and Y+j < YB:
                    if board[X+i][Y+j] == 'M':
                        mine+=1
        board[X][Y] = str(mine)
        if mine != 0:
            return board
        if mine == 0:
            board[X][Y] = 'B'
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if X+i >= 0 and X+i < XB and Y+j >= 0 and Y+j < YB and board[X+i][Y+j]=='E':
                        self.updateBoard(board, [X+i, Y+j]) 
        return board
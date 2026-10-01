class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(f'Starting step 1')
        for row in board:
            if not self.check_line(row):
                return False


        print(f'Startign step 2')
        for i in range(9): # all boards have the same sized rows
            column = [x[i] for x in board]
            if not self.check_line(column):
                return False


        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                cube = []
                cube.extend(board[i][j:j+3])
                cube.extend(board[i+1][j:j+3])
                cube.extend(board[i+2][j:j+3])
                if not self.check_line(cube):
                    return False
        
        return True

    def check_line(self, row: List[str]) -> bool:
        map = {}
        for s in row:
            if s == ".":
                continue
            if s in map:
                return False
            else: 
                map[s] = True
        return True
    
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            column = []
            for j in range(len(board[0])):
                column.append(board[j][i])
            filteredrow = [x for x in board[i] if x != '.']
            filteredcolumn = [y for y in column if y != '.']
            if len(filteredrow) != len(set(filteredrow)):
                return False
            elif len(filteredcolumn) != len(set(filteredcolumn)):
                return False
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                subbox = []
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        subbox.append(board[a][b])
                filteredbox = [z for z in subbox if z != '.']
                if len(filteredbox) != len(set(filteredbox)):
                    return False
        return True
            

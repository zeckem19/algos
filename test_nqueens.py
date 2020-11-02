class QueensProblem:
    def __init__(self, numOfQueens):
        self.num_of_queens = numOfQueens
        self.chess_table = [[None for i in range(numOfQueens)] for j in range(numOfQueens)]
    def solve_queens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print('There is no solution...')
            
    def solve(self, col):
        if col == self.num_of_queens:
            return True
        for row in range(self.num_of_queens):
            if self.check_valid(row, col):
                self.chess_table[row][col] = 1
                if self.solve(col+1):
                    return True
                self.chess_table[row][col] = 0
            
        return False
    
    def check_valid(self,row,col):
        for x in range(self.num_of_queens):
            if x==col:
                continue
            if self.chess_table[row][x]:
                return False
        
        
        x,y= row,col
        while (x<self.num_of_queens-1 and x > 0) and\
                (y<self.num_of_queens-1 and y > 0):
            x+=1
            y+=1
            if self.chess_table[x][y]:
                return False
            
        x,y= row,col           
        while (x<self.num_of_queens-1 and x > 0) and\
            (y<self.num_of_queens-1 and y > 0):
            x-=1
            y-=1
            if self.chess_table[x][y]:
                return False
            
        x,y= row,col
        while (x<self.num_of_queens-1 and x > 0) and\
                (y<self.num_of_queens-1 and y > 0):
            x+=1
            y-=1
            if self.chess_table[x][y]:
                return False
            
        x,y= row,col           
        while (x<self.num_of_queens-1 and x > 0) and\
            (y<self.num_of_queens-1 and y > 0):
            x-=1
            y+=1
            if self.chess_table[x][y]:
                return False
        
        return True
    
    def print_queens(self):
        for i in range(self.num_of_queens):
            for j in range(self.num_of_queens):
                if self.chess_table[i][j] == 1:
                    print(' * ', end='')
                else:
                    print(' - ', end='')

            print('\n')


QP= QueensProblem(4)
QP.solve_queens()
import numpy as np
def mark_current_island(matrix, x, y, r, c) :
        if x<0 or x>=r or y<0 or y>=c or matrix[x][y]!='1':  #Boundary case for matrix
            return
        
        matrix[x][y] = '2';
        #Make recursive call in all 4 adjacent directions
        mark_current_island(matrix,x+1,y,r,c)  #DOWN
        mark_current_island(matrix,x,y+1,r,c)  #RIGHT
        mark_current_island(matrix,x-1,y,r,c)  #TOP
        mark_current_island(matrix,x,y-1,r,c)  #LEFT
        
def numIslands(grid):
        a=np.array(grid)
        rows, cols = a.shape
        if rows == 0:     #Empty grid boundary case
            return 0
        #Iterate for all cells of the array
        no_of_islands = 0
        for i in range(0,rows):
            for j in range(0,cols):

                if grid[i][j]=='1':
                    
                    mark_current_island(grid,i,j,rows,cols);
                    no_of_islands += 1;
                    
        return no_of_islands;

grid1 = [['O', '1', 'O'],
       ['1', '1', 'O'],
       ['1', '1', 'O'],
       ['O', 'O', '1'],
       ['O', 'O', '1'],
       ['1', '1', 'O']]

no = numIslands(grid1)  
print(no)

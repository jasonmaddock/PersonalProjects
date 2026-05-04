from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        def more_expensive(coord, cost, score, budget):
            if coord == [0, 0]:
                return score
            if coord == [2,3]:
                print()
            up_bust, left_bust = False, False
            if coord[0] != 0:
                up_score = grid[coord[0]-1][coord[1]]
                up_cost = int(up_score > 0)
                up_bust = (up_cost + cost) > budget
            if coord[1] != 0:
                left_score = grid[coord[0]][coord[1]-1]
                left_cost = int(left_score > 0)
                left_bust = (left_cost + cost) > budget

            if (up_bust and coord[1] == 0) or (coord[0] == 0 and left_bust) or (up_bust and left_bust):
                return -1
            if coord[1] == 0 or left_bust:
                return more_expensive([coord[0]-1, coord[1]], cost + up_cost, score + up_score, budget)
            if coord[0] == 0 or up_bust:
                return more_expensive([coord[0], coord[1]-1], cost + left_cost, score + left_score, budget)
            f_up_score = more_expensive([coord[0]-1, coord[1]], cost + up_cost , score + up_score, budget)
            f_left_score = more_expensive([coord[0], coord[1]-1], cost + left_cost, score + left_score, budget)
            return max(f_left_score, f_up_score)
        
        grid = self.compress(grid)
        mc = [len(grid)-1, len(grid[0])-1]
        f_tile = grid[mc[0]][mc[1]]
        cost = int(f_tile>0)
        score = f_tile
        return more_expensive(mc, cost ,score ,k)
    
    def compress(grid):
        row = 0
        zero_count = 0
        compressed_rows_grid = []
        while row != len(grid):
            try:
                sum(grid[row])
            except:
                print()
            if sum(grid[row]) == 0:
                zero_count += 1
            else:
                zero_count = 0
            if zero_count < 2:
                compressed_rows_grid.append(grid[row])
            row += 1
        
        zero_count = 0
        column = 0
        comp_grid = [[] for i in compressed_rows_grid]

        while column != len(compressed_rows_grid[0]):
            col_vals = [i[column] for i in compressed_rows_grid]
            if sum(col_vals) == 0:
                zero_count +=1
            else:
                zero_count = 0
            if zero_count < 2:
                for r, val in zip(comp_grid, col_vals):
                    r.append(val)
                    
            column += 1
        return comp_grid
        

    


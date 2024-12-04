from enum import Enum
import numpy as np

def read_input(file_path: str) -> list:
    letters_to_int = { 'X': 0, 'M': 1, 'A': 2, 'S': 3 }

    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            row = np.zeros(len(line.strip('\n')), dtype=int)
            for r in range(0, len(row)):
                row[r] = letters_to_int[line[r]]
            lines.append(row)

    return np.vstack(lines)

class Searches(Enum):
    UP = [[0,0], [-1,0], [-2,0], [-3,0]]
    RIGHT_UP = [[0,0], [-1,1], [-2,2], [-3,3]]
    RIGHT = [[0,0], [0,1], [0,2], [0,3]]
    RIGHT_DOWN = [[0,0], [1,1], [2,2], [3,3]]
    DOWN = [[0,0], [1,0], [2,0], [3,0]]
    LEFT_DOWN = [[0,0], [1,-1], [2,-2], [3,-3]]
    LEFT = [[0,0], [0,-1], [0,-2], [0,-3]]
    LEFT_UP = [[0,0], [-1,-1], [-2,-2], [-3,-3]]

def apply_search(puzzle: np.array, search: Searches, i: int, j: int) -> int:
    if (i + search.value[3][0] < 0) or (i + search.value[3][0] >= len(puzzle)):
        return 0
    
    if (j + search.value[3][1] < 0) or (j + search.value[3][1] >= len(puzzle[i])):
        return 0
    
    for k in range(1, len(search.value)):
        if puzzle[i + search.value[k][0]][j + search.value[k][1]] != k:
            return 0
        
    return 1

def find_xmas(puzzle: np.array) -> int:
    found = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                for search in Searches:
                    found += apply_search(puzzle, search, i, j)
    
    return found

class CrossSearches(Enum):
    MAS_SAM = [[1, 0, 3], # M . S
               [0, 2, 0], # . A . 
               [1, 0, 3]] # M . S
    MAS_MAS = [[1, 0, 1], # M . M
               [0, 2, 0], # . A .
               [3, 0, 3]] # S . S
    SAM_SAM = [[3, 0, 3], # S . S
               [0, 2, 0], # . A .
               [1, 0, 1]] # M . M
    SAM_MAS = [[3, 0, 1], # S . M
               [0, 2, 0], # . A .
               [3, 0, 1]] # S . M

def apply_cross_search(puzzle: np.array, search: CrossSearches, i: int, j: int) -> int:
    def check_diagonals_zero(array: np.array) -> bool:
        main_diagonal = np.diagonal(array)
        anti_diagonal = np.diagonal(np.fliplr(array))
        
        return np.all(main_diagonal == 0) and np.all(anti_diagonal == 0)
    
    current = np.array([[puzzle[i-1][j-1], puzzle[i-1][j], puzzle[i-1][j+1]],
                        [puzzle[i][j-1], puzzle[i][j], puzzle[i][j+1]],
                        [puzzle[i+1][j-1], puzzle[i+1][j], puzzle[i+1][j+1]]])
    return 1 if check_diagonals_zero(current - search.value) else 0

def find_crossmas(puzzle: np.array):
    found = 0
    for i in range(1, puzzle.shape[0] - 1):
        for j in range(1, puzzle.shape[1] - 1):
            if puzzle[i][j] == 2:
                for search in CrossSearches:
                    found += apply_cross_search(puzzle, search, i, j)
                
    return found

if __name__ == '__main__':
    puzzle = read_input('inputs/day_four.txt')
        
    print(f'Part 1: {find_xmas(puzzle)}')
    print(f'Part 2: {find_crossmas(puzzle)}')
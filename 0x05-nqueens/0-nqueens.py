#!/usr/bin/python3
import sys


def solve_nqueens(n):
    def could_place(row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    
    def place_queen(row, n):
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if could_place(row, col):
                board[row] = col
                place_queen(row + 1, n)
    
    solutions = []
    board = [-1] * n
    place_queen(0, n)
    return solutions

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
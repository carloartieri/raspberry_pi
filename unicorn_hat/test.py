import curses
from sys import exit
from time import sleep


cell = [None,0,0,0] 
temp_mat = []
matrix = []
for y in range(0,8):
        temp_mat.append(cell)
for x in range(0,8):
        matrix.append(list(temp_mat))

ship = ['s',255,0,0]
ship_pos = [3,7]
matrix[3][7] = ship

print matrix[3]
#for y in range(0,8):
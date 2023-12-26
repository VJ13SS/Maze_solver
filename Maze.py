"""
Maze Solver with Curses Visualization

This script demonstrates a maze-solving algorithm using the curses library for visualization.
It defines functions to find a path from the starting point 'O' to the endpoint 'X' in a maze.

Usage:
- Run the script to visualize the maze-solving process in the terminal.

Requirements:
- Python
- curses library

Maze Legend:
- 'O': Starting point
- 'X': Endpoint
- '#': Wall
- ' ': Open path

Functions:
- print_maze(stdscr, maze, path=[], message=""): Display the maze with an optional path and message.
- find_start_pos(maze, start): Find the starting position in the maze.
- find_neighbours(maze, row, col): Find neighboring positions in the maze.
- find_path(maze, stdscr): Find a path from start to end and visualize it using curses.


Author....VJ 13 SS
Last mofified....26 Dec 2023 6:22pm
"""
import curses
from curses import wrapper
import queue
import time

maze = [
    ["O", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", "#", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#", "#", " ", "#", "#"],
    ["#", " ", "#", " ", "#", " ", " ", " ", "#", "#", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#", "#", "#", " ", "#"]
]

def print_maze(stdscr,maze,path=[]):
	
	red=curses.color_pair(1)
	for i,row in enumerate(maze):
		for j,value in enumerate(row):
			if(i,j) in path:
				stdscr.addstr(i,j*2,'*',red)
			else:
				stdscr.addstr(i,j*2,value)
def find_start_pos(maze,start):
	for i,row in enumerate(maze):
		for j,value in enumerate(row):
			if(value==start):
				return i,j
	return None
def find_neighbours(maze,row,col):
	neighbours=[]
	if(row>0):
		neighbours.append((row-1,col))
	if(row +1<len(maze)):
		neighbours.append((row+1,col))
	if(col>0):
		neighbours.append((row,col-1))
	if(col+1<len(maze)):
		neighbours.append((row,col+1))
	return neighbours

def find_path(maze,stdscr):
	start='O'
	end='X'
	start_pos=find_start_pos(maze,start)
	q=queue.Queue()
	q.put((start_pos,[start_pos]))
	visited=set()
	while not q.empty():
		current_pos,path=q.get()
		row,col=current_pos
		stdscr.clear()
		print_maze(stdscr,maze,path)
		time.sleep(0.5)
		stdscr.refresh()
		if(maze[row][col]==end):
			return path
		neighbours=find_neighbours(maze,row,col)
		for neighbour in neighbours:
			if(neighbour in visited):
				continue
			r,c=neighbour
			if maze[r][c]=='#':
				continue
			newpath=path+[neighbour]
			q.put((neighbour,newpath))
			visited.add(neighbour)
	
def main(stdscr):
	curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
	find_path(maze,stdscr)
	#curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	time.sleep(2)
	stdscr.getch()
wrapper(main)
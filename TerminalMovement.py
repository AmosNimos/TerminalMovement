import numpy as np
import random as rn
from termcolor import colored
import os
from curtsies import Input

grid = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

Columns = []
Rows = []
xx=0
yy=0

def display():
	linetxt=""
	for y in range(9):
		print(linetxt)
		linetxt=""
		for x in range(9):
			if(x==xx and y ==yy):
				linetxt+=colored(str(grid[x][y]),'red')
			else:
				linetxt+=colored(".",'white')

def main():
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			return e

while True:
	keypress = main()
	debug=""
	if keypress == 'd':
		xx+=1;
		debug = "Move Right"
	if keypress == 'a':
		xx-=1;
		debug = "Move Left"
	if keypress == 'w':
		yy-=1;
		debug = "Move Up"
	if keypress == 's':
		yy+=1;
		debug = "Move Down"
	os.system('clear')
	display()
	print(keypress)
	print(debug)


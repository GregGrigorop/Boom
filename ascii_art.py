from pyfiglet import figlet_format
import sys
from colorama import init,Back,Fore,Style
from termcolor import colored,cprint
init()

def ascii_art(msg,color,bg_color):
	valid_colors = ('red','blue','white','yellow','green','magenta','cyan')
	while True:
		if color.lower() not in valid_colors:
			print("The possible choices are: white,yellow,blue,cyan,magenta,red, green")
			color = input("What is the color you want to be used?\n")
		else:
			break
	while True:
		if bg_color.lower() not in valid_colors:
			print("The possible choices are: white,yellow,blue,cyan,magenta,red, green")
			bg_color = input("What about the background color?\n")
		else:
			break
	cprint(figlet_format(msg),color=color.lower(),on_color='on_'+bg_color.lower(),attrs=['bold'])

msg = input("What is the text you want colored?\n")
color = input("What is the color you want to be used?\n")
bg_color = input("What about the background color?\n")

ascii_art(msg,color,bg_color)
#!/usr/bin/env python3

import argparse as ap
import os
from colored import fg, bg, attr
import datetime, time
import re

def slideFrame(slide, title, slideNum, lenslides):
	global frameColor, reset
	currtime = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
	footnote = 'Slide Number: ' + str(slideNum) + '/' + str(lenslides) + ' '*(116-4-4-len(str(slideNum))-len(currtime)-len(str(lenslides))) + currtime
	print(frameColor + '#'*130 + '\n##'+' '*126+'##\n##  ' + reset + title + frameColor + ' ##\n##'+' '*126+'##\n' + '#'*130 + '\n##' + reset + ' '*126 + frameColor + '##' + reset)
	lines = slide.split('\n')
	for line in range(len(lines)):
		print(frameColor + '##' + reset + '   ' +  lines[line] + ' '*(123-len(lines[line])) + frameColor + '##' + reset)
	for _ in range(30-len(lines)):
		print(frameColor + '##' + reset + ' '*126 + frameColor + '##' + reset)
	print(frameColor + '#'*130 + '\n##'+' '*126+'##\n##  ' + reset + footnote + frameColor + ' ##\n##'+' '*126+'##\n' + '#'*130 + reset)

def slide(slideFile, folder):
	with open(folder+'/'+slideFile+'.txt', 'r') as file:
		return file.read()

def controls(currentslide, lenslides):
	print('\n[F]irst          [P]revious          [N]ext          [L]ast          SlideNum          [E]xit')
	while True:
		choice = input('>> ')
		if choice.lower() == 'f' or choice.lower() == 'first':
			return 1
		elif choice.lower() == 'p' or choice.lower() == 'previous':
			if currentslide <= 1:
				return currentslide
			return currentslide-1
		elif choice.lower() == 'n' or choice.lower() == 'next':
			if currentslide >= lenslides:
				return currentslide
			return currentslide+1
		elif choice.lower() == 'l' or choice.lower() == 'last':
			if currentslide >= lenslides:
				return currentslide
			return lenslides
		elif re.search('^\d+$',choice):
			if (int(choice) > (lenslides)) or (int(choice) == 0):
				print('No such slide number!')
				continue
			return int(choice)
		elif choice.lower() == 'e' or choice.lower() == 'exit':
			if input('Are you sure you want do exit the presentation? If so, type yes: ').lower() == 'yes':
				os.system('clear')
				exit(0)
		else:
			print('Option not recognized. Try again!')

def loadPresentation(folder):
	print('Checking all the necessary files...')
	time.sleep(2)
	if os.path.isdir(folder):
		if not os.path.exists(folder+'/header.txt'):
			print('Make sure you have one header.txt and that your slide files ar named using numbers, eg. 0.txt, 1.txt etc.')
			exit(1)
		else:
			print('Header found. Loading presentation...')
			time.sleep(2)
		with open(folder+'/header.txt', 'r') as header:
			subject = header.readline().rstrip('\n')
			place = header.readline().rstrip('\n')
			title = subject + ' '*(129-3-3-len(subject)-len(place)) + place
		slides = []
		for file in os.listdir(folder):
			if re.search('\d+\.txt',file):
				slides.append(file[:-4])
		if slides == []:
			print('No slides found!! Exiting...')
			exit(1)
	else:
		print('The folder you specified was not found.')
		exit(1)

	return title, sorted(slides, key=lambda x: float(x)), len(slides)

def main():
	global frameColor, reset
	parser = ap.ArgumentParser()
	parser.add_argument('folder', help='The folder in which the presentation is.')
	parser.add_argument('-b', '--bg', default='dark_green', help='Background color of the presentation frame.')
	parser.add_argument('-f', '--fg', default='white', help='Foreground color of the presentation frame.')
	args = parser.parse_args()
	
	title, slides, lenslides = loadPresentation(args.folder)
	currentslide = 1

	frameColor = bg(args.bg) + fg(args.fg)
	reset = attr('reset')

	while True:
		os.system('clear')
		slideFrame(slide(slides[currentslide-1], args.folder), title, currentslide, lenslides)
		currentslide = controls(currentslide, lenslides)


if __name__ == '__main__':
	main()

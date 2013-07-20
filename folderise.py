#!/usr/bin/env python

#
# A simple script for moving files in a directory into their own
# individual directories
#

import sys
import shutil

from os import listdir, mkdir
from os.path import isfile, join

# Ensure compatible keyboard input from both versions of Python
if sys.version_info.major < 3: input = raw_input

PATH = "D:/Test/"

def main():
	files = [ join(PATH, f) for f in listdir(PATH) if isfile(join(PATH, f)) ]
	folders = [ f.split('.')[0] + '/' for f in files ]
	
	if files:
		print("The following folders will be created (%s):" % PATH)

		for i, f in enumerate(folders):
			print("\t%d. %s" % (i + 1, f))

		if input("Continue with procedure (y/n)? ").lower() == 'y':
			# Continue with procedure
			print

			for f, folder in zip(files, folders):
				src, dst = (f, folder)
				print("%s -> %s" % (src, dst))
				
				try:
					mkdir(dst)
					shutil.move(src, dst)
				except OSError as e:
					# mkdir() throws OSError
					print("Error creating directory '%s': %s" % (dst, e.strerror))
					continue
				except shutil.Error as e:
					# shutil.move() throws shutil.Error
					print("Error moving %s: %s" % (src, e.strerror))
					continue
		else:
			exit()

if __name__ == '__main__':
	main()

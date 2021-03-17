import sys
import os
import re
from PIL import Image

platform_used = sys.platform
windows_match = re.search('^win[3,6][2,4]$', platform_used)
if windows_match:
	slash = '\\'
else:
	slash = '/'

def syntax():
	print(f' syntax: py {os.path.basename(__file__)} existing_jpg_folder{slash} png_folder{slash}')

def quit_program():
	print('program quit')
	quit()

# grab first and second argumets
try:
	jpg_path = sys.argv[1]
	if not(jpg_path.endswith(slash)):
		jpg_path = jpg_path + slash
	png_path = sys.argv[2]
	if not(png_path.endswith(slash)):
		png_path = png_path + slash
	arg_len = len(sys.argv) - 1
	if arg_len > 2:
		print(f'2 arguments are needed but {arg_len} are given.')
		syntax()
		quit_program()
except IndexError:
	print('No or less argument (2 arguments needed)')
	syntax()
	quit_program()

if __name__ == '__main__':

	# check if new/ exist, if not create it

	try:
		file_list = os.listdir(jpg_path)
		jpg_list = []
		for file in file_list:
			if file.endswith('.jpg'):
				jpg_list.append(file)
		print(f'{len(jpg_list)} jpg files found')
		if len(jpg_list) == 0:
			quit_program()
	except FileNotFoundError:
		print(f'{jpg_path} folder not exist')
		quit_program()

	if not(os.path.isdir(png_path)):
		print(f'{png_path} folder not exist, create the folder')
		os.mkdir(png_path)
		print(f'....{png_path} folder created')



	# loop through Pokedex

	for jpg in jpg_list:
		# convert images to png
		# save them to the new folder
		try:
			img = Image.open(f'.{slash}{jpg_path}{jpg}')
		except:
			print(f'.{slash}{jpg_path}{jpg} is not a jpg image file.')
			print('....skipped')
			continue
		png_file = jpg.replace('.jpg', '.png')
		print(f'converting {jpg_path}{jpg} to {png_path}{png_file}')
		img.save(f'.{slash}{png_path}{png_file}', 'png')
		print('....done!')

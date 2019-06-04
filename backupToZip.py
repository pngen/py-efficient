#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
	# Backup entire contents of "folder" into a ZIP file.

	folder = os.path.abspath(folder)	# make sure folder is absolute

	# Figure out the filename this code should use based on
	# what files already exist.
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number += 1

	print('Creating %s...' % (zipFilename))
	backupZip = zipfile.ZipFile(zipFilename, 'w')

	for foldername, subfolders, filenames in os.walk(folder):
		print('Adding files in %s...' % (foldername))
		# Add current folder to ZIP file.
		backupZip.write(foldername)
		# Add all files in this folder to ZIP file.
		for filename in filenames:
			newBase = str(os.path.basename(folder) + '_')
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue # don't backup the backup ZIP files
			backupZip.write(os.path.join(foldername, filename))
	backupZip.close()
	print('Done.')


backupToZip(os.path.curdir)
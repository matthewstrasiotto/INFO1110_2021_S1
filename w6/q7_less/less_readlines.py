import sys

path = sys.argv[1]

try:
	f = open(path)
except FileNotFoundError:
	print('File could not be found :(')
	sys.exit()

# reads the whole thing, and returns it as a list of each line
lines = f.readlines()

for line in lines:
        # get the next line as a string

	# Stop if we have reached the end of the file
	if line == '':
		break
	
	print(line.strip())

	# Stop if the user hits `q`
	cmd = input()
	if cmd == 'q':
		break

# Don't forget to close the file!
f.close()

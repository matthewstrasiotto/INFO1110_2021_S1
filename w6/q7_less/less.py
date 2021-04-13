import sys

path = sys.argv[1]

try:
	f = open(path)
except FileNotFoundError:
	print('File could not be found :(')
	sys.exit()

# because we're reading them one at a time
while True:
        # get the next line as a string
	line = f.readline()

	# Stop if we have reached the end of the file
	if line == '':
		break
	
	print(line.strip())

	# Stop if the user hits `q`
	cmd = input()
        print(f"you entered: {cmd}")
	if cmd == 'q':
		break

# Don't forget to close the file!
f.close()

import sys

try:
    path = sys.argv[1]

    f = open(path)
except FileNotFoundError:
    print('File could not be found :(')
    sys.exit()
except IndexError:
    print("requires the path")
    sys.exit()
    # what kind of exception to check theyve given enough args?

# reads the whole thing, and returns it as a list of each line
lines_original = f.readlines()

print("THIS IS IOBase.readlines():")
print(lines_original)


# Don't forget to close the file!
f.close()


# now DIY:
lines_v2 = []

try:
    f = open(path)
except FileNotFoundError:
    print('File could not be found :(')
    sys.exit()

while True:
    # get the next line as a string
    line = f.readline()

    # Stop if we have reached the end of the file
    if line == '':
            break

    lines_v2.append(line)

print(lines_v2)

# Don't forget to close the file!
f.close()

import sys

try:
    path_stem = sys.argv[1]
    path = f"{path_stem}.txt"

    f = open(path)
except FileNotFoundError:
    print('File could not be found :(')
    sys.exit()
except IndexError:
    print("requires the path")
    sys.exit()


lines_unsorted = f.readlines()

f.close()

print(lines_unsorted)

# sorted just sorts the input & returns it :)
lines_sorted = sorted(lines_unsorted)

print(lines_sorted)

# "with" is just a
with open(f"{path_stem}-sorted.txt", "w") as f:
    f.writelines(lines_sorted)

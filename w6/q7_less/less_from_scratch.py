
#>  A file path will be given as a command line argument.

# command line argument:
# this means I need to read sys.arg 
import sys

file_path = sys.argv[1]


try:
    f = open(file_path)

    # file path:
    # This means i need to do f = open()

    # this is the more complicated stuff
    """
    When launched, your program will print the first line of the file and wait for user input.

    If the user hits Enter, print the next line and wait for further input.

    If the user types q and then Enter, exit the program.
    """
    # because we're going to exit when they type q, lets do a while loop & break only on 'q'

    while True:
        #> When launched, your program will print the first line of the file 
        current_line = f.readline()
        current_line = current_line.strip()
        print(current_line)

        #> and wait for user input.
        user_input = input()

        #> If the user hits Enter, print the next line and wait for further input.
        
        user_input_trimmed = user_input.strip()

        #> If the user types q and then Enter, exit the program.
        if user_input_trimmed == 'q':
            break


#> Make sure you handle the case where the file cannot be found! 
except FileNotFoundError:
    print(" Make sure you handle the case where the file cannot be found!")
finally:
    #> Also don't forget to close the file after you are done with it.
    f.close()

import sys
import math

def quadratic(a, b, c):
    # Raise ValueError if a equals zero
    if a == 0:
        raise ValueError("Not a valid quadratic: the leading coefficient cannot be zero.")
    disc = b**2 - 4*a*c
    # Raise ValueError if discriminant is negative
    if disc < 0:
        raise ValueError("There are no real solutions.")
    # Otherwise just return the two roots (even if double roots)
    return (-b + math.sqrt(disc)) / (2*a), \
           (-b - math.sqrt(disc)) / (2*a)


try:
    # Take integer input from user
    # If IndexError, execution jumps to line 34. If ValueError, jumps to line 38.
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    
    try:
        # If user inputs are good, then try and call quadratic() function
        # If ValueError, execution jumps to line 36
        x_1, x_2 = quadratic(a, b, c)
        
        # One/two solution cases should not be dealt with by exception handling!
        if x_1 == x_2:
            print('The equation {}x^2 + {}x + {} = 0 has one solution:'.format(a, b, c))
            print('x = {:.2f}'.format(x_1))
        else:
            print('The equation {}x^2 + {}x + {} = 0 has two solutions:'.format(a, b, c))
            print('x = {:.2f} and x = {:.2f}'.format(x_1, x_2))
    
    except ValueError as e:
        print(e)    # Prints message from the exception raised

except IndexError:
    print("A quadratic needs three coefficients")

except ValueError:
    print("The coefficients must be integers.")

import sys
import math

def quadratic(a, b, c):
    disc = b**2 - 4*a*c      # the discriminant
    if disc == 0:
        return -b / (2*a)    # what's the type here?
    else:
        return (-b + math.sqrt(disc)) / (2*a), \
               (-b - math.sqrt(disc)) / (2*a)         # type?
        
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
x_1, x_2 = quadratic(a, b, c)    # unpack returned tuple

print('The equation {}x^2 + {}x + {} = 0 has these solutions:'.format(a, b, c))
print('x = {:.2f} and x = {:.2f}'.format(x_1, x_2))

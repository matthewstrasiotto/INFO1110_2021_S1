
# WHAT WILL THIS PRINT

try:
    #  raise IndexError("out of bounds")
    raise KeyError("no keu")

except NameError:
    print("NameError")
#  except IndexError:
    #  print('IndexError')
#  except LookupError:
    #  print("LookupError")

except Exception: # this will catch everything
    # always put it at the end IF you do catch it
    # but also, not catching Exception is probably better often
    print("general exception")

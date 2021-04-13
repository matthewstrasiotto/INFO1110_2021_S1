def set_meeting(time):
    if type(time) != int:
        # What is the next word to type?
        raise TypeError("Error: time must be an integer")

    # what to write?
    if time < 0 or time > 2359:
        raise ValueError("Error: time must be between 0000 hrs and 2359 hrs.")
    
    # 
    if time < 800 or time > 2200:
        raise ValueError("No...I'm sleeping...")

    return "You have a meeting at {:04d} hrs Don't forget!".format(time)
# Should print: You have a meeting at 0900 hrs Don't forget!

try:
    print(set_meeting(900))
    print(set_meeting(2200))
    print(set_meeting("900"))
    print(set_meeting(2300))
except ValueError:
    print("some kind of value error?")
except TypeError:
    print("some kind of type error")


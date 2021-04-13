cm_to_inches = 0.393791
inches_to_feet = 12

invalid_input = True

while True:
    try:
        height_cm = float(input('Enter your height in cm: '))
        
        if (height_cm <= 0):
            # How to report something is wrong?
            raise ValueError("Negative height????")

        feet = height_cm * cm_to_inches // inches_to_feet
        inch = height_cm * cm_to_inches % inches_to_feet
        print("You are {:.0f} feet {:.0f} inches tall!".format(feet, inch))
        #  invalid_input = False
        break
    # Imagine we want to tell people something is wrong, but be specific if its a 
    # ValueError
    # what will python print if we type in "a string"
    except ValueError:
        print("Only positive numeric inputs are accepted. Please try again.")
        print()
    except Exception:
        print("something went wrong!")
    

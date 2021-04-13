cm_to_inches = 0.393791
inches_to_feet = 12

try:
    height_cm = float(input('Enter your height in cm: '))
    feet = height_cm * cm_to_inches // inches_to_feet
    inch = height_cm * cm_to_inches % inches_to_feet
    print("You are {:.0f} feet {:.0f} inches tall!".format(feet, inch))
except:
    ValueError:
        print("Only positive numeric inputs are accepted, please try again")



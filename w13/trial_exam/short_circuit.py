
def condition(true_or_false : bool, message : str):
    print(message)
    return true_or_false


if condition(True, "1") or condition(True, "2"):
    print("okay")

if condition(False, "3") or condition(False, "4"):
    print("okay2")

if condition(False, "5") and condition(True, "6"):
    print("okay3")

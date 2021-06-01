def find_evens(start, end):
    out = ""
    for i in range(start, end + 1):
        if i % 2 == 0: out += f"{i} "

    out = out.rstrip()

    return out
    
print(find_evens(2, 10))

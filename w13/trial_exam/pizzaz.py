def order(   ):

    n_tix = input("Enter the number of tickets you're purchasing :")
    n_tix = int(n_tix)

    n_popcorn = 0
    for i in range(n_tix):
        want_popcorn = input(f"For person {i+1}, would you like to purchase popcorn? ")
        want_popcorn = want_popcorn.tolower()

        if want_popcorn == "y": n_popcorn += 1
        #if want_popcorn == "n": pass

    return (n_tix, n_popcorn)

def calculate_total(n_tix, n_popcorn):
    price_per_ticket = 10.0
    price_per_popcorn = 8.0

    out = n_tix*price_per_ticket + n_popcorn*price_per_popcorn
    return out

def transaction(total_price, user_paid):
    denoms = {
        100*100: "$100",
        100*50: "$50",
        100*20: "$20",
        100*10: "$10",
        100*5: "$5",
        100*2: "$2",
        100*1: "$1",
        50: "50 cents",
        20: "20 cents",
        10: "10 cents",
        5: "5 cents"
    }
    out = {}
    # could do some checks about if this is negative, or if equal
    curr_remaining =  user_paid - total_price
    curr_remaining = int(curr_remaining * 100)

    for denom in denoms:
        denom_string = denoms[denom]
        n_divisions = curr_remaining // denom
        curr_remaining -= n_divisions * denom

        if denom_string not in out:
            out[denom_string] = 0

        out[denom_string] += n_divisions
    return out

out = transaction(36, 200.5)
print(out)
for denom in out:
    if out[denom]: print(f"{denom}: {out[denom]}")

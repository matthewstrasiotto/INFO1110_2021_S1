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
       "$100"    : 100*100,
       "$50"     : 100*50,
       "$20"     : 100*20, 
       "$10"     : 100*10,
       "$5"      : 100*5, 
       "$2"      : 100*2,  
       "$1"      : 100*1,  
       "50 cents": 50,  
       "20 cents": 20,     
       "10 cents": 10,     
       "5 cents" : 5     
    }
    out = {}
    # could do some checks about if this is negative, or if equal
    change_remaining =  user_paid - total_price
    change_remaining = int(change_remaining * 100)
    
    # iterate over each of the keys
    for denom_string in denoms.keys():
        denom_cents = denoms[denom_string]

        n_divisions = change_remaining // denom_cents
        change_remaining -= n_divisions * denom_cents

        out[denom_string] = n_divisions
    return out

out = transaction(36, 200.5)
print(out)
for denom in out:
    if out[denom]: print(f"{denom}: {out[denom]}")

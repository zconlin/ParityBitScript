######################################################################
# A script that generates random data and adds a parity bit. This    #
# was written as a visual demonstration of how parity bits function  #
# and to see the success/failure conditions of this type of parity.  #
######################################################################

import random

def parity_decider(data):
    j = sum(data)
    parity_bit = j % 2
    return parity_bit

def generate_random(data):
    for i in range(8):
        random_bit = random.randint(0, 1)
        data.append(random_bit)

def main():
    data = []
    generate_random(data)
    
    print("This is our correct data with parity bit:", data, parity_decider(data))
    
    # 1 Error
    data[3] = 1 - data[3]
    print("1 error - Flipped bit 4")
    print("This is our incorrect data with parity bit:", data, parity_decider(data))

    parity_bit_old = parity_decider(data)
    
    if parity_bit_old == parity_decider(data):
        print("Data is correct.\n")
    else:
        print("Data is incorrect.\n")
    
    # 2 Errors
    data[4] = 1 - data[4]
    print("2 errors - Flipped bit 5")
    print("This is our incorrect data with parity bit:", data, parity_decider(data))

    if parity_bit_old == parity_decider(data):
        print("Data is correct.\n")
    else:
        print("Data is incorrect.\n")

    # 3 Errors
    data[5] = 1 - data[5]
    print("3 errors - Flipped bit 6")
    print("This is our incorrect data with parity bit:", data, parity_decider(data))

    if parity_bit_old == parity_decider(data):
        print("Data is correct.")
    else:
        print("Data is incorrect.")

if __name__ == "__main__":
    main()

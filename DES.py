"""
Program to implement the DES algorithm. Uses 3 default source files "inputDES.txt", "keyDES.txt", and "outputDES.txt".
"inputDES.txt" requires a "d" or an "e" on the first line do determine encryption or decryption.
@authors Kevin Hoopes, Jeremy Schmich, Dustin Roan, Adam Callanan, Sage Elfanbaun
@version 9/29/2017
"""

ip_table = [58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9,  1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7]

inverse_ip = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]

e_table = [32, 1, 2, 3, 4, 5,
           4, 5, 6, 7, 8, 9,
           8, 9, 10, 11, 12, 13,
           12, 13, 14, 15, 16, 17,
           16, 17, 18, 19, 20, 21,
           20, 21, 22, 23, 24, 25,
           24, 25, 26, 27, 28, 29,
           28, 29, 30, 31, 32, 1]

s1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

s2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

s3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

s4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

s5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

s6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 7, 13]]

s7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

s8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

p_box = [16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25]

# Added the locations of the parity bits for cleaner code - they're removed later anyway
permuted_choice1 = [57, 49, 41, 33, 25, 17, 9, 8,
                    1, 58, 50, 42, 34, 26, 18, 16,
                    10, 2, 59, 51, 43, 35, 27, 24,
                    19, 11, 3, 60, 52, 44, 36, 32,
                    63, 55, 47, 39, 31, 23, 15, 40,
                    7, 62, 54, 46, 38, 30, 22, 48,
                    14, 6, 61, 53, 45, 37, 29, 56,
                    21, 13, 5, 28, 20, 12, 4, 64]

permuted_choice2 = [14, 17, 11, 24, 1, 5, 3, 28,
                    15, 6, 21, 10, 23, 19, 12, 4,
                    26, 8, 16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55, 30, 40,
                    51, 45, 33, 48, 44, 49, 39, 56,
                    34, 53, 46, 42, 50, 36, 29, 32]

left_shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

parity_bits = ''


# Function to generate all of the keys for specified number of rounds
def generate_keys(rounds, key_file):
    global parity_bits
    keys = []
    file = open(key_file, 'r')
    original = file.read()
    file.close()

    # Put key through permuted choice 1 table
    permuted_key = ''
    for i in permuted_choice1:
        permuted_key += original[i-1]

    # Pull out the parity bits to reduce to 56 bits
    reduced_key = ''
    for i in range(7, 64, 8):
        parity_bits += permuted_key[i]
        reduced_key += permuted_key[i-7:i]

    # Split key
    left_bits = reduced_key[:28]
    right_bits = reduced_key[28:]

    # Generate keys for every round
    for r in range(rounds):

        # Shift the halves according to the shift schedule
        left_bits = circular_shift(left_bits, left_shift_schedule[r])
        right_bits = circular_shift(right_bits, left_shift_schedule[r])
        pre_key = left_bits + right_bits

        # Reduce to 48 bits through permuted choice 2 table
        key = ''
        for j in permuted_choice2:
            key += pre_key[j - 1]

        keys.append(key)

    return keys


# Helper function to shift the keys according to schedule
def circular_shift(key, n_shifts):
    return key[n_shifts:] + key[0: n_shifts]


"""
Methods for converting characters to binary and back, 
if necessary in the future
"""
# def to_binary(line):
#     # pad each seven bit input with 1 to make it 8 bits
#     padded = '0'.join(format(ord(x), 'b') for x in line)
#     padded = '0' + padded
#     return padded


# def from_binary(chunk):
#     decimal = int(chunk, 2)
#     asciichar = chr(decimal)
#     return asciichar


# Function to xor 2 chunks of binary
def xor(bits1, bits2):
    output = ''

    for i in range(len(bits1)):
        if bits1[i] == bits2[i]:
            output += '0'
        else:
            output += '1'

    return output


# Function to expand the right half from 32 bits to 48 bits
def expand(bits):
    expanded = ''

    for i in range(0, 48):
        expanded += bits[e_table[i] - 1]

    return expanded


# Function to shrink the xor of the key and expanded right half
# from 48 bits to 32 bits using S-Boxes
def substitution(bits):
    s_boxes = [s1, s2, s3, s4, s5, s6, s7, s8]
    subbed_bits = ''

    for i in range(0, 8):
        temp_bits = bits[:6]
        bits = bits[6:]

        row = int(temp_bits[0] + temp_bits[-1], 2)
        col = int(temp_bits[1:5], 2)
        short_bits = bin(s_boxes[i][row][col])[2:]

        while len(short_bits) != 4:
            short_bits = '0' + short_bits

        subbed_bits += short_bits

    return subbed_bits


# Generalized permute function
# Works with IP table, Inverse IP table, and P-Box
def permute(bits, table):
    permuted = ''

    for i in range(len(bits)):
        permuted += bits[table[i] - 1]

    return permuted


# Performs the f-box of a round on the right half
def do_round(half, key):
    expanded = expand(half)
    key_and_val = xor(expanded, key)
    reduced = substitution(key_and_val)
    output = permute(reduced, p_box)
    return output


# Run the DES
def main(n_rounds=16, input_file='inputDES.txt', output_file='outputDES.txt', key_file='keyDES.txt'):
    keys = generate_keys(n_rounds, key_file)
    fi = open(input_file, 'r')
    fo = open(output_file, 'w')
    total_input = ""

    # Read file
    mode = fi.readline()

    # Turn input file to bits
    with fi as openfileobject:
        for line in openfileobject:
            total_input += line
    fi.close()

    # Pad if number of characters is not divisible of 8
    if len(total_input) % 64 != 0:
        total_input += (64 - (len(total_input) % 64)) * '0'
    print("Input size = " + str(len(total_input)))

    # Put each 64 bit chunk through DES
    while total_input != "":
        binary_value = total_input[:64]
        total_input = total_input[64:]

        # Initial permutation (w/ ip_table)
        binary_value = permute(binary_value, ip_table)

        # Determine if encrypt or decrypt
        if mode[0] == 'd':
            keys.reverse()
        elif mode[0] != 'e':
            print("mode not set")

        # Go through the rounds
        for i in range(0, n_rounds):
            # Split input
            left_half = binary_value[0:32]
            right_half = binary_value[32:64]

            # Get proper key for round
            key = keys[i]

            # Put the right half through calculations
            round_output = do_round(right_half, key)

            # New right and left for next round
            new_right = xor(left_half, round_output)
            left_half = right_half
            binary_value = left_half + new_right

        # Final 32 bit swap
        binary_value = binary_value[32:64] + binary_value[0:32]

        # Final permutation (w/ inverse_ip)
        binary_value = permute(binary_value, inverse_ip)

        fo.write(binary_value)

    fo.close()


main()

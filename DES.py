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

e_table = [[32, 1, 2, 3, 4, 5],
           [4, 5, 6, 7, 8, 9],
           [8, 9, 10, 11, 12, 13],
           [12, 13, 14, 15, 16, 17],
           [16, 17, 18, 19, 20, 21],
           [20, 21, 22, 23, 24, 25],
           [24, 25, 26, 27, 28, 29],
           [28, 29, 30, 31, 32, 1]]

p_table = [[16, 7, 20, 21, 29, 12, 28, 17],
           [1, 15, 23, 26, 5, 18, 31, 10],
           [2, 8, 24, 14, 32, 27, 3, 9],
           [19, 13, 30, 6, 22, 11, 4, 25]]

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

p_box = [[16, 7, 20, 21, 29, 12, 28, 17],
         [1, 15, 23, 26, 5, 18, 31, 10],
         [2, 8, 24, 14, 32, 27, 3, 9],
         [19, 13, 30, 6, 22, 11, 4, 25]]

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
keys = []


def generate_keys(rounds):
    global parity_bits, keys

    file = open('keyDES.txt', 'r')
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


# Helper function to shift the keys according to schedule
def circular_shift(key, n_shifts):
    return key[n_shifts:] + key[0: n_shifts]


def to_binary(line):
    # pad each seven bit input with 1 to make it 8 bits
    padded = '0'.join(format(ord(x), 'b') for x in line)
    padded = '0' + padded
    return padded


def from_binary(chunk):
    decimal = int(chunk, 2)
    asciichar = chr(decimal)
    return asciichar


def initial_permutation(binary_value):
    permutated_binary_value = ''
    while len(binary_value) !=0:
        temp_binary_value =  binary_value[:64]
        binary_value = binary_value[64:]
        changed_value = ''
        
        for i in range(0,64):
            j = ip_table[i] - 1
            changed_value = changed_value + temp_binary_value[j]

        permutated_binary_value = permutated_binary_value + changed_value
    return permutated_binary_value


def final_permutation(binary_value):
    permutated_binary_value = ''
    while len(binary_value) != 0:
        temp_binary_value = binary_value[:64]
        binary_value = binary_value[64:]
        changed_value = ''
        
        for i in range(0, 64):
            j = inverse_ip[i] - 1
            changed_value = changed_value + temp_binary_value[j]

        permutated_binary_value = permutated_binary_value + changed_value
    return permutated_binary_value

def main():
    fi = open('inputDES.txt','r')
    fo = open('outputDES.txt','w')
    binary_value = ""
    final_text = ""

    #read file
    mode = fi.readline()

    #turn input file to bits
    with fi as openfileobject:
        for line in openfileobject:
            binary_value = binary_value + to_binary(line)

    fi.close()

    #pad if number of characters is not divisible of 8
    while (len(binary_value) % 64 != 0):
        binary_value = binary_value + '00000000'

    #initial permutation (w/ ip_table)
    binary_value = initial_permutation(binary_value)

    #determine if encrypt or decrypt

    if (mode[0] == 'e'):
        print("encrypt")
        #encrypt 8 rounds
        for i in range(0,8):
            print(i)
            left_bits = binary_value[32:64]
            print(left_bits)
            right_bits = binary_value[0:32]
            print(right_bits)

            new_bin = right_bits + left_bits
            print(new_bin)

    elif (mode[0] == 'd'):
        print("decrypt")
        #decrypt 8 rounds
        for i in range(0,8):
            print(i)

    else:
        print("mode not set")

    #final permutation (w/ inverse_ip)
    binary_value = final_permutation(binary_value)

    #for loop for how many 8bin there are
    while (len(binary_value) != 0):
        firstchar = binary_value[:8]
        binary_value = binary_value[8:]
        final_text = final_text + from_binary(firstchar)

    fo.write(final_text)
    fo.close()


generate_keys(16)
for zzz in keys:
    print(zzz)


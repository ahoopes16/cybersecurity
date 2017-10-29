import threading
import datetime
from DES import encrypt

P = C = ''

def to_binary(line):
    binary_line = format(line, '056b')
    return binary_line

def breakDES(tfirst,tlast):
    global P
    global C
    start = datetime.datetime.now()
    for k in range(tfirst,tlast):

        # find encryptedP
        bin_k = to_binary(k)
        encryptedP = encrypt(P, bin_k)
        
        if encryptedP == C:
           end = datetime.datetime.now()
           print("*^* " + str(bin_k) + " *^*")

           pfile = open("found_key.txt", 'w')
           pfile.write("Thread Victorious ... " + str(tfirst) + " - " + str(tlast))
           pfile.write("\n")
           pfile.write("thread started  : " + str(start))
           pfile.write("\n")
           pfile.write("thread finished : " + str(end))
           pfile.write("\n")
           pfile.write("Key Found: " + str(bin_k))
           pfile.close()
           
           # stop all threads & machines
           break
    
    print("Thread Complete Over: " + str(tfirst) + " to " + str(tlast) + " ** ")
    
def main():
    global P
    global C
    
    machine_num = 0
        
    plain_txt ='P.txt'
    cipher_txt ='C.txt'
    
    pfile = open(plain_txt, 'r')
    cfile = open(cipher_txt, 'r')

    # read in the values of p and c
    P = pfile.read()
    print("P = " + P)
    C = cfile.read()
    print("C = " + C)

    pfile.close()
    cfile.close()

    num_machines = 12
    num_threads = 5

    afirst = 0
    #alast = 72057594037927940
    alast = 1000000
    agap = alast / num_machines

    mfirst = (int(afirst + (agap*machine_num)))
    mlast = (int(afirst + (agap*(machine_num+1))) + 1)

    mgap = (mlast - mfirst) / num_threads

    tfirst = []
    tlast = []

    tfirst.append(mfirst)
    
    for i in range(4):
        interval = int(mfirst + (mgap*(i+1)))
        tfirst.append(interval)
        tlast.append(interval)

    tlast.append(mlast + 5)

    threads = []
    for i in range(5):
        print("Thread " + str(i) + " range " + str(tfirst[i]) + " : " + str(tlast[i]))
        t = threading.Thread(target=breakDES, args=(tfirst[i],tlast[i]))
        threads.append(t)
        t.start()

main()

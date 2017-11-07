import threading
import datetime
from DES import encrypt
from termserver import create_server
from client import Client

"""
Program used to break the DES algorithm by brute force checking the keys in 
tandem with 11 other computers using 5 threads each. Written for the completion 
of Project Part 2 Submission assigned by Dr. Jaiswal for CS 455.
@authors Adam Callanan, Sage Elfanbaum, Kevin Hoopes, Dustin Roan, Jeremy Schmich
@version 10/30/2017
"""

# Global variables
P = C = ''
terminate = False


def to_binary(line):
    """
    Convert a given line to binary, meant for use with integers in this case
    :param line: the line to be converted
    :return: the line in binary
    """
    binary_line = format(line, '056b')
    return binary_line


def break_des(tfirst, tlast):
    """
    Try keys within the specified range. If a key works,
    print it out to a file with the length of time it took.
    Meant to be used as the target of threads.
    :param tfirst: starting key
    :param tlast: ending key
    """
    global P
    global C
    global terminate
    start = datetime.datetime.now()
    
    log_name = str(tfirst) + "_log.txt"
    
    logfile = open(log_name, 'a')
    logfile.write("Thread " + str(tfirst) + " - " + str(tlast))
    logfile.write("\n")
    logfile.close()


    # Check all keys k in given range for the thread
    for k in range(tfirst, tlast):

        # Find encrypted_p
        bin_k = to_binary(k)
        encrypted_p = encrypt(P, bin_k)

        # If encryption with key k equals ciphertext, print to file and terminate
        if encrypted_p == C:
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

            terminate = True
            Client('150.243.146.253', 10001).main()  # Change to dedserver IP address and port
        # Trigger if another thread finds the key
        elif terminate:
            print("Thread terminated before Key was found")
            break
        # about every hour, add a checkpoint in case of a crash
        elif (k % 1000000 == 0):
            logfile = open(log_name, 'a')
            logfile.write("Checkpoint " + str(k))
            logfile.write("\n")
            logfile.close()
            
    print("Thread Complete Over: " + str(tfirst) + " to " + str(tlast) + " ** ")


def terminate_des():
    """
    Create the terminal server for this machine to wait
    for a connection from ded_server. If connection received,
    terminate threads
    """
    global terminate
    terminate = create_server()


def main():
    """
    Main program
    Determine ranges for threads, establish and start threads
    """
    global P
    global C

    machine_num = 2

    # Read in given plaintext and ciphertext and close files
    plain_txt = 'P.txt'
    cipher_txt = 'C.txt'
    pfile = open(plain_txt, 'r')
    cfile = open(cipher_txt, 'r')
    P = pfile.read()
    C = cfile.read()
    pfile.close()
    cfile.close()

    num_machines = 12
    num_threads = 5

    afirst = 0
    alast = 72057594037927940
    agap = alast / num_machines

    mfirst = (int(afirst + (agap * machine_num)))
    mlast = (int(afirst + (agap * (machine_num + 1))) + 1)
    mgap = (mlast - mfirst) / num_threads

    tfirst = []
    tlast = []

    tfirst.append(mfirst)

    # Determine ranges for each thread to check keys over
    for i in range(4):
        interval = int(mfirst + (mgap * (i + 1)))
        tfirst.append(interval)
        tlast.append(interval)

    tlast.append(mlast + 5)

    # Establish all of the computing threads and start them
    threads = []
    for i in range(5):
        print("Thread " + str(i) + " range " + str(tfirst[i]) + " : " + str(tlast[i]))
        t = threading.Thread(target=break_des, args=(tfirst[i], tlast[i]))
        threads.append(t)
        t.start()

    # Start 6th thread to run the terminal server
    print("Term Server Activated:")
    t = threading.Thread(target=terminate_des)
    threads.append(t)
    t.start()


main()

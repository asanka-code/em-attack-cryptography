#!/usr/bin/python

import time

print("Hello on RPi 3 B+ !")

# XOR encryption between two byte arrays
def xor(data, key):
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))


key = '1111111111'
plaintext = '1010101010'
print("key = %s" % str(key))
print("plaintext = %s" % str(plaintext))
print("\n\n")

# Run continuously
while True:
    for i in range(0, 20000):
        ciphertext = xor(plaintext, key)
        #print("ciphertext = %s" % str(ciphertext))
        decrypted = xor(ciphertext, key)
        #print("decrypted = %s" % str(decrypted))


    #print("Sleeping...")
    time.sleep(2)

print("Exiting...")

#!/usr/bin/python

import time

print("Hello on RPi 3 B+ !")

while True:

    for i in range(0, 20000):
        a = 10 + 20
        print("In the loop i=%d" % i)

    print("Sleeping...")
    time.sleep(2)

'''
while True:

    for i in range(0, 10000):
        a = 10 + 20
        print("In the loop i=%d" % i)

    for i in range(0, 10000):
        b = a
        print("In the loop i=%d" % i)

    print("Sleeping...")
    time.sleep(1)
'''

print("Exiting...")

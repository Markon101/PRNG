import time
import numpy as np
import cv2

# Getting video capture from webcam
vidc = cv2.VideoCapture(0)

testlist = [] 
while True:
    # Get a seed value from system time each loop
    seed = time.time()
    # Get frame
    if vidc.isOpened():
        returnvalue, frame = vidc.read()
    # Get clock
    clk = time.clock_gettime(1)
    # Do x interations of the algorithm
    for i in range(30):
        # Add the value of 400 pixels to the clk variable
        for x in range(400):
            for y in range (400):
                clk += frame[x][y][1]*2
        clk += seed
        clk = int(clk) >> 2
        clk += int(clk) % 3
        clk *= int(clk) % 2 + 1
        if(i != 0):
            clk += clk % i
        clk += clk % 2
        clk *= 4
        if(clk not in testlist):
            print(clk)
        # Test list for debugging PRNG
        testlist.append(clk)
    
    if(len(testlist) > 2000):
        testlist = []
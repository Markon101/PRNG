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
    pixel = frame[300][300][1]
    pixel_2 = frame[55][20][1]
    pixel_3 = frame[400][400][1]
    # Get clock
    clk = time.clock_gettime(1)
    for i in range(20):
        if (pixel < cv2.INTER_MAX):
            pixel *= 2 + pixel_2 + pixel_3
        clk += clk+pixel
        clk += seed
        clk = np.right_shift(int(clk), 2)
        clk += int(clk) % 3
        clk *= int(clk) % 2 + 1
        clk += clk % i
        if(clk not in testlist):
            print(clk)
        # Test list for debugging PRNG
        testlist.append(clk)
    
    if(len(testlist) > 2000):
        testlist = []
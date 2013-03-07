import sys,time,os
timeend = time.time()
while time.time() < timeend + 1:
    time.sleep(0.25)
    print( 'time - '+str(time.time()) )
    print( 'process - '+str(os.getpid()) )

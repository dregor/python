import time,os
timeend = time.time()
while time.time() < timeend + 10:
    #print( 'time - '+str(time.time()) )
    print( 'process - '+str(os.getpid()))

import time
from datetime import datetime
def sagar(a,b):
    return(a+b)

def harry(a,b):
    if(a>0 and b>0):
        pass
    sum([4,5])
    return a+b
    
if __name__=="__main__":
    initial=time.time()
    for i in range(0,100000):
        harry(3,4)
    print("Total time harry function take is",time.time()-initial)
    initial= time.time()
    for i in range(0,100000):
        sagar(3,4)
    print("Total time sagar function take is",time.time()-initial)
import numpy as np
def difference2D(a,b):
    c=a[0]-b[0],a[1]-b[1]
    return c

def sum2D(a,b):
    c=a[0]+b[0],a[1]+b[1]
    return c

def neighbors(arr,x,y,n):
    '''
    Given a 2D-array, returns an nxn array whose "center"
    element is arr[x,y]
    !!ATTENTION!!
    n is how many cells to include for each side:
        example:
            0  0  0  0  0
            0  1  1  1  0
            0  1  5  1  0
            0  1  1  1  0
        to obtain:
            1  1  1
            1  5  1
            1  1  1
        n=1
    This workout is needed to avoid repeated division which is
    computationally expensive, I know python it s not performance but
    it s far more expensive as I tested.
    '''
    arr=np.roll(np.roll(arr,shift=-x+n,axis=0),shift=-y+n,axis=1)
    return arr[:2*n+1,:2*n+1]

def updatePBC(A,B,x,y,n):
    A=np.roll(np.roll(A,-x+n,axis=0),-y+n,axis=1)
    A[0:2*n+1,0:2*n+1]=B
    A=np.roll(np.roll(A,+x-n,axis=0),+y-n,axis=1)
    return A

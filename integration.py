#Code adapted from https://uweb.engr.arizona.edu/~edatools/Phys305/integration.html

# integration.py                         Phys 305        David MacQuigg  1/28/10

'''
    Illustrating the use of Python to teach math and science.  The main purpose of
    Python is clarity.  Later we will re-write these functions in C for 100X boost
    in speed.  For now, we are just trying to understand some algorithms used in
    numerical integration, including their accuracy and relative speed.  There is a
    lot of "overhead" in most languages if you want nice printouts, timings, etc.
    Python minimizes that overhead.
'''

def f(x):  
    return 0.5 + x*x  # This is the function we will integrate.


def integLeft(a, b, f, nbins=10):
    '''Return the integral from a to b of function f using the left hand rule
        integLeft(0, 1, f, 4)
        0.71875
    '''
    h = float(b-a)/nbins    # allow input of integer a and b
    assert h > 0            # warn if b not > a
    assert type(nbins) == int
    
    sum = 0.0
    for n in range(nbins):  # [0, 1, ... nbins-1]
        sum = sum + h * f(a + n*h)   # left hand rule

    return sum

def integMid(a, b, f, nbins=10):
    
    '''Return the integral from a to b of function f using the midpoint rule
        integMid(0, 1, f, 4)
        0.828125
    '''
    h = float(b-a)/nbins
    assert h > 0
    assert type(nbins) == int
    
    sum = 0.0
    x = a + h/2                  # first midpoint
    while (x < b):
        sum += h * f(x)
        x += h

    return sum

def integTrap(a, b, f, nbins=10):
    '''Return the integral from a to b of function f using trapezoidal rule
        integTrap(0, 1, f, 4)
        0.84375
    '''
    h = float(b-a)/nbins
    assert h > 0
    assert type(nbins) == int
    
    sum = (h/2) * (f(a) + f(b))  # endpoints are special
    for n in range(1, nbins):    # [1, 2, ... nbins-1]
        sum += h * f(a + n*h)
    
    return sum


if __name__ == '__main__':
  
    def table_of_errors(a, b, f, exact):
        
        '''
            Print timings and a table of errors comparing these integration methods to
            an exact result.  Show how the error decreases as o(1/nbins) or
            o(1/nbins**2), depending on the method.
       '''

        print()
        print ("nbins       Left         Mid           Trap")

        for nbins in [4, 40, 400]:
            print ('%4s %13.9f %13.9f %13.9f' % (nbins, integLeft(a,b,f,nbins), integMid(a,b,f,nbins), integTrap(a,b,f,nbins)))
        
        print()

        for nbins in [4, 40, 400]:
            print ('%4s %13.9f %13.9f %13.9f' % (nbins, integLeft(a,b,f,nbins) - exact, integMid(a,b,f,nbins) - exact,  integTrap(a,b,f,nbins) - exact ))
        print()

        iterations = 1000

        from time import time  # from time module import time function
        t0 = time()  # seconds
        integLeft (0, 1, f, iterations)
        t1 = time()
        integMid  (0, 1, f, iterations)
        t2 = time()
        integTrap (0, 1, f, iterations)
        t3 = time()
        
        print (f"Time for {iterations} bins:\n    %13.6f %13.6f %13.6f" % ( (t1-t0), (t2-t1), (t3-t2) )  )


    table_of_errors(0, 1, f, 5/6.)




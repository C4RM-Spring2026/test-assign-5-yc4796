def FizzBuzz(start, finish):
    import numpy as np
    numvec = np.arange(start, finish)
    objvec = np.array(numvec, dtype=object)
    
    fizzbuzz = (numvec % 3 == 0) & (numvec % 5 == 0)
    fizz = (numvec % 3 == 0) & (numvec % 5 != 0)
    buzz = (numvec % 3 != 0) & (numvec % 5 == 0)
    
    objvec[fizzbuzz] = 'fizzbuzz'
    objvec[fizz] = 'fizz'
    objvec[buzz] = 'buzz'
    
    return objvec

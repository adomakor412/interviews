from profiler import Profiler
from algorithms import *

def main(sort = selectionSort, lyst = None, size = 15, unique = True,
         comp = True, exch = True, trace = True):
    p = Profiler()
    p.test(selectionSort, None, size, unique, comp, exch, trace)

if __name__ == "__main__":
    main()

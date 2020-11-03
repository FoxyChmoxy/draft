import numpy as np
from timeit import default_timer as timer
from numba import vectorize

@vectorize(["float32(float32, float32)"], target='cuda')
def vector_add(a, b):
    return a + b

def main():
    n = 200_000_000

    a = np.ones(n, dtype=np.float32)
    b = np.ones(n, dtype=np.float32)
    c = np.zeros(n, dtype=np.float32)

    start = timer()
    c = vector_add(a, b)
    vector_add_time = timer() - start
    print("c[:5] = " + str(c[:5]))
    print("c[-5:] = " + str(c[-5:]))

    print(vector_add_time)

if __name__ == "__main__":
    main()
from functions import MPI, send, receive, rank, p, comm
import timeit
import random
import numpy as np

def main():
    size = 1_000_000
    print_enabled = False
    array, data, output = (None, np.empty(size), np.empty(p))

    if rank == 0:
        array = np.random.rand(p, size)
        if print_enabled:
            print("GLOBAL ARRAY:", array)
        
    comm.Scatter(array, data, root=0)

    local_min = data.min()

    if print_enabled:
        print(f"({rank}) LOCAL ARRAY:", data)
        print(f"({rank}) LOCAL MIN:", local_min)

    comm.Gather(local_min, output, root=0)

    if rank == 0:
        if print_enabled:
            print("GLOBAL MIN ARRAY:", output)
        print("GLOBAL MIN:", output.min())
    

if __name__ == "__main__":
    print(timeit.timeit(main, number=1))
    MPI.Finalize 
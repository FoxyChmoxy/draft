from functions import MPI, send, receive, rank, p, comm
import numpy as np
import random
import timeit

def scatter():
    size = 100
    array, data = (None, np.empty(size))

    if rank == 0:
        array = np.random.rand(p, size)
        
    comm.Scatter(array, data, root=0)
    print(rank, data.min())

def gather():
    sendbuf = np.zeros(100, dtype='i') + rank
    recvbuf = None
    if rank == 0:
        recvbuf = np.empty([p, 100], dtype='i')
    comm.Gather(sendbuf, recvbuf, root=0)
    if rank == 0:
        for i in range(p):
            print(recvbuf[i,:], i)

def simple():
    print(min([random.randrange(10, 1_000_000_000) for _ in range(8_000_000)]))

if __name__ == "__main__":
    print(timeit.timeit(simple, number=1))
    MPI.Finalize
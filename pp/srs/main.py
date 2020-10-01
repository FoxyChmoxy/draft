from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
p = comm.Get_size()

GLOBAL_TAG = 11

def scatter(ref, out, root):
    # ref - что отправил
    # out - куда записал
    # root - кто главный
    global comm
    comm.Scatter(ref, out, root=root)

def gather(get, out, root):
    # get - что получил
    # out - куда записал
    # root - кто батька
    global comm
    comm.Gather(get, out, root=root)

if __name__ == "__main__":
    array = None

    print("---------------------")
    print(array)
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
p = comm.Get_size()

GLOBAL_TAG = 11

def send(data, dest):
    return comm.send(data, dest=dest, tag=GLOBAL_TAG)

def receive(source):
    return comm.recv(source=source, tag=GLOBAL_TAG)
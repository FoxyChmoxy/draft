from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
p = comm.Get_size()
GLOBAL_TAG = 11

def main():
    pass

if __name__ == "__main__":
    main()
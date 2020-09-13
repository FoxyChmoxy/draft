from functions import MPI, send, receive, rank, p
import timeit
import random

def main():
    if rank == 0:
        n = int(input("n: "))

        if n <= p:
            print("count of elements should be more than count of processes")
            return 0

        array = [random.randint(-100000000, 100000000) for _ in range(n)]

        # S count of elements for per process = N count of elements / P count of processes 
        # and round to the nearest integer
        s = round(n / p)

        # processes minimum
        mins = [min(array[:s])]

        for pi in range(1, p):
            start = pi * s
            end = start + s
            send(data=array[start:end], dest=pi)
            mins.append(receive(source=pi))
        
        print("processes mins:", mins)
        print("final:", min(mins))
    else:
        parent_process = 0
        array = receive(source=parent_process)
        min_num = min(array)
        send(data=min_num, dest=parent_process)


if __name__ == "__main__":
    print(timeit.timeit(main, number=1))
    MPI.Finalize
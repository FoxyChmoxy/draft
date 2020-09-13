from functions import MPI, send, receive, rank, p

def main():
    data = None
    if rank == p - 1:
        data = 125
        send(data, rank - 1)
    else:
        data = receive(rank + 1)
        if rank != 0:
            send(data, rank - 1)
    print(rank, data)

if __name__ == "__main__":
    main()
    MPI.Finalize
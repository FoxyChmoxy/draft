from functions import MPI, send, receive, rank, p

def main():
    if rank == 0:
        try:
            data = int(input("Введите число: "))
            send(data * 2, rank + 1)
            data = receive(p - 1)
            print(data)
        except:
            send(0, rank + 1)
            data = receive(p - 1)
            print("Произошла ошибка", data)
    else:
        data = receive(rank - 1)
        if rank == p - 1:
            send(data * 2, 0)
        else:
            send(data * 2, rank + 1)

if __name__ == "__main__":
    main()
    MPI.Finalize
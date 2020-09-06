from functions import send, receive, rank, n
import random

def display(rank, data, message):
    print({ "rank" : rank, "data" : data, "message": message})

def main():
    if n % 2 != 0:
        print("n должно быть четным")
        return

    if rank % 2 == 0:
        data = random.randint(1, 10)
        send(data, rank + 1)
    else:
        data = receive(rank - 1)
        display(rank, data, "sending to rank 0")
        send(data, 0)
    
    if rank == 0:
        data = 0
        for i in range(1, n, 2):
            data += receive(i)
        display(rank, data, "final result")

if __name__ == "__main__":
    main()
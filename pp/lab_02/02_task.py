from functions import MPI, send, receive, rank, p
import random

def multiple(array):
    el = array[0]
    for i in range(1, len(array)):
        el *= array[i]
    return el

def main():
    if rank == 0:
        m = int(input("count of subarray:"))
        n = int(input("count of elements:"))

        if n != p:
            print("count of elements should be equals to count of processes")
            return 0
        
        array = [[random.randint(-1000000, 1000000) for _ in range(n)] for _ in range(m)]
        responses = [multiple(array[:][0])]

        for i in range(1, n):
            vector = []
            for j in range(m):
                vector.append(array[j][i])
            send(data=vector, dest=i)
            responses.append(receive(source=i))
        
        print(sum(responses))
    else:
        parent_rank = 0
        vector = receive(source=parent_rank)
        send(data=multiple(vector), dest=parent_rank)

if __name__ == "__main__":
    main()
    MPI.Finalize
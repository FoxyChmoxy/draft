from functions import MPI, send, receive, rank, n
import random

def main():
    array = [random.randint(-1000, 1000) for _ in range(100)]
    

if __name__ == "__main__":
    main()
    MPI.Finalize
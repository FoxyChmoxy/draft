mpiexec -n 4 python $2

# spi = start process index
# epi = end process index

# spi, epi, tag = 10, 1, 11

# comm.send(data, dest=spi-1, tag=tag)

# for i in range(spi, epi, -1):
#     data = comm.recv(source=i, tag=tag)
#     comm.send(data, dest=i-1, tag=tag)

# if rank == epi:
#     data = comm.recv(source=epi+1, tag=tag)
#     print(data)
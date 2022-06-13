from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = [i for i in range(size)]
    print(f"\nInitial data: {data}")
    dest = rank + 1

    print(f"\n{rank}|My message is: {data.pop(0)}")
    comm.send(data, dest=dest)
    print(f"{rank}|Sent data: {data} to process: {dest}")

    source = size - 1
    received_data = comm.recv(source=source)
    print(f"{rank}|Received data: {received_data} from process: {source}")


else:
    source = rank - 1
    received_data = comm.recv(source=source)
    print(f"{rank}|Received data: {received_data} from process: {source}")
    print(f"{rank}|My message is: {received_data.pop(0)}")

    dest = (rank + 1) % size
    comm.send(received_data, dest=dest)
    print(f"{rank}|Sent data: {received_data} to process: {dest}")

# mpiexec -n 4 python Lista2/zad1.py

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    number = 2
    dest = rank + 1
    comm.send(number, dest=dest)
    print(f"\n{rank}|Sent number: {number} to process: {dest}")

    source = 3
    received_number = comm.recv(source=source)
    print(f"{rank}|Received number: {received_number} from process: {source}")


else:
    source = rank - 1
    received_number = comm.recv(source=source)
    print(f"{rank}|Received number: {received_number} from process: {source}")

    dest = (rank + 1) % 4
    number = received_number + np.random.randint(low=1, high=10)
    comm.send(number, dest=dest)
    print(f"{rank}|Sent number: {number} to process: {dest}")

# mpiexec -n 4 python Lista1/zad3.py

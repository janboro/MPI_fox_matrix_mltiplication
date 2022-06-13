from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    number = 2
    dest = 1
    comm.send(number, dest=dest)
    print(f"\n{rank}|Sent number: {number} to process: {dest}")

    received_number = comm.recv(source=dest)
    print(f"{rank}|Received number: {received_number} from process: {dest}")

elif rank == 1:
    source = 0
    received_number = comm.recv(source=source)
    print(f"{rank}|Received number: {received_number} from process: {source}")

    number = received_number + np.random.randint(low=1, high=10)
    comm.send(number, dest=source)
    print(f"{rank}|Sent number: {number} to process: {source}")


# mpiexec -n 2 python Lista1/zad2.py

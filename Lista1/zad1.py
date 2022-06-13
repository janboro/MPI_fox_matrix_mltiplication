from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    number = 2
    dest = 1
    comm.send(number, dest=dest)
    print(f"\n{rank}|Sent number: {number} to process: {dest}")

elif rank == 1:
    source = 0
    received_number = comm.recv(source=source)
    print(f"{rank}|Received number: {received_number} from process: {source}")

# mpiexec -n 2 python Lista1/zad1.py

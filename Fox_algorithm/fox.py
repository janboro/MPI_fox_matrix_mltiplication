# https://cdn.discordapp.com/attachments/905122257402204200/977988614115967036/Fox_example.pdf
#  mpirun --hostfile hostfile -np 25 python fox.py
import time
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

divided_vector_len = 0
matrix_size = 5

if rank == 0:
    A = np.random.randint(low=0, high=10, size=(matrix_size, matrix_size))
    B = np.random.randint(low=0, high=10, size=(matrix_size, matrix_size))

    print(f"\nA:\n{A}")
    print(f"\nB:\n{B}")
    # A = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    # B = np.array([[4, 5, 6], [7, 8, 9], [0, 1, 2]])

    # A = np.array([[0, 1], [2, 3]])
    # B = np.array([[4, 5], [6, 7]])

    # A = np.array([[1]])
    # B = np.array([[4]])
    final_C = np.zeros_like(A)

    start_time = time.time()
    P = np.zeros_like(A)
    process = 0
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(A)[1]):
            P[i][j] = process
            process += 1
    # print(f"P: {P}")

    no_of_processes = np.shape(A)[1]
    dest = 0

    for i in range(np.shape(A)[0]):
        for j in range(np.shape(A)[0]):
            for k in range(np.shape(A)[0]):
                # C[i][j] += A[i][k] * B[k][j]

                comm.send(A[i][k], dest=P[i][j])
                comm.send(B[k][j], dest=P[i][j])
                dest += 1

else:
    no_of_processes = None

no_of_processes = comm.bcast(no_of_processes, root=0)

C = 0
for i in range(no_of_processes):
    A = comm.recv(source=0)
    B = comm.recv(source=0)
    C += A * B

comm.send(C, dest=0)

if rank == 0:
    buffer = []
    for i in range(no_of_processes * no_of_processes):
        c = comm.recv(source=i)
        buffer.append(c)

    for i in range(np.shape(final_C)[0]):
        for j in range(np.shape(final_C)[1]):
            final_C[i][j] = buffer.pop(0)
    end_time = time.time()

    print(f"\nSolution:\n{final_C}")
    print(f"Processing time: {end_time - start_time}")

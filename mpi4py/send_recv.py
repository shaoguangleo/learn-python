#!/usr/bin/env python
# coding=utf-8

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Point2Point communication
data_send = [comm_rank] * 5
comm.send(data_send,dest=(rank+1)%size)
data_recv = comm.recv(source=(rank-1)%size)

print ("My rank is : %d , and I received: " % rank)
print data_recv

#!/usr/bin/env python
# coding=utf-8

from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()

if rank == 0 :
    data = {'a':1,'b':2,'c':3}
    comm.send(data,dest = 1, tag = 123)
    print 'Now send data on %d' % rank
elif rank == 1:
    data = comm.recv(source = 0, tag = 123)
    print 'Now recv data on %d' % rank
    print data
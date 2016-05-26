#!/usr/bin/env python
# coding=utf-8

from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()

if rank == 0 :
    data = {'a':1,'b':2,'c':3}
    req = comm.isend(data,dest = 1, tag = 123)
    req.wait()
    print 'Now send data on %d' % rank
elif rank == 1:
    req = comm.irecv(source = 0, tag = 123)
    data = req.wait()
    print 'Now recv data on %d' % rank
    print data
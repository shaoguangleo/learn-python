#!/usr/bin/env python
# coding=utf-8

from mpi4py import MPI

rank = MPI.COMM_WORLD.Get_rank()

print ("Hello World!")
print ("My rank is : %d " % rank)

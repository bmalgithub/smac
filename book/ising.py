# Copyright (C) 2018 Greenweaves Software Limited

# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>

import math

# Nbr
#
# Find neighbours in rectangular array indexed: 0, 1, ... m*n-1
#
# 0 [2, 1]
# 1 [3, 0]
# 2 [0, 3]
# 3 [1, 2]
#  0 [3, 1]
#  1 [4, 0, 2]
#  2 [5, 1]
#  3 [0, 6, 4]
#  4 [1, 7, 3, 5]
#  5 [2, 8, 4]
#  6 [3, 7]
#  7 [4, 6, 8]
#  8 [5, 7]
def Nbr(k,m,n,periodic=False):
    neighbours = []
    def add_periodic(k,incr):
        candidate = k + incr
        if abs(incr)==1:
            while candidate//n < k//n:
                candidate += n
            while candidate//n > k//n:
                candidate -= n            
        else:
            while candidate<0:
                candidate += m*n
            while candidate>=m*n:
                candidate -= m*n
        if candidate != k and not candidate in neighbours:
            neighbours.append(candidate)
        
    def add_if_possible(k,incr):
        candidate = k + incr
        if -1 < candidate and candidate < m*n:
            if abs(incr)==1:
                if candidate//n == k//n:   # Same row?
                    neighbours.append(candidate)   
            else:
                if abs(incr)==n:   # Same column?
                    neighbours.append(candidate)  
     
    def add(k,incr):
        if periodic:
            add_periodic(k,incr)
        else:
            add_if_possible(k,incr)
            
    if k<m*n and k>-1:
        add(k,-n)
        add(k,+n)
        add(k,-1)
        add(k,+1)
        
    return neighbours
    
def gray_flip(tau,N):
    k = tau[0]
    if k<N:
        tau[k-1] = tau[k]
        tau[k] = k+1
        if (k != 1): tau[0] = 1
    return k,tau

def flip(ch):
    return '+' if ch =='-' else '-'

def enumerate_ising(m,n,periodic=True):
    N         = m * n
    Ns        = {}
    sigma     = [-1]  *N
    tau       = list(range(1,(N+1)+1))
    E         = -2 * N
    Ns[E]     = 2
    spins     = ''.join([('+' if sigma[j]>0 else '-') for j in range(N)])
    #print ('{0} {1} h={2},E={3},N={4}'.format('-', spins, '-', E, Ns[E+2*N]))
    for i in range(2**(N-1)-1):
        k,tau     = gray_flip(tau,N)
        k         -= 1
        h         = sum(sigma[j] for j in Nbr(k,m,n,periodic=periodic))
        E         += (2*sigma[k] * h)
        #print (i,E,2**(N-1)-1,k,Nbr(k,m,n,periodic=periodic))
        if not E in Ns:
            Ns[E] = 0
        Ns[E] += 2

        sigma[k]  = -sigma[k]
        spins     = ''.join([('+' if sigma[j]>0 else '-') for j in range(N)])
        #print ('{0} {1} h={2},E={3},N={4}'.format(k, spins, h, E, Ns[E+2*N]))
    return [(E,Ns[E]) for E in sorted(Ns.keys())]

if __name__=='__main__':
    #for i in range(9):
        #print (i,Nbr(i,3,3))
    #for i in range(16):
        #print (i,Nbr(i,4,4,periodic=True))
    for E,Ns in enumerate_ising(6,6):
        print (E,Ns)
    
    #N=4
    #tau = list(range(1,N+1+1))
    #spins = '-'*N
 
    #for i in range(2**N):
        #k,tau=gray_flip(tau,N)
        #print (i+1,spins,k,tau)
        #spins = ''.join([flip(spins[j]) if j==k-1 else spins[j] for j in range(N)])
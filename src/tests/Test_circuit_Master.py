#===============================================================================
# Doctoral student: Anderson Santos Nunes
# Date:24/02/2014
# University: UFSC - GRUCAD
#===============================================================================

#===============================================================================
# Import modules following official guidelines:
#===============================================================================
import numpy as np
import Solver
import scipy
import string
clear_all()
#===============================================================================
# Variables
#===============================================================================

##Branch impedance matrix
Zb=np.zeros((17,17))
Zb[0,0]=530516476.972984
Zb[1,1]=68209261.325098
Zb[2,2]=26793761.463282
Zb[3,3]=14283135.9185034
Zb[4,4]=8869315.71409943
Zb[5,5]=6041077.8951375
Zb[6,6]=4378866.15914209
Zb[7,7]=3319416.22132707
Zb[8,8]=2602822.54214739
Zb[9,9]=2095595.23128621
Zb[10,10]=1723433.09695756
Zb[11,11]=1442302.47876816
Zb[12,12]=1224758.69649317
Zb[13,13]=1052973.15939259
Zb[14,14]=914955.565400924
Zb[15,15]=802400.994641028
Zb[16,16]=709409.484977719
#
rows,cols=Zb.shape
Yb=np.zeros((17,17))
for row in range(0,rows):
    for col in range(0,cols):
        if row==col:
            Yb[row,col]=1.0/Zb[row,col]
#
##Nodal incidence matrix
A=np.array([
[1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[-1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,-1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,-1,0,0,1,0,1,0,0,0,0,0,0,0,0,0],
[0,0,0,-1,0,-1,1,0,1,0,0,0,0,0,0,0,0],
[0,0,0,0,-1,0,-1,0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,-1,0,0,-1,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,-1,0,1,-1,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,-1,0,1,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,-1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,-1]])
#
##Branch source matrix
F=np.zeros((17,1))
F[5,0]=1000
F[6,0]=1000
F[10,0]=1000
F[11,0]=1000

flux_nodal=Solver.solve_node_circuit(A,Yb, F)
flux_nodal_1=Solver.solve_nodal_circuit(A,Yb, F)

B=np.array([
[-1,0,0,0,0,0],
[0,-1,0,0,0,0],
[1,0,0,0,0,0],
[-1,1,0,0,0,0],
[0,-1,0,0,0,0],
[1,0,-1,0,0,0],
[0,1,0,-1,0,0],
[0,0,1,0,0,0],
[0,0,-1,1,0,0],
[0,0,0,-1,0,0],
[0,0,-1,0,1,0],
[0,0,0,-1,0,1],
[0,0,0,0,1,0],
[0,0,0,0,-1,1],
[0,0,0,0,0,-1],
[0,0,0,0,1,0],
[0,0,0,0,0,1]])
#
#!/usr/bin/python3

from message import *
from generation import *
from attack import *
from client import *

from random import *
import sys
import time



def test_all_cs(ci, nb_try, nb_structure, connection, len_cs) :
    A=Attack()
    tab_len_cs=[8,28,56,70]
    size_result=tab_len_cs[len_cs-1]

    result=[]
    for i in range(size_result): 
        result.append(0)

    for index in range(nb_try):
        for index2 in range(nb_structure) :
            structure = get_structure(connection, ci)
            offset=0
            
            if len_cs==2 :
                for i in range(7) :
                    for j in range(i+1, 8) :
                        cs=[[(1,i+8),(1,j+8)]]
                        r = A.process_structure(structure,cs)
                        result[offset] += r
                        offset+=1
                        
            elif len_cs==3:
                for i in range(6) :
                    for j in range(i+1, 7) :
                        for k in range(j+1, 8) :
                            cs=[[(1,i+8),(1,j+8),(1,k+8)]]
                            r = A.process_structure(structure,cs)
                            result[offset] += r
                            offset+=1
                            
            elif len_cs==4:
                for i in range(5) :
                    for j in range(i+1, 6) :
                        for k in range(j+1, 7) :
                            for l in range(k+1, 8) :
                                cs=[[(1,i+8),(1,j+8),(1,k+8),(1,l+8)]]
                                r = A.process_structure(structure,cs)
                                result[offset] += r
                                offset+=1
                                
    for i in range(len(result)) :
        result[i] = (result[i]/nb_try)

    A.result_analysis(result, ci, len_cs, 50)




def test(connection):
    xor=1
    L=Lilliput(6)
    nb_message =2**7
    nb_try=20
    len_ci=2
    len_cs=2

    if xor==1:
        nb_structure=int(((nb_message*(nb_message-1)/2)//120 +1))
        nb_message=nb_structure*16

    if len_ci==2:
        for ii in range(7) :
            for jj in range(ii+1, 8) :
                #Input condition
                ci=[ii+8,jj+8]
                test_all_cs(ci, nb_try, nb_structure, connection, len_cs)
    elif len_ci==3:
        for ii in range(6) :
            for jj in range(ii+1, 7) :
                for kk in range(jj+1, 8) :
                    #Input condition
                    ci=[ii+8,jj+8,kk+8]
                    test_all_cs(ci, nb_try, nb_structure, connection, len_cs)
    elif len_ci==4:
        for ii in range(5) :
            for jj in range(ii+1, 6) :
                for kk in range(jj+1, 7) :
                    for ll in range(kk+1, 8):
                        #Input condition
                        ci=[ii+8,jj+8,kk+8,ll+8]
                        test_all_cs(ci, nb_try, nb_structure, connection, len_cs)
    elif len_ci==5:
        for ii in range(4) :
            print(ii)
            for jj in range(ii+1, 5) :
                for kk in range(jj+1, 6) :
                    for ll in range(kk+1, 7):
                        for mm in range(ll+1, 8):
                            #Input condition
                            ci=[ii+8,jj+8,kk+8,ll+8,mm+8]
                            test_all_cs(ci, nb_try, nb_structure, connection, len_cs)
                            
    if len_ci==1:
        for ii in range(8) :
            #Input condition
            ci=[ii+8]
            test_all_cs(ci, nb_try, nb_structure, connection, len_cs)


def try_attack(c) :
    L=Lilliput(6)
    ci,cs=[9,13],[[(1, 8), (1, 14)]]
    A=Attack()
    nb_message = 4
    nb_try=50

    r=0
    nb_structure=int(((nb_message*(nb_message-1)/2)//120 +1))
    nb_message=nb_structure*16
    
    for index in range(nb_try):
        for index2 in range(nb_structure) :
            structure = get_structure(c, ci)
            r += A.process_structure(structure,cs)
    r/=nb_try

    print(ci, cs, r)
    print()


c=connection(0)
print("Test of the distinguishing attack on 6 rounds.")
try_attack(c)
print("Research of all attacks on 6 rounds with 68 structures.")
test(c)
connection(1,c)


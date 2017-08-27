#!/usr/bin/python3

from message import *
from generation import *
from attack import *

import socket


def generate_structure(L, ci, xor) :
    m=Message()
    structure = Structure()
    result=structure.generate(L,m,ci,xor)
    return structure


def structure2Str(tab) :
    result=""
    for i in tab :
        result = result + str(i[0]) + " " + str(i[1]) + " "
    return result



def precompute(L,len_ci,xor) :
    size=len_ci
    tab_structure={}

    if size == 5:
        for i in range(4):
            for j in range(i+1,5):
                for k in range(j+1,6):
                    for l in range(k+1,7):
                        for m in range(l+1,8):
                            ci=[i+8,j+8,k+8,l+8,m+8]
                            string_ = str(generate_structure(L,ci,xor))
                            tab_structure[i+8,j+8,k+8,l+8,m+8] = string_

    if size == 4:
        for i in range(5):
            for j in range(i+1,6):
                for k in range(j+1,7):
                    for l in range(k+1,8):
                        ci=[i+8,j+8,k+8,l+8]
                        string_ = str(generate_structure(L,ci,xor))
                        tab_structure[i+8,j+8,k+8,l+8] = string_
    elif size==3:
        for i in range(6):
            for j in range(i+1,7):
                for k in range(j+1,8):
                    ci=[i+8,j+8,k+8]
                    string_ = str(generate_structure(L,ci,xor))
                    tab_structure[i+8,j+8,k+8] = string_
    elif size==2 :
        for i in range(7):
            for j in range(i+1,8):
                ci=[i+8,j+8]
                string_ = str(generate_structure(L,ci,xor))
                tab_structure[i+8,j+8] = string_

    elif size==1 :
        for i in range(8) :
            ci=[i+8]
            string_=str(generate_structure(L,ci,xor))
            tab_structure[i+8]=string_

    return tab_structure



def list2Key(string_rcv) :
    return string_rcv.split(' ')

def getKey(string_rcv) :
    msg_list = list2Key(string_rcv)
    for i in range(len(msg_list)):
        msg_list[i]=int(msg_list[i])

    if len(msg_list)==1:
        return msg_list[0]
    else:
        msg_tuple=tuple(msg_list)
        return msg_tuple


def ci2Str(ci) :
    result=""
    for i in ci:
        result=result+str(i)+" "
    return result[:-1]


L=Lilliput(6)
len_ci=2
r=0
xor=1

print("Wait")
tab_structure=precompute(L,len_ci,xor)
print("We can start now")

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind(('',12801))
connection.listen(20)
connection_client, connection_info = connection.accept()

while True:
    msg = connection_client.recv(4096)
    msg=msg.decode()

    if msg == "end":
        break

    key=''
    msg_list = list2Key(msg)
    for i in range(len(msg_list)):
        msg_list[i]=int(msg_list[i])

    if len(msg_list)==1:
        key=msg_list[0]
    else:
        msg_tuple=tuple(msg_list)
        key=msg_tuple

    connection_client.send(tab_structure[key].encode())
    tab_structure[key]=str(generate_structure(L,msg_list,xor))



connection_client.close()
connection.close()


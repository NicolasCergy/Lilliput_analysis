import socket





def connection(flag, c=None) :
    if flag==0:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect(('localhost', 12801))
        return connection

    else :
        c.send("end".encode())
        c.close()
        return 0
        


def ci2Str(ci) :
    result=""
    for i in ci:
        result=result+str(i)+" "
    return result[:-1]


def get_structure(connection, ci) :
    """read a structure"""
    result=[]
    connection.send(ci2Str(ci).encode())
    msg_r = connection.recv(4096).decode()
    list_=msg_r.split(';')

    for i in list_ :
        list_message = i.split(',')
        m=list_message[0].split(' ')
        c=list_message[1].split(' ')
        for j in range(16) :
            m[j]=int(m[j])
            c[j]=int(c[j])

        result.append((m,c))
    return result



def get_list_structure(connection, ci, size) :
    result=[]
    msg_send=ci2Str(ci).encode()
    for index in range(size):
        result.append([])
        connection.send(msg_send)
        msg_r = connection.recv(4096).decode()
        
        list_=msg_r.split(';')

        for i in list_ :
            list_message = i.split(',')
            m=list_message[0].split(' ')
            c=list_message[1].split(' ')
            for j in range(16) :
                m[j]=int(m[j])
                c[j]=int(c[j])

            result[index].append((m,c))
    return result
    

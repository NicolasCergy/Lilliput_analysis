
from random import randrange
from lilliput import *



class Message :
    """
    Messages management
    """

    def __init__(self, copy=None) :
        if isinstance(copy, Message) :
            self.I=[copy.I[x] for x in range(16)]
        else :
            if isinstance(copy, list) :
                self.I=[copy[x] for x in range(16)]
            else :
                self.I=[randrange(16) for x in range(16)]

    def print_message(self) :
        print([self.I[x] for x in range(16)][::-1], end="")

    def __str__(self) :
        result=""
        for i in range(16) :
            result = result+str(self.I[i])+" "
        return result[:-1]

    def generate_with_delta(self, ci, xor=1) :
        """
        Generate a specific message:
        - ci : condition on Inputs
        - xor : -> 1 if the difference is similar
                -> 2 if the difference is a non zero value
                -> [3, val] to get a specific value
        """
        I2 = Message(self)
        if xor==1 :
            r=randrange(15)+1
            for i in ci :
                I2.I[i]^=r

        elif xor==2 :
            flag=0
            while flag == 0 :
                flag=0
                for i in ci :
                    r=randrange(15)+1
                    I2.I[i]=self.I[i]^r
                    flag^=r

        elif isinstance(xor, list) :
            if xor[0]==3:
                for i in ci :
                    I2.I[i]=self.I[i]^xor[1]

            elif xor[0]==4:
                for i in range(len(ci)) :
                    I2.I[ci[i]]=self.I[ci[i]]^xor[1][i]
        else:
            for i in ci :
                r=randrange(15)+1
                I2.I[i]=self.I[i]^r

        return I2





class Structure :
    """
    Structure Management
    """

    def __init__(self) :
        self.index_i=0
        self.index_j=1
        self.tab=[]
        self.size=0

    def __str__(self):
        result=""
        for i in self.tab:
            result=result+str(i[0])+","+str(i[1])+";"
        return result[:-1]

    def reset_struct(self) :
        self.tab=[]
        self.size=0
        self.index_i=0
        self.index_j=1


    def generate(self, lilliput, I, ci, xor=1) :
        self.reset_struct()
        C=Message(lilliput.encrypt(I.I))
        self.tab.append([I, C])

        if xor==1 :
            for i in range(1,16) :
                y=[3,i]
                I2=I.generate_with_delta(ci, y)
                C2=Message(lilliput.encrypt(I2.I))
                self.tab.append([I2, C2])

        if xor==0 :
            nb_branch = len(ci)
            nb_bits = 4*nb_branch
            size=2**(nb_bits)

            for i in range(1, size) :
                bit = bin(i)[2:]
                while len(bit) != nb_bits :
                    bit = '0'+bit

                current_delta=[4, []]
                for j in range(nb_branch) :
                    current_delta[1].append(int(bit[4*j:4*(j+1)], 2))

                I2=I.generate_with_delta(ci, current_delta)
                C2=Message(lilliput.encrypt(I2.I))
                self.tab.append([I2, C2])

        if (xor==2) and (len(ci) > 2):
            for i in range(1,15):
                for j in range(i+1,16):
                    if i!=j:
                        y=[4, []]
                        r=0
                        for k in range(len(ci)) :
                            if r==4:
                                r=0
                                y[1].append(j)
                            elif r>=2:
                                y[1].append(i)
                            else:
                                y[1].append(j)
                            r+=1

                        I2=I.generate_with_delta(ci,y)
                        C2=Message(lilliput.encrypt(I2.I))
                        self.tab.append([I2,C2])                    

        self.size=len(self.tab)
        return self.tab


    def increment(self) :
        if self.index_i==(self.size-1) :
            self.index_i=0
            self.index_j=1
            return 0
        self.index_j+=1
        if self.index_j>=self.size :
            self.index_i+=1
            self.index_j=self.index_i+1
        return 1

    def get_couple(self) :
        x=self.index_i
        y=self.index_j
        if self.increment() == 1 :
            return self.tab[x], self.tab[y]
        else :
            return -1, -1


from random import randrange

class Lilliput :
    """
    Lilliput cipher management
    """
    def __init__(self, D) :
        self.D=D
        self.pi=[13,9,14,8,10,11,12,15,4,5,3,1,2,6,0,7]
        self.pii=[self.pi.index(i) for i in range(16)]
        self.S=[4,8,7,1,9,3,2,0xE,0,0xB,6,0xF,0xA,5,0xD,0xC]
        self.RK=[[randrange(16) for i in range(8)] for j in range(D)] 

    def encrypt(self, X) :
        """ X in X0 X1 ... X15 """
        X=X[:]
        for r in range(self.D):
            X[8:16]=[X[i+8]^self.S[self.RK[r][i]^X[7-i]] for i in range(8)]
            X[15]^= X[1]^X[2]^X[3]^X[4]^X[5]^X[6]^X[7]
            X[9:15] =[X[i]^X[7] for i in range(9,15)]
            X=[X[self.pii[i]] for i in range(16)]
        return X


    def decrypt(self, X) :
        X=X[:]
        for r in range(self.D) [::-1]:
            X=[X[self.pi[i]] for i in range(16)]
            X[15]^= X[1]^X[2]^X[3]^X[4]^X[5]^X[6]^X[7]
            X[9:15] =[X[i]^X[7] for i in range(9,15)]
            X[8:16]=[X[i+8]^self.S[self.RK[r][i]^X[7-i]] for i in range(8)]
        return X



    def lilliput_tour(self, X):
        L=[X]
        for r in range(self.D):
            X=X[:]
            X[8:16]=[X[i+8]^self.S[self.RK[r][i]^X[7-i]] for i in range(8)]
            X[15]^= X[1]^X[2]^X[3]^X[4]^X[5]^X[6]^X[7]
            X[9:15] =[X[i]^X[7] for i in range(9,15)]
            X=[X[self.pii[i]] for i in range(16)]
            L.append(X)
        return L



    def lilliput_tour_inv(self, X):
        L=[X]
        for r in range(self.D):
            X=X[:]
            X=[X[self.pi[i]] for i in range(16)]
            X[15]^= X[1]^X[2]^X[3]^X[4]^X[5]^X[6]^X[7]
            X[9:15] =[X[i]^X[7] for i in range(9,15)]
            X[8:16]=[X[i+8]^self.S[self.RK[r][i]^X[7-i]] for i in range(8)]
            L.append(X)
        return L

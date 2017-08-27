from message import *



class Generation : 
    
    def __init__(self, nb_sample=1, nb_message=16, xor=1) :
        """
            - nb_sample : number of sample
            - nb_message : number of messages
        """
        self.xor=xor
        self.list_sample=[]
        self.nb_sample=nb_sample
        self.nb_message=nb_message

        if self.xor==1:
            self.nb_message=((self.nb_message*(self.nb_message-1)/2)//120 +1)*16


    def generate(self, ci, lilliput) :
        """
            - ci: condition on Inputs
        """
        
        self.list_sample=[]

        #For each sample
        for i in range(self.nb_sample) :
            current_nb=0
            self.list_sample.append([])

            while current_nb < self.nb_message :
                m=Message()
                struct=Structure()
                struct.generate(lilliput, m, ci, self.xor)
                self.list_sample[i].append(struct)
                current_nb += len(struct.tab)
        return self.list_sample


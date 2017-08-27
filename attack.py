from generation import *
import sys

class Attack :

    def __init__(self) :
        pass

    def process(self, tab, cs, num_sample_max=0, offset_min=0) :
        
        average=0
        #Number of samples
        nb_sample=len(tab)
        #Number of messages
        nb_struct=len(tab[0])
        size_struct=len(tab[0][0].tab)
        nb_message=(size_struct*(size_struct-1)/2)*nb_struct

        if offset_min>=nb_sample :
            offset_min=0
        if (num_sample_max==0) or ((num_sample_max+offset_min) > nb_sample) :
            num_sample_max=nb_sample
        else :
            num_sample_max+=offset_min

        for sample in range(offset_min, num_sample_max) :
            result=0
            sample_tab=tab[sample]
            
            for struct in sample_tab :
                a=(0,0)
                #for each pair
                while a!= (-1,-1) :
                    a=struct.get_couple()

                    #End condition
                    if isinstance(a[0], int) :
                        continue

                    success=1

                    #For each equation
                    for equation in cs :
                        result_temp=0
    
                        for condition in equation :

                            #Condition on I or S
                            if condition[0] < 2:
                                result_temp^=a[0][condition[0]].I[condition[1]]
                                result_temp^=a[1][condition[0]].I[condition[1]]

                            elif condition[0] == 2:
                                result_temp^=a[0][1].I[condition[1]]
                                result_temp^=a[1][1].I[condition[1]]
                                result_temp^=condition[1]

                        #fail condition
                        if result_temp != 0:
                            success=0
                    
                    if success==1 :
                        result+=1
            average+=result
            permutation_result=nb_message/(2**(4*len(cs)))
            final_result=average/(num_sample_max-offset_min)

        return final_result, num_sample_max-offset_min, nb_struct, size_struct, nb_message, permutation_result, final_result-permutation_result





    def process_structure(self, tab_couples, cs) :
        result=0
        size = len(tab_couples)

        for i in range(size-1):
            for j in range(i+1, size):
                success=1

                #For each equation
                for equation in cs :
                    result_temp=0
                    
                    for condition in equation :
                        #Condition on I or S
                        if condition[0] < 2:
                            result_temp^=tab_couples[i][condition[0]][condition[1]]
                            result_temp^=tab_couples[j][condition[0]][condition[1]]

                        
                        elif condition[0] == 2:
                            result_temp^=tab_couples[i][1][condition[1]]
                            result_temp^=tab_couples[j][1][condition[1]]
                            result_temp^=condition[1]

                    if result_temp != 0:
                        success=0
                
                if success==1 :
                    result+=1
        return result


    def give_attack_cs(self, nb, len_cs) :
        r=0
        if len_cs==1:
            for i in range(8) :
                if r==nb:
                    return [i+8]
                r+=1
        if len_cs==2:
            for i in range(7):
                for j in range(i+1, 8) :
                    if r==nb :
                        return i+8,j+8
                    r+=1

        if len_cs==3:
            for i in range(6):
                for j in range(i+1, 7) :
                    for k in range(j+1, 8) :
                        if r==nb :
                            return i+8,j+8,k+8
                        r+=1
        if len_cs==4:
            for i in range(5):
                for j in range(i+1, 6) :
                    for k in range(j+1, 7) :
                        for l in range(k+1, 8) :
                            if r==nb :
                                return i+8,j+8,k+8,l+8
                            r+=1

        if len_cs==5:
            for i in range(4):
                for j in range(i+1, 5) :
                    for k in range(j+1, 6) :
                        for l in range(k+1, 7) :
                            for m in range(l+1, 8) :
                                if r==nb :
                                    return i+8,j+8,k+8,l+8,m+8
                                r+=1



    def result_analysis(self, result, ci, len_cs, borne=15) :
        borne=510 #2**7 +- 32
        offset=32


#        borne = 32736 
#        offset= 64

#        borne = 131008 
#        offset=362

#        borne=524160
#        offset=724

#        borne=8388096 
#        offset=2896


        for i in range(len(result)) :
            if (result[i] < borne-offset) or (result[i] > borne+offset) :
                cs = self.give_attack_cs(i, len_cs)
                self.print_attack(ci, cs,result[i])
                sys.stdout.flush()



    def print_attack(self, ci, cs, r2) :
 #       print(ci, cs, r2) 
        for i in ci :
            if i == ci[-1] :
                print('I' + str(i+1), end='')
            else :
                print('I' + str(i+1) + ', ', end='')
        print('   ', end='')
        
        for i in cs :
            if i == cs[-1] :
                print('S' + str(i+1), end='')
            else :
                print('S' + str(i+1) + ' + ', end='')

        print(' = ', end='')

        print('   ' + str(r2))



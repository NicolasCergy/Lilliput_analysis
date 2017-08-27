# Lilliput_analysis

Please read this file if you want to use the tool.

To use this tool, you have to use serveur.py with "./serveur.py" or "python3 serveur.py" in order to launch this serveur. 
It generates structure of messages the attackers need. Indeed, an attack can require more messages than the RAM or HDD can contain. 
Thus, this serveur generates a structure and then, once you have managed it, you can request an other one.

In serveur.py, you only need to edit the number of rounds you want to attack for LILLIPUT at the line L=Lilliput(6) for 6 rounds for example.

Then you have to edit "len_ci" to controle the number of input branches involved in the attack according to our paper. 
"len_ci=2" in order to have pairs (m1,m2) such that they are equal on all branches but 2 in the left side and with a common difference.

The second file to edit is "test.py" into the function "test". In this function you can manage "len_ci" and "len_cs" for the number of input branches and output branches respectively according to our paper. 
The len_ci has to correspond with the one in "serveur.py".

You can test only one attack with the function "try_attack(c)" by choosing directly the inpu and output conditions "ci,cs". 
The function try is to test an attack and the function test is to research all attacks for a given number of rounds.

Finally, to use the tool, please launch ./serveur.py and then ./test.py.
By default, as a demonstration, it tests the distinguishing attack on 6 rounds, and then it processes a complete research of attacks on 6 rounds.

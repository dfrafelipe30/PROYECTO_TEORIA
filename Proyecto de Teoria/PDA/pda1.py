from PDA_class import PDA
import time

#L(M) = {0^n 1 ^n}
states = ['q0','q1','q2','q3']
alphabet  = ['0','1','E']
stackAlphabet = list("01$")
transitions = {
    ('q0','E'):((('E','$'),'q1')),
    ('q1','0'):((('E','0'),'q1')),
    ('q1','1'):((('0','E'),'q2')),
    ('q2','1'):((('0','E'),'q2')),
    ('q2','E'):((('$','E'),'q3'))
    }

    
start = 'q0'
accepts = ['q0','q3']

pda1 = PDA(states,alphabet,stackAlphabet,transitions,start,accepts)




#print pda1.test(list("1"))
#print pda1.generateLanguage(4)
print pda1.max_input_len(8)



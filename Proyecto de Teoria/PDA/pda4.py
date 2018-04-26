from PDA_class import PDA
import time

#L = { a^ibc^i | i > 0 }

states = ['q0','q1','q2','q3']
alphabet  = ['a','b','c','E']
stackAlphabet = list("AB$")
transitions = {
    ('q0','E'):(('E','$'),'q1'),
    ('q1','a'):(('E','A'),'q1'),
    ('q1','b'):(('E','E'),'q2'),
    ('q2','c'):(('A','E'),'q2'),
    ('q2','E'):(('$','E'),'q3')
    }

    
start = 'q0'
accepts = ['q0','q3']

pda4 = PDA(states,alphabet,stackAlphabet,transitions,start,accepts)


#print pda4.test(list("acc"))
#print "El tiempo que tarda la ejecucion es ", (end-begin), " segundos"
#print pda4.generateLanguage(6)
print pda4.max_input_len(10)


    

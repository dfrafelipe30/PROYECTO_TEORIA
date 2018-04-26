from PDA_class import PDA

#L(M) = {wccwR | wR es igual a el inverso de w}
states = ['q0','q1','q2','q3','r']
alphabet = ['0','1','c','E']
stackAlphabet = list("01c$")
transitions = {
    ('q0','E'):(('E','$'),'q1'),
    ('q1','0'):(('E','0'),'q1'),
    ('q1','1'):(('E','1'),'q1'),
    ('q1','c'):(('E','c'),'r'),
    ('r','c'):(('c','E'),'q2'),
    ('q2','0'):(('0','E'),'q2'),
    ('q2','1'):(('1','E'),'q2'),
    ('q2','E'):(('$','E'),'q3')
    }
    

start = 'q0'
accepts = ['q0','q3']

pda3 = PDA(states,alphabet,stackAlphabet,transitions,start,accepts)



#print pda3.test(list("010cc010"))
#print pda3.generateLanguage(6)
print pda3.max_input_len(8)

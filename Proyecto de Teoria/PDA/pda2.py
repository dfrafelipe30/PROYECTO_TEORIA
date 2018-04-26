from PDA_class import PDA
import time
# L(M) = { u00v | u = {a,b}*, v = {c,d}* y |u| = |v|}

states = ['q0','q1','r','q2','q3']
alphabet = ['0','a','b','c','d','E']
stackAlphabet = list("01EKX")
transitions = {
    ('q0','E'):(('E','$'),'q1'),
    ('q1','a'):(('E','X'),'q1'),
    ('q1','b'):(('E','X'),'q1'),
    ('q1','0'):(('E','K'),'r'),
    ('r','0'):(('K','E'),'q2'),
    ('q2','c'):(('X','E'),'q2'),
    ('q2','d'):(('X','E'),'q2'),
    ('q2','E'):(('$','E'),'q3')
    }

start = 'q0'
accepts = ['q3']

pda2 = PDA(states,alphabet,stackAlphabet,transitions,start,accepts)

#print pda2.generateLanguage(6)
#print pda2.test(list("ab00dd"))
print pda2.max_input_len(10)


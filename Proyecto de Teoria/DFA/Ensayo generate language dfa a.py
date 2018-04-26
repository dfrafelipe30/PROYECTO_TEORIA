from ndfa import DFA
import logging
states = list("012")
alphabet = ['0','1']
transitions = {
    ('0','0'): '1',
    ('0','1'): '0',
    ('1','1'): '0',
    ('1','0'): '2',
    ('2','1'): '2',
    ('2','0'): '2',
}
start = '0'
accepts = list('0')
dfa_a = DFA(states, alphabet, transitions, start, accepts)
#print dfa_a.generateAll(3)
print " Estas cadenas son aceptadas por el automata 1"
print dfa_a.generateLanguage(20)

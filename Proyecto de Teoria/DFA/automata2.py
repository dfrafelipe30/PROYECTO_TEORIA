from ndfa import DFA
tamanho = 5

#Segundo automata
states = ['q0', 'q1', 'q2']
alphabet = list('10')
transitions = {
    ('q0', '0') : 'q2',
    ('q0', '1') : 'q1',
    ('q1', '0') : 'q0',
    ('q1', '1') : 'q2',
    ('q2', '0') : 'q1',
    ('q2', '1') : 'q0',
    }
start = 'q0'
accepts = ['q1']
dfa2 = DFA(states,alphabet,transitions,start,accepts)

print dfa2.generateAll(tamanho)
print "estos son el lenguaje que acepta el automata"
print dfa2.generateLanguage(tamanho)
print "---------------------------------------"


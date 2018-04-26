from ndfa import DFA
tamanho = 5



#Primer automata
states = ['q0', 'q1', 'q2']
alphabet = list('10')
transitions = {
    ('q0', '0') : 'q1',
    ('q0', '1') : 'q',
    ('q1', '0') : 'q2',
    ('q1', '1') : 'q',
    ('q2', '0') : 'q2',
    ('q2', '1') : 'q2',
    }
start = 'q0'
accepts = ['q0']
dfa1 = DFA(states,alphabet,transitions,start,accepts)
                 
print dfa1.generateAll(tamanho)
print "estos son el lenguaje que acepta el automata"
print dfa1.generateLanguage(tamanho)
print "---------------------------------------"



from ndfa import DFA
tamanho = 5

#Cuarto automata
states = ['q0', 'q1', 'q2','q3','q4']
alphabet = list('ab')
transitions = {
    ('q0', 'a') : 'q1',
    ('q0', 'b') : 'q3',
    ('q1', 'a') : 'q1',
    ('q1', 'b') : 'q2',
    ('q2', 'a') : 'q1',
    ('q2', 'b') : 'q2',
    ('q3', 'a') : 'q4',
    ('q3', 'b') : 'q3',
    ('q4', 'a') : 'q4',
    ('q4', 'b') : 'q3',
    }
start = 'q0'
accepts = ['q1','q3']
dfa4 = DFA(states,alphabet,transitions,start,accepts)

print  dfa4.generateAll(tamanho)
print "estos son los lenguajes que acepta el automata"
print dfa4.generateLanguage(tamanho)

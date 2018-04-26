from ndfa import DFA
tamanho = 5

#Quinto automata
states = ['q0', 'q1', 'q2']
alphabet = list('ab')
transitions = {
    ('q0', 'a') : 'q1',
    ('q0', 'b') : 'q0',
    ('q1', 'a') : 'q2',
    ('q2', 'a') : 'q2',
    ('q2', 'b') : 'q0',
    }
start = 'q0'
accepts = ['q0','q1']
dfa5 = DFA(states,alphabet,transitions,start,accepts)


print  dfa5.generateAll(tamanho)
print "estos son los lenguajes que acepta el automata"
print dfa5.generateLanguage(tamanho)

from ndfa import DFA
tamanho = 4

#tercer atomata
states = ['q0', 'q1', 'q2','q3']
alphabet = list('ab')
transitions = {
    ('q0', 'a') : 'q1',
    ('q0', 'b') : 'q0',
    ('q1', 'a') : 'q2',
    ('q1', 'b') : 'q3',
    ('q2', 'b') : 'q2',
    ('q3', 'a') : 'q3',
    ('q3' ,'b') : 'q3',
    }


start = 'q0'
accepts = ['q0','q2']
dfa3 = DFA(states,alphabet,transitions,start,accepts)

#print "estos son las cadenas de longitud n "
#print dfa3.generateAll(tamanho)
print "Estas son las cadenas que acepta dfa 3:"
print dfa3.generateLanguage(tamanho)


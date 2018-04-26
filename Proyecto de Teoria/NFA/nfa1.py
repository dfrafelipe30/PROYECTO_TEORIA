from NFA import NDFA

states = ['A','B','C','D']
alphabet = list("ab")
transitions = {
    ('A','b'):['B','C'],
    ('B','a'):['D'],
    ('B','b'):['C'],
    ('C','a'):['D']
    }
start = 'A'
accepts = ['D']
nfa = NDFA(states,alphabet,transitions,start,accepts)
print nfa.test("bba")

#intento de NuevosEstados(Q)
Q = set([nfa.start])
estados = set(Q)
#nfa.NuevosEstados(Q,estados)



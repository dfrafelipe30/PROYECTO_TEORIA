from Turing  import TM

states = ['q0','q1','q2','q3','q4']
alphabet = list("abcd")
tapeAlphabet = list("abcdXYB")
transitions = {
    ('q0','X'):('q0','X','D'),
    ('q0','a'):('q1','Y','D'),
    ('q0','b'):('q1','Y','D'),
    ('q1','a'):('q1','a','D'),
    ('q1','b'):('q1','b','D'),
    ('q1','X'):('q1','X','D'),
    ('q1','c'):('q2','X','I'),
    ('q1','d'):('q2','X','I'),
    ('q2','X'):('q2','X','I'),
    ('q2','a'):('q2','a','I'),
    ('q2','b'):('q2','b','I'),
    ('q2','Y'):('q0','Y','D'),
    #Esta transicion envia a q_accept
    ('q0','B'):('q4','B','D'),
    #Estas son transiciones no definidas que envian a q_reject
    ('q0','c'):('q3','c','D'),
    ('q0','d'):('q3','d','D')  
    }

start = 'q0'
accept  = 'q4'
reject = 'q3'

tm1 = TM(states,alphabet,tapeAlphabet,transitions,start,accept,reject)

print tm1.test("bcc")

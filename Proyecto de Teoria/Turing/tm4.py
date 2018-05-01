from Turing import TM
import time

#L(M) = {a^ib^ic^i | i > 0 }

states = ['q0','q1','q2','q3','q4','q5','q6']
alphabet = list("abc")
tapeAlphabet = list("abcXYZB")
transitions = {
    ('q0','a'):('q1','X','D'),
    ('q0','Y'):('q4','Y','D'),
    ('q1','a'):('q1','Y','D'),
    ('q1','Y'):('q1','Y','D'),
    ('q1','b'):('q2','Y','D'),
    ('q2','b'):('q2','b','D'),
    ('q2','Z'):('q2','Z','D'),
    ('q2','c'):('q3','Z','D'),
    ('q3','a'):('q3','a','I'),
    ('q3','b'):('q3','b','I'),
    ('q3','Y'):('q3','Y','I'),
    ('q3','Z'):('q3','Z','I'),
    ('q3','X'):('q0','X','D'),
    ('q4','Y'):('q4','Y','D'),
    ('q4','Z'):('q4','Z','D'),
    #estados de reject
    ('q0','B'):('q6','B','D'),
    ('q0','Y'):('q6','Y','D'),
    ('q0','b'):('q6','b','D'),
    ('q0','c'):('q6','c','D'),
    ('q1','c'):('q6','c','D'),
    ('q1','Z'):('q6','Z','D'),
    ('q2','B'):('q6','B','D'),
    ('q4','Y'):('q4','Y','D'),
    #estados de aceptacion
    ('q4','B'):('q5','B','D'),
    }
start = 'q0'
accept = 'q5'
reject = 'q6'

tm4 = TM(states,alphabet,tapeAlphabet,transitions,start,accept,reject)

w = "abc"
print tm4.test(w)

from Turing import TM
import time

#L(M) = {0^n1^n2 | n > 0 }

states = ['q0','q1','q2','q3','q4','q5']
alphabet = list("012")
tapeAlphabet = list("01BXY")
transitions = {
    ('q0','B'):('q0','B','D'),
    ('q0','0'):('q1','X','D'),
    ('q0','Y'):('q0','Y','D'),
    ('q1','B'):('q1','B','D'),
    ('q1','Y'):('q3','Y','D'),
    ('q1','1'):('q2','Y','I'),
    ('q1','0'):('q1','0','D'),
    ('q2','B'):('q2','B','I'),
    ('q2','0'):('q2','0','I'),
    ('q2','Y'):('q2','Y','I'),
    ('q2','X'):('q0','X','D'),
    ('q3','Y'):('q3','Y','D'),
    ('q3','1'):('q2','Y','I'),
    #estados de reject
    ('q0','1'):('q5','1','D'),
    ('q3','2'):('q5','2','D'),
    #estados de aceptacion
    ('q0','2'):('q4','2','D'),
    }
start = 'q0'
accept = 'q4'
reject = 'q5'

tm4 = TM(states,alphabet,tapeAlphabet,transitions,start,accept,reject)

#w = "001112"
#print tm4.test(w)
n = 5
ini = time.time()
aceptados =  tm4.generateLanguage(n)
print aceptados 
fin = time.time()
print "Tiempo que tarda generateLanguage con n = %d:" %n
print fin - ini


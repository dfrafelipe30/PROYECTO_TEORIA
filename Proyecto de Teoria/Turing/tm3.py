from Turing import TM
import time
#L(M)= {w en sigma* | w = a^n b^n c^n , n>=0 }

states = ['q0','q1','q2','q3','q4','q5','q6']
alphabet = list("abc")
tapeAlphabet = list("abcXYZ")
transitions = {
    ('q0','a'):('q1','X','D'),
    ('q1','a'):('q1','a','D'),
    ('q1','Y'):('q1','Y','D'),
    ('q1','b'):('q2','Y','D'),
    ('q2','b'):('q2','b','D'),
    ('q2','Z'):('q2','Z','D'),
    ('q2','c'):('q3','Z','I'),
    ('q3','Z'):('q3','Z','I'),
    ('q3','b'):('q3','b','I'),
    ('q3','Y'):('q3','Y','I'),
    ('q3','a'):('q3','a','I'),
    ('q3','X'):('q0','X','D'),
    ('q0','Y'):('q4','Y','D'),
    ('q4','Y'):('q4','Y','D'),
    ('q4','Z'):('q4','Z','D'),
    #Esta transicion lleva a q_accept = q5
    ('q4','B'):('q5','B','I'),
    ('q0','B'):('q5','B','I'),
    #Estas transiciones llevan a q_reject = q6
    ('q0','b'):('q6','b','I'),
    ('q0','c'):('q6','b','I'),
    
    }

start = 'q0'
accept = 'q5'
reject = 'q6' # reject se creo solo para poder crear el objeto TM tm3

tm3 = TM(states,alphabet,tapeAlphabet,transitions,start,accept,reject)

w = "aabbcc"
#print tm3.test("w")
n = 10
ini = time.time()
aceptados =  tm3.generateLanguage(n)
fin = time.time()
print "Tiempo que tarda generateLanguage con n = %d:" %n
print fin - ini

#Maximo n para el cual genereateLanguage acaba en menos de 10 minutos:
#para n = 9: 48.77 s


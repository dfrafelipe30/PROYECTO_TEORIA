from Turing  import TM
import time
#L(M) = {uv : u = {a,b}* , v = {c,d}* y |u| = |v|}

states = ['q0','q1','q2','q3','q4','q5','q6'] 
alphabet = list("abcd")
tapeAlphabet = list("abcdXYB")
transitions = {
    ('q0','a'):('q0','a','D'),
    ('q0','B'):('q5','B','I'),
    ('q0','b'):('q0','b','D'),
    ('q0','c'):('q1','X','I'),
    ('q0','d'):('q1','X','I'),
    ('q1','a'):('q2','Y','D'),
    ('q1','b'):('q2','Y','D'),
    ('q1','X'):('q1','X','I'),
    ('q1','Y'):('q1','Y','I'),
    ('q2','Y'):('q2','Y','D'),
    ('q2','X'):('q3','X','D'),
    ('q3','X'):('q3','X','D'),
    ('q3','c'):('q1','X','I'),
    ('q3','d'):('q1','X','I'),
    ('q3','B'):('q5','B','I'),
    ('q5','X'):('q5','X','I'),
    ('q5','Y'):('q5','Y','I'),
    #Estas transiciones llevan al q_reject = q4
    ('q5','a'):('q4','a','D'),
    ('q5','b'):('q4','b','D'),
    ('q1','B'):('q4','B','D'),
    ('q0','B'):('q5','B','I'),
    ('q3','a'):('q4','a','I'),
    ('q3','b'):('q4','b','I'),
    #Etas transicion lleva a q_accept = q6
    ('q5','B'):('q6','B','D'),
    }

#La direccion de q_accept y q_reject no importa

start = 'q0'
accept  = 'q6'
reject = 'q4'

tm1 = TM(states,alphabet,tapeAlphabet,transitions,start,accept,reject)
w = "abcd"
#print tm1.test(w)

n = 11

ini = time.time()
aceptados = tm1.generateLanguage(n)
fin = time.time()
print "Tiempo que tarda generateLanguage con n = %d: " %n
print fin - ini


#Maximo n para el cual generateLanguage para termina en menos de 10 minutos:
#para n = 11: 52.47 s

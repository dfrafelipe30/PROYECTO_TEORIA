from Turing import TM
import time

states = ['q0','q1','q2','q3','q4']
alphabet = list ("()")
tapeAlphabet = list("()XYB")
transitions = {
    ('q0','X'):('q0','X','D'),
    ('q0','('):('q1','Y','D'),
    ('q1','('):('q1','(','D'),
    ('q1','X'):('q1','X','D'),
    ('q1',')'):('q2','X','I'),
    ('q2','('):('q2','(','I'),
    ('q2','X'):('q2','X','I'),
    ('q2','Y'):('q0','Y','D'),
    #Esta transicion envia a q_reject
    ('q0',')'):('q3',')','D'),
    #Esta transicion lleva a q_accept
    ('q0','B'):('q4','B','D')
    }
#La direccion de q_accept y q_reject no importa

start = 'q0'
accept = 'q4'
reject = 'q3'

tm2 = TM(states,alphabet,tapeAlphabet,transitions,start,accept,reject)

w = "(())"

#print tm2.test("w")

n = 18

#Maximo n para el cual generateLanguage para en menos de 10 minutos:
#para n = 18: 438 s


ini = time.time()
aceptados = tm2.generateLanguage(n)
fin = time.time()
print "Tiempo de ejecucion de generateLanguage con n = %d: " %n
print(fin - ini)

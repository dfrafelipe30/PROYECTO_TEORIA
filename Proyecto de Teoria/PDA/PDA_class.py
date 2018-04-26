import logging
import time
from itertools import product




class PDA(object):

    def __init__(self, states, alphabet,stackAlphabet, transitions, start, accepts):
        assert start in states, \
                'Start state must be a valid state.'
        assert set(accepts).issubset(set(states)), \
                'Accept states must be a subset of states.'
        
        self.states = states
        self.alphabet = alphabet
        self.stackAlphabet = stackAlphabet
        self.transitions = transitions
        self.start = start
        self.accepts = accepts

        

    def test(self, word):
        stack = [] 
        current_state = self.start
        

        #Se agregan los epsilon 'E' al comienzo y al final para las transiciones
        # con $
        word.insert(0,'E')
        word.append('E')
        

        
        logging.info('Testing word "%s"...' % word)
        logging.debug('Initial state: %s' % current_state)
        
        if(word != 'EEE'): #Se evaulua si el input es la cadena vacia 'E'
            
            for symbol in word:
                logging.debug('Current symbol: %s' % symbol)
                assert symbol in self.alphabet, \
                        'Symbol "%s" must be in alphabet.' % symbol

                #Se verifica si la transicion existe

                if((current_state, symbol) in self.transitions ):
                
                    v = self.transitions[(current_state,symbol)]
                    #Este primer if se hace para poner o quitar el '$' en el stack
                    if (v[0][0] != 'E' and v[0][0] != '$' ):
                        #Este if es especificamente para quitar elementos del stack
                        if((v[0][0] == stack[-1] and v[0][1] == 'E') and stack[-1] != '$'):
                            stack.pop()

                        elif(v[0][0] != stack[-1]):
                            #Este elif es para evaluar el caso en el que se leyo todo el input pero que al final no qued el simbolo '$'
                            return False
                        else:
                            if(v[0][1] != 'E'):
                                stack.append(v[0][1])
                    
                    else:
                        #Aqui se ponen elementos en el stack
                        if(v[0][1] != 'E'):
                           stack.append(v[0][1])
                           
                        elif(v[0][0] == stack[-1] and len(stack) != 0):
                            stack.pop()
                    current_state = v[1]

                else:
                    return False
                
                #print "Stack: ",stack    
                    
                assert current_state in self.states, \
                    'Current state must be a valid state.'
            
            logging.debug('New state: %s' % current_state)
        logging.debug('Final state: %s' % current_state)
        logging.info('Accepted: %s\n' % (current_state in self.accepts))
        return current_state in self.accepts and len(stack) == 0

    def generateAll(self,n):
        #Se tuvo que modificar la funcion "generateAll()" ya que el string 'E' estaba definido en el alfabeto pero no se necesita 
        nuevoAlfabeto = self.alphabet[:-1]
        candidatos_posibles = []
        Lal = len(nuevoAlfabeto)
        miListaProv = list(product(nuevoAlfabeto, repeat = n))
        for j in range(len(miListaProv)):
            lista = list(miListaProv[j])
            candidatos_posibles.append(lista) #Aqui se crearon los candidatos
        

        LCand = len(candidatos_posibles)
        for k in range(Lal,LCand): # empieza en la primera lista
            w = ""
            for s in self.states:
                for c in candidatos_posibles[k]:
                    if((s, c) not in self.transitions):
                        del(c)
                        
                    else:
                        w = w + c
                        
        return candidatos_posibles
        
    def generateLanguage(self,n):
        #Se cambio generateLanguage(n) de manera que genere solo las cadenas de longitud n(y no de 1 hasta n)
        #Esto se realizo para que se pueda aumentar de uno en uno la longitud de las cadenas que acepta en un tiempo determinado(ver funcion max_input_len(tiempo))
        todos = self.generateAll(n)
        accepted = []
        for s in todos:
            if(self.test(s) == True):
                accepted.append(s)

        return "Estas son las cadenas que acepta: ",accepted

    

    def max_input_len(self,tiempo):
        
        begin = time.time()
        end = time.time()
        t = end-begin
        n = 1
        #La variable 'error_aprox_tiempo' se creo para tener una aproximacion real al tiempo que se ingresa como parametro en la funcion
        #error_aprox_tiempo varia dependiendo de el PDA y el tiempo que se ejecute la funcion
        error_aprox_tiempo = 1.5
        while( t < tiempo - error_aprox_tiempo):
            if(t >= tiempo):
                n = n-1
                print t
                return "La longitud maxima que puede generar en segundos es " ,n
                
            
            self.generateLanguage(n)
            end = time.time()
            t = end - begin
            
            n = n+1
            
        print t
        return "La longitud maxima que puede generar en segundos es " ,n

            
        
    

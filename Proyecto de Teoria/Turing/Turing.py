from itertools import product

class TM(object):
    def __init__(self,states,alphabet,tapeAlphabet,transitions,start,accept,reject):
        assert start in states, \
               'start state must be a valid state'
        assert accept in states,\
               'accept state must be a subset of states.'
        assert reject in states,\
               'reject state must be a subset of states.'
        self.states = states
        self.alphabet = alphabet
        self.tapeAlphabet = tapeAlphabet
        self.transitions = transitions
        self.start = start
        self.accept = accept
        self.reject = reject

    def test(self,word):
        #print "w = ",word
        current_state =  self.start
       # print "current_state: ",current_state
        cinta = list("BBB"+word+"BBB")
        contador = 3 # para que comience desde el primer simbolo de la cadena
        MAX_ITER = 100000 #numero maximo de iteraciones
        #it  = contador de iteraciones para forzar a que pare
        it = 0
        while(current_state != self.accept and current_state != self.reject):
            if (it > MAX_ITER): 
                return " No termina"
            else:

                #print "Testing " + str((current_state,cinta[contador]))
              
                
                if((current_state,cinta[contador]) in self.transitions):

                    #print "Se encontro la pareja: " + str((current_state,cinta[contador]))
                    
                    val = self.transitions[(current_state,cinta[contador])]
                    current_state = val[0]
                    #print "current_state: ",current_state
                    cinta[contador] = val[1]
                    #print "Se cambio el simbolo de la cinta por: "  + str(val[1])
                    if(contador > 0 and val[2] == 'I'):
                        contador = contador -1
                        #print "La direccion del apuntador es hacia la izquierda"
                    elif( contador >=0 and val[2] == 'D'):
                        contador = contador + 1
                        #print "La direccion del apuntador es hacia la derecha"
                    else:
                        #print "Error: elemento en la cinta no accesible"
                        return "Error: elemento en la cinta no accesible"
                    
                    #print "-----------------------"
                it = it +1
       # print "Numero de iteraciones: ",it        
        if (current_state == self.accept):
            return True
        elif(current_state == self.reject):
            return False

        else:
            return False

        
    def generateAll(self,n):
        todos  = []
        for i in range(n+1):
            listaN = list(product(self.alphabet,repeat = i))
            for j in listaN:
                todos.append(j)

        for t in range(len(todos)):
            w = ""
            todos[t] = w.join(todos[t])
        #del todos[0] # Evitando cadena vacia
        return todos
        
    def generateLanguage(self,n):
        final = self.generateAll(n)
        accepted = []
        for s in final:
            if(self.test(s) == True):
                accepted.append(s)
        return accepted
                        
                

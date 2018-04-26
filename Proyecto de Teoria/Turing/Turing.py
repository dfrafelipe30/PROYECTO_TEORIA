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
        current_state =  self.start
        print "current_state: ",current_state
        cinta = list(word+"B")
        
        contador = 0
        

        while(current_state != self.accept and current_state != self.reject):

            print "Testing " + str((current_state,cinta[contador]))
          
            
            if((current_state,cinta[contador]) in self.transitions):

                print "Se encontro la pareja: " + str((current_state,cinta[contador]))
                
                val = self.transitions[(current_state,cinta[contador])]
                current_state = val[0]
                print "current_state: ",current_state
                cinta[contador] = val[1]
                print "El valor en la cinta es: "  + str(val[1])
                if(contador > 0 and val[2] == 'I'):
                    contador = contador -1
                    print "La direccion del apuntador es hacia la izquierda"
                elif( contador >=0 and val[2] == 'D'):
                    contador = contador + 1
                    print "La direccion del apuntador es hacia la derecha"
                else:
                    print "Error: elemento en la cinta no accesible"
                    return
                
                print "-----------------------"
        if (current_state == self.accept):
            return True
        elif(current_state == self.reject):
            return False

        else:
            return False

                        
                

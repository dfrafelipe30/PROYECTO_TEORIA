import logging

class NDFA(object):
    def __init__(self,states,alphabet,transitions,start,accepts):
        assert start in states ,\
               'start state must be a valid state'
        assert set(accepts).issubset(set(set(states))),\
               'accept states must be a subset of states.'
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.accepts = accepts

    def test(self,word):
        current_state = self.start
        logging.info('testing word "%s" .. ' %word)
        logging.debug('initial state: %s' %current_state)
        for symbol in word:
            logging.debug('current symbol:%s' %symbol)
            assert symbol in self.alphabet,\
                   'symbol "%s" must be in alphabet.' %symbol
            for k in self.transitions :
               for qi in self.transitions[k]:
                   nuevo_estado = []
                   if ((qi,symbol) in self.transitions):
                       nuevo_estado = nuevo_estado + self.transitions[(qi,symbol)]
            current_state = nuevo_estado
        for i in current_state :
            if ( i in self.accepts ):
                return True
        return False

    def NuevosEstados():
        estado = [self.start]
        registro = []
        aux = ['q0']
        while (aux not in registro):
        
                    
                    
                    
                    
                        
                        
                        
                       
  
    
                        

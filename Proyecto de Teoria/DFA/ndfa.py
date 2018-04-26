import logging
from itertools import product

class DFA(object):

    def __init__(self, states, alphabet, transitions, start, accepts):
        assert start in states, \
                'Start state must be a valid state.'
        assert set(accepts).issubset(set(states)), \
                'Accept states must be a subset of states.'
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.accepts = accepts

    def test(self, word):
        current_state = self.start
        logging.info('Testing word "%s"...' % word)
        logging.debug('Initial state: %s' % current_state)
        for symbol in word:
            logging.debug('Current symbol: %s' % symbol)
            assert symbol in self.alphabet, \
                    'Symbol "%s" must be in alphabet.' % symbol



            current_state = self.transitions[(current_state, symbol)]
            assert current_state in self.states, \
                    'Current state must be a valid state.' 
            logging.debug('New state: %s' % current_state)
        logging.debug('Final state: %s' % current_state)
        logging.info('Accepted: %s\n' % (current_state in self.accepts))
        return current_state in self.accepts

    def generateAll(self,n):
        candidatos_posibles = list(self.alphabet)
        Lal = len(self.alphabet)
        for i in range(Lal,n+1):
            miListaProv = list(product(self.alphabet, repeat = i))
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
        todos = self.generateAll(n)
        accepted = []
        for s in todos:
            if(self.test(s) == True):
                accepted.append(s)
        return accepted
    


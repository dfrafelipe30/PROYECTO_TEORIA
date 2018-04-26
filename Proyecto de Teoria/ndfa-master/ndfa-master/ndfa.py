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
    
    #Aqui se crean las cadenas de longitud n
    def combin_long_n(miAlfabeto,n):
        candidatos_posibles = list(miAlfabeto)
        for i in range(2,n+1):
            miListaProv = list(product(miAlfabeto, repeat = i))
            for j in range(len(miListaProv)):
                candidatos_posibles.append(miListaProv[j])
        return candidatos_posibles

    #Aqui se pegan los simbolos de una cadena
    def concatSimbolos(misCandidatos):
        for i in range(len(misCandidatos)):
            w = ""
            if (type(misCandidatos[i]) == tuple):
                for k in (misCandidatos[i]):
                    w= w+k
                misCandidatos[i] = w

            
    def generateLanguage(self,n):
        k = combin_long_n(self.alphabet,n)
        concatSimbolos(k)
        aceptados = []
        for i in k :
            if (test(self,k[i]) == True ):
                aceptados.append(k[i])
        return aceptados



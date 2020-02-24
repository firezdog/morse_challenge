from morse_letters import MORSE_LETTERS

# this is called a "trie" even though in fact it functions as a binary tree.
class MorseTrie:
    def __init__(self):
        self.root = self.Node()


    class Node:
        def __init__(self):
            self.dot = None
            self.dash = None
            self.words = []
            self.morse = ''
    
    # assume 'word' is a string of uppercase letters
    def put(self, word):
        word_to_add = word.upper().strip()
        walker = self.root
        
        morse = ''
        for char in word_to_add:
            morse += MORSE_LETTERS[char]

        for tic in morse:
            if tic == '.':
                if not walker.dot:
                    walker.dot = self.Node()
                    walker.dot.morse = walker.morse + '.'
                walker = walker.dot
            elif tic == '-':
                if not walker.dash:
                    walker.dash = self.Node()
                    walker.dash.morse = walker.morse + '-'
                walker = walker.dash
        walker.words.append(word_to_add)
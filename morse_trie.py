# this is called a "trie" even though in fact it functions as a binary tree.
class MorseTrie:
    def __init__(self):
        self.dot = None
        self.dash = None
        self.words = []
        self.morse = ''

morse_letters = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}
root = MorseTrie()

# assume 'word' is a string of uppercase letters
def build_word_trie(word):
    walker = root
    for char in word:
        translation = morse_letters[char]
        for tic in translation:
            if tic == '.':
                if walker.dot:
                    pass
                else:
                    walker.dot = MorseTrie()
                    walker.dot.morse = walker.morse + '.'
                walker = walker.dot
            elif tic == '-':
                if walker.dash:
                    pass
                else:
                    walker.dash = MorseTrie()
                    walker.dash.morse = walker.morse + '-'
                walker = walker.dash
    walker.words.append(word)

with open('top_words.txt', 'r') as popular_words:
    for word in popular_words:
        word = word.upper().strip()
        build_word_trie(word)

def translate_morse(morse):
    walker = root
    for tick in morse:
        if tick == '-':
            walker = walker.dash
        if tick == '.':
            walker = walker.dot
        if walker is None:
            print('translation not found')
            return
    if not walker.words:
        print('translation not found')
    else:
        print(walker.words)

translate_morse('......-...-..---')
translate_morse('...---...-..')
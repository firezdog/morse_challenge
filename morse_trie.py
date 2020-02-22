# this is called a "trie" even though in fact it functions as a binary tree.
class MorseTrie:
    dot = None
    dash = None
    message = None
    morse = ''

morse_letters = {
    'A': '.-',
    'B': '-...',
    'c': '-.-.',
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

# assume 'word' is a string of uppercase letters
def build_word_trie(word):
    root = MorseTrie()
    for char in word:
        translation = morse_letters[char]
        for tic in translation:
            walker = root
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
    return root

sample = build_word_trie('DOG')
print('done')
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

# make a pass through the morse, putting all possibilities for first word into an array of arrays, where the first entry of the sub-array is the remaining string and the rest if it acts as a stack for words
def parse_morse(morse):
    possible_interpretations = []
    finished_interpretations = []
    possible_interpretations.append([morse])
    while len(possible_interpretations):
        walker = root
        interpretation_to_process = possible_interpretations.pop(0)
        morse_to_process = interpretation_to_process.pop(0)
        for index, tick in enumerate(morse_to_process):
            if tick == '-':
                walker = walker.dash
                if walker and len(walker.words):
                    for word in walker.words:
                        interpretation = list(interpretation_to_process)
                        interpretation.append(word)
                        interpretation.insert(0, morse_to_process[index + 1:])
                        if not morse_to_process[index + 1:]:
                            finished_interpretations.append(interpretation)
                        else:
                            possible_interpretations.append(interpretation)
            if tick == '.':
                walker = walker.dot
                if walker and len(walker.words):
                    for word in walker.words:
                        interpretation = list(interpretation_to_process)
                        interpretation.append(word)
                        interpretation.insert(0, morse_to_process[index + 1:])
                        if not morse_to_process[index + 1:]:
                            finished_interpretations.append(interpretation)
                        else:
                            possible_interpretations.append(interpretation)
            if walker is None:
                break
        if (finished_interpretations):
            print(finished_interpretations)
    print(finished_interpretations)

parse_morse('......-...-..---.-----.-..-..-..')
print('done')
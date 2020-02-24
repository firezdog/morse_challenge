import nltk

from morse_trie import MorseTrie as _MorseTrie

class MorseTranslator:
    def __init__(self, dictionary):
        self.dictionary = _MorseTrie()
        self.root = self.dictionary.root
        self.possible_interpretations = []
        self.finished_interpretations = []
        try:
            with open(dictionary, 'r') as popular_words:
                for word in popular_words:
                    self.dictionary.put(word)
        except Exception as exc:
            print('Error reading dictionary file')
            raise(exc)

    # make a pass through the morse, putting all possibilities for first word into an array of arrays, where the first entry of the sub-array is the remaining string and the rest if it acts as a stack for words
    def parse_morse(self, morse):
        self.possible_interpretations = [[morse]]
        self.finished_interpretations = []
        while self.possible_interpretations:
            walker = self.root
            interpretation_to_process = self.possible_interpretations.pop(0)
            morse_to_process = interpretation_to_process.pop(0)
            for index, tick in enumerate(morse_to_process):
                if walker is None:
                    break
                if tick == '-':
                    walker = walker.dash
                if tick == '.':
                    walker = walker.dot
                self.add_interpretations(
                    walker=walker,
                    index=index,
                    interpretation=interpretation_to_process,
                    morse=morse_to_process,
                )
        return self.finished_interpretations

    def add_interpretations(
        self, 
        walker,
        index,
        interpretation, 
        morse, 
    ):
        if walker and walker.words:
            for word in walker.words:
                new_interpretation = list(interpretation)
                new_interpretation.append(word)
                if not MorseTranslator.validate_grammar(new_interpretation):
                    return

                new_interpretation.insert(0, morse[index + 1:])
                if not morse[index + 1:]:
                    if not new_interpretation in self.finished_interpretations:
                        self.finished_interpretations.append(new_interpretation)
                else:
                    if not new_interpretation in self.possible_interpretations:
                        self.possible_interpretations.append(new_interpretation)

    @staticmethod
    def validate_grammar(interpretation):
        # keep small interpretations
        if len(interpretation) < 4:
            return True
        
        # length of words in an english sentence is on average 5
        sum = 0
        for word in interpretation:
            sum += len(word)
        if sum / len(interpretation) < 4:
            return False
        
        # make sure interpretations start with a noun (very basic)
        parsed_tokens = nltk.pos_tag(interpretation)
        if parsed_tokens[0][1] != 'NNP':
            return False 

        return True

    def translate_morse(self, morse):
        walker = self.root
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
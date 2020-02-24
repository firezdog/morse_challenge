from sys import argv
from re import match, compile

from morse_translator import MorseTranslator

dictionary = argv[1]
morse_input = ''

while not morse_input:
    morse_input = input('Input a string of morse code ("." or "-") with no spaces\n').strip()
    if not match(compile(r'[.-]+'), morse_input):
        morse_input = ''

morse_translator = MorseTranslator(dictionary)

print(f'results for {morse_input}')
for index, interpretation in enumerate(morse_translator.parse_morse(morse_input)):
    interpretation.pop(0)
    print(f'{index}: {" ".join(interpretation).lower()}')
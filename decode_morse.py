# Fonction pour décoder le code Morse

MORSE_DICT = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', 
        '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', 
        '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!', '-....-': '-', '.----.': "'", '-.-.-.': ';', '-..-.': '/',
        '.-.-.': '+', '-...-': '=', '.-..-.': '"', '---...': ':', '-.-.-': '.', '.-...': '&', '...-..-': '$'
    }

def decode_morse(morse_code):
    morse_words = morse_code.split("   ")  # Séparer les mots par des espaces triples
    decoded_message = []
    
    for word in morse_words:
        morse_letters = word.split()  # Séparer les lettres par un seul espace
        decoded_word = ''.join(MORSE_DICT.get(letter, '') for letter in morse_letters)
        decoded_message.append(decoded_word)
    
    return ''.join(decoded_message)
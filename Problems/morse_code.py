MORSE_CODE = {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5', '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N', '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';', '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'}

def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    output = ""
    
    char = '...'
    h_char = MORSE_CODE[char]
    
    return h_char

result = decodeMorse('.... . -.--   .--- ..- -.. .')

print(result)
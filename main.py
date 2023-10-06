import re

def main():
    code = read_text_file()
    print(code)
    analyze_code(code)

# Function to import the input.txt file
def read_text_file():
    file_path = "./File/Input.txt"
    code_builder = []

    try:
        # Open the file
        with open(file_path, "r") as file_reader:
            lines = file_reader.readlines()
            code_builder = "".join(lines)

    except IOError as e:
        print(e)

    # Return the content read from the file as a string
    return code_builder

def analyze_code(code):
    # Setup keywords
    keyword = "while|if|else|return|break|continue|int|float|void|for"

    letter = "[A-Za-z]"
    digit = "[0-9]"
    underscore = "_"
    identifier = letter + "(" + letter + "|" + digit + "|" + underscore + ")*"

    digits = digit + "(" + digit + ")*"
    optional_fraction = "(\\." + digits + ")?"
    optional_exponent = "(.)?(E[+|-]?" + digits + ")?"
    num = "^" + digits + optional_fraction + optional_exponent + "$"

    # Create regular expressions for different types of lexemes to be analyzed
    keyword_pattern = re.compile(r'\b(' + keyword + r')\b')
    identifier_pattern = re.compile(r'\b' + identifier + r'\b')
    num_pattern = re.compile(r'\b' + num + r'\b')
    operator_pattern = re.compile(r'[-+*/=(){}<>;]')
    error_pattern = re.compile(r'[.^a-zA-Z_0-9\-*/=(){}<>;]')

    # Create a list to store lexemes
    lexemes = []

    # Tokenize the code
    code = re.sub(r'\s', ' ', code)
    code = re.sub(r'(\b|\s*)([-+*/=(){}<>;])(\b|\s*)', r'\1 \2 \3', code)
    tokens = code.split()

    for token in tokens:
        if keyword_pattern.match(token):
            lexemes.append(f'keyword : {token}')
        elif identifier_pattern.match(token):
            lexemes.append(f'identifier : {token}')
        elif num_pattern.match(token):
            lexemes.append(f'num : {token}')
        elif operator_pattern.match(token):
            lexemes.append(f'{token} : {token}')
        elif error_pattern.search(token):
            lexemes.append(f'Error : {token}')

    # Print the result
    print("Class : Lexeme")
    for lexeme in lexemes:
        print(lexeme)

if __name__ == "__main__":
    main()

import re
# Hàm để đọc nội dung từ tệp tin.

def read_text_file():
    file_path = "./File/Input.txt"
    code_builder = []

    try:
        with open(file_path, "r") as file_reader:
            lines = file_reader.readlines()
            code_builder = "".join(lines)

    except IOError as e:
        print(e)
    return code_builder

def analyze_code(code):
    # Tạo các biểu thức chính quy để nhận dạng từng loại lexeme cần phân tích.
    keyword = "while|if|else|return|break|continue|int|float|void|for"
    letter = "[A-Za-z]"
    digit = "[0-9]"
    underscore = "_"
    identifier = letter + "(" + letter + "|" + digit + "|" + underscore + ")*"

    digits = digit + "(" + digit + ")*"
    optional_fraction = "(\\." + digits + ")?"
    optional_exponent = "(.)?(E[+|-]?" + digits + ")?"
    num = "^" + digits + optional_fraction + optional_exponent + "$"

    # Tạo các biểu thức chính quy để nhận dạng từng loại lexeme cần phân tích.
    keyword_pattern = re.compile(r'\b(' + keyword + r')\b')
    identifier_pattern = re.compile(r'\b' + identifier + r'\b')
    num_pattern = re.compile(r'\b' + num + r'\b')
    operator_pattern = re.compile(r'[-+*/=(){}<>;]')
    error_pattern = re.compile(r'[.^a-zA-Z_0-9\-*/=(){}<>;]')

    lexemes = []

    code = re.sub(r'\s', ' ', code) # Thay thế khoảng trắng và ký tự trắng bằng một dấu cách đơn (' ').
    code = re.sub(r'(\b|\s*)([-+*/=(){}<>;])(\b|\s*)', r'\1 \2 \3', code) # Thêm dấu cách xung quanh các toán tử.

    tokens = code.split()

    for token in tokens:
        if keyword_pattern.match(token):
            lexemes.append(f'keyword : {token}') # Nếu token là từ khóa, thêm vào danh sách lexemes với thông tin "keyword :".

        elif identifier_pattern.match(token):
            lexemes.append(f'identifier : {token}')

        elif num_pattern.match(token):
            lexemes.append(f'num : {token}')

        elif operator_pattern.match(token):
            lexemes.append(f'{token} : {token}')

        elif error_pattern.search(token):
            lexemes.append(f'Error : {token}')  # Nếu token không khớp với các biểu thức chính quy trên, coi là lỗi.
    print("Class : Lexeme")
    for lexeme in lexemes:
        print(lexeme)

def main():
    code = read_text_file()
    analyze_code(code)

if __name__ == "__main__":
    main()

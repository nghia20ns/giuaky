import re  # Import thư viện 're' (regular expressions) để sử dụng cho tìm kiếm và phân tích cú pháp (lexical analysis).

# Hàm để đọc nội dung từ tệp tin.
def read_text_file():
    file_path = "./File/Input.txt"  # Đường dẫn tới tệp tin cần đọc.
    code_builder = []  # Danh sách để lưu trữ nội dung từ tệp tin.

    try:
        # Mở tệp tin ở chế độ đọc ("r") và sử dụng 'with' để đảm bảo tệp tin sẽ được đóng đúng cách sau khi hoàn thành.
        with open(file_path, "r") as file_reader:
            lines = file_reader.readlines()  # Đọc tất cả các dòng từ tệp tin.
            code_builder = "".join(lines)  # Nối các dòng thành một chuỗi văn bản và lưu vào biến 'code_builder'.

    except IOError as e:
        print(e)  # In ra thông báo lỗi nếu có lỗi xảy ra trong quá trình đọc tệp tin.

    return code_builder  # Trả về nội dung đọc từ tệp tin dưới dạng chuỗi văn bản.

# Hàm để phân tích cú pháp nội dung mã.
def analyze_code(code):
    keyword = "while|if|else|return|break|continue|int|float|void|for"  # Danh sách các từ khóa.

    letter = "[A-Za-z]"
    digit = "[0-9]"
    underscore = "_"
    identifier = letter + "(" + letter + "|" + digit + "|" + underscore + ")*"  # Biểu thức chính quy cho từ ngữ (identifier).

    digits = digit + "(" + digit + ")*"
    optional_fraction = "(\\." + digits + ")?"
    optional_exponent = "(.)?(E[+|-]?" + digits + ")?"
    num = "^" + digits + optional_fraction + optional_exponent + "$"  # Biểu thức chính quy cho số (num).

    # Tạo các biểu thức chính quy để nhận dạng từng loại lexeme cần phân tích.
    keyword_pattern = re.compile(r'\b(' + keyword + r')\b')
    identifier_pattern = re.compile(r'\b' + identifier + r'\b')
    num_pattern = re.compile(r'\b' + num + r'\b')
    operator_pattern = re.compile(r'[-+*/=(){}<>;]')
    error_pattern = re.compile(r'[.^a-zA-Z_0-9\-*/=(){}<>;]')

    lexemes = []  # Danh sách để lưu trữ các lexeme.

    code = re.sub(r'\s', ' ', code)  # Thay thế khoảng trắng và ký tự trắng bằng một dấu cách đơn (' ').
    code = re.sub(r'(\b|\s*)([-+*/=(){}<>;])(\b|\s*)', r'\1 \2 \3', code)  # Thêm dấu cách xung quanh các toán tử.

    tokens = code.split()  # Tách mã thành các token dựa trên dấu cách.

    for token in tokens:
        if keyword_pattern.match(token):
            lexemes.append(f'keyword : {token}')  # Nếu token là từ khóa, thêm vào danh sách lexemes với thông tin "keyword :".

        elif identifier_pattern.match(token):
            lexemes.append(f'identifier : {token}')  # Nếu token là từ ngữ (identifier), thêm vào danh sách lexemes với thông tin "identifier :".

        elif num_pattern.match(token):
            lexemes.append(f'num : {token}')  # Nếu token là số (num), thêm vào danh sách lexemes với thông tin "num :".

        elif operator_pattern.match(token):
            lexemes.append(f'{token} : {token}')  # Nếu token là toán tử, thêm vào danh sách lexemes với thông tin "toán tử : toán tử".

        elif error_pattern.search(token):
            lexemes.append(f'Error : {token}')  # Nếu token không khớp với các biểu thức chính quy trên, coi là lỗi.

    print("Class : Lexeme")  # In tiêu đề cột.
    for lexeme in lexemes:
        print(lexeme)  # In danh sách các lexeme đã tìm thấy.

def main():
    code = read_text_file()  # Đọc nội dung từ tệp tin và lưu vào biến 'code'.
    print(code)  # In nội dung đã đọc từ tệp tin.
    analyze_code(code)  # Gọi hàm 'analyze_code' để phân tích cú pháp nội dung mã.

if __name__ == "__main__":
    main()  # Gọi hàm chính khi chương trình được chạy.


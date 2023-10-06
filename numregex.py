import re

def main():
    code = read_text_file()
    print(code)
    analyze_code(code)

# Hàm import file input.txt
def read_text_file():
    file_path = "./File/Input.txt"
    code_builder = []

    try:
        # Mở file
        with open(file_path, "r") as file_reader:
            lines = file_reader.readlines()
            code_builder = "".join(lines)

    except IOError as e:
        print(e)

    # Trả về nội dung đọc được từ file dưới dạng chuỗi
    return code_builder

def analyze_code(code):
    pass

if __name__ == "__main__":
    main()

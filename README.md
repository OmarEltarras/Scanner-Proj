Team Members :
Name : قزر دومحم لداع نيدلا دامع
ID : 200650
Name : سارتلا دومحم زيزعلا دبع رمع
ID : 2000632
Name : نامثع هيطع دمحا دمحم
ID : 2000682
Python Code Scanner
This Python project is a simple lexical analyzer (or tokenizer) that scans Python code input
and outputs individual tokens. Each token is classified according to its type, such as
keywords, identifiers, numbers, strings, operators, comments, and whitespace. This tool can
help with understanding how a Python program is structured by breaking it down into these
basic elements.
Features
Tokenizes Python Code: The scanner takes C Programming code as input and identifies
all tokens within it.
Token Types Supported
:
Keywords: Recognizes Python keywords (e.g., def , return , if , else ).
Identifiers: Recognizes variable and function names.
Numbers: Detects integer values.
Strings: Detects strings enclosed in single or double quotes.
Operators: Recognizes standard Python operators (e.g., + , - , * , / , == , != ).
Comments: Identifies comments beginning with # .
Whitespace: Skips whitespace but keeps it for structural integrity.
Regex-Based Scanning: Uses regular expressions to define and match each token type.
How It Works
The program utilizes Python's re (regular expression) module to define token types using
patterns. It then scans the input code and matches each pattern to identify token types,
ignoring whitespace for readability.
Example
c_code = """
// A simple addition
int add(int a, int b) {
return a + b;
}
"""
Expected Output
('COMMENT', '# This is a comment')
('KEYWORD', 'def')
('IDENTIFIER', 'add')
('SPECIAL_CHAR', '(')
('IDENTIFIER', 'x')
('SPECIAL_CHAR', ',')
('IDENTIFIER', 'y')
('SPECIAL_CHAR', ')')
('OPERATOR', ':')
('KEYWORD', 'return')
('IDENTIFIER', 'x')
('OPERATOR', '+')
('IDENTIFIER', 'y')
Usage
1. Clone the Repository:
git clone https://github.com/your-username/python-code-scanner.git
cd python-code-scanner
2. Run the Program:
Run the code in the terminal:
python scanner.py

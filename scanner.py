import re

TOKEN_TYPES = {
    'COMMENT': r'(#.*?$)',
    'KEYWORD': r'\b(def|return|if|else|elif|while|for|in|break|continue|import|from|as|class|try|except|finally|with|lambda|True|False|None)\b',
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'NUMBER': r'\b\d+\b',
    'STRING': r'(\".*?\"|\'.*?\')',
    'OPERATOR': r'(\+|\-|\*|\/|%|==|!=|<=|>=|<|>|=)',
    'WHITESPACE': r'\s+',
}

TOKEN_REGEX = '|'.join(f'(?P<{key}>{pattern})' for key, pattern in TOKEN_TYPES.items())

def tokenize(code):
    tokens = []
    for match in re.finditer(TOKEN_REGEX, code, re.MULTILINE):
        kind = match.lastgroup
        value = match.group()
        if kind != 'WHITESPACE':  
            tokens.append((kind, value))
    return tokens

if __name__ == "__main__":
    code = input("please enter code to scan it:\n")
    
    tokens = tokenize(code)
    for token in tokens:
        print(token)
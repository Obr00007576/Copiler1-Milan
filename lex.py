from ply import lex

tokens = (
    'IDENTIFIER', 
    'NUMBER_INT',
    'NUMBER_FLOAT', 
    'BEGIN', 
    'END', 
    'IF', 
    'THEN', 
    'ELSE', 
    'FI', 
    'WHILE', 
    'DO', 
    'OD', 
    'WRITE', 
    'READ', 
    'ASSIGN', 
    'ADDOP', 
    'MULOP', 
    'CMP', 
    'LPAREN', 
    'RPAREN', 
    'SEMICOLON',
    'TYPE',
    'COMMA'
)

reserved = {
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'fi': 'FI',
    'while': 'WHILE',
    'do': 'DO',
    'od': 'OD',
    'write': 'WRITE',
    'read': 'READ',
    'float': 'TYPE',
    'int': 'TYPE'
}

t_ignore = ' \t'
t_ASSIGN = r':='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','

def t_MULOP(t):
    r'\*|/'
    if t.value == '*':
        t.value = 'A_MULTIPLY'
    elif t.value == '/':
        t.value = 'A_DIVIDE'
    return t

def t_ADDOP(t):
    r'\+|-'
    if t.value == '+':
        t.value = 'A_PLUS'
    elif t.value == '-':
        t.value = 'A_MINUS'
    return t

def t_CMP(t):
    r'=|(!=)|(<=)|<|>=|>'
    if t.value == '=':
        t.value = 'C_EQ'
    elif t.value == '!=':
        t.value = 'C_NE'
    elif t.value == '<=':
        t.value = 'C_LE'
    elif t.value == '<':
        t.value = 'C_LT'
    elif t.value == '>=':
        t.value = 'C_GE'
    elif t.value == '>':
        t.value = 'C_GT'
    return t

def t_IDENTIFIER(t):
    r'[A-Za-z_][\w_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
        return t
    return t

def t_NUMBER_FLOAT(t):
    r'\d+\.\d*'
    t.value = float(t.value)    
    return t

def t_NUMBER_INT(t):
    r'\d+'
    t.value = int(t.value)    
    return t


def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

lexer = lex.lex()
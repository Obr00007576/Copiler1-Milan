from ply import yacc
from lex import lexer,tokens
var_tab = {}
var_num = 0
const_tab = {}
const_num = 0
mem_tab = {}
P_CODE = []

def p_program(p):
    'program : BEGIN statementList END'
    global P_CODE
    P_CODE.append("STOP")
    pass

def p_empty(p):
    'empty :'
    pass

def p_statementList(p):
    '''statementList : statement SEMICOLON statementList
                     | empty
    '''
    if len(p)==4:
        p[0]=p[1]+p[3]
    else:
        p[0]=0

def p_statement(p):
    '''statement : IDENTIFIER ASSIGN expression
                 | IF relation THEN statementList FI
                 | IF relation THEN statementList ELSE statementList FI
                 | WHILE relation DO statementList OD
                 | WRITE LPAREN expression RPAREN
    '''
    global mem_tab,P_CODE
    p[0]=0
    if p[2]==':=':
        mem_address = mem_tab[p[1]][1]
        P_CODE.append(f"STORE {mem_address}")
        p[0]=p[3]+1
    if p[1]=='write':
        P_CODE.append('OUT')
        p[0]=p[3]+1
    if p[1]=='if':
        print(p[2])
        print(p[4])

def p_expression(p):
    '''expression : term
                  | expression ADDOP term
    '''
    if len(p)==4:
        if p[2]=='A_PLUS':
            P_CODE.append('ADD')
        elif p[2]=='A_MINUS':
            P_CODE.append('SUB')
        p[0]=p[1]+p[3]+1
    else:
        p[0]=p[1]

def p_term(p):
    '''term : factor
            | factor MULOP factor
    '''
    global P_CODE
    if len(p)==4:
        if p[2]=='A_MULTIPLY':
            P_CODE.append('MULT')
        elif p[2]=='A_DIVIDE':
            P_CODE.append('DIV')
        p[0]=p[1]+p[3]+1
    else:
        p[0]=p[1]

def p_factor(p):
    '''factor : IDENTIFIER
              | NUMBER
              | READ
              | LPAREN expression RPAREN
    '''
    global mem_tab,P_CODE
    if len(p)==2:
        if p[1]=='read':
            P_CODE.append('INPUT')
        else:
            mem_address = mem_tab[p[1]][1]
            P_CODE.append(f"LOAD {mem_address}")
        p[0]=1
    else:
        p[0]=p[2]

def p_relation(p):
    'relation : expression CMP expression'
    global mem_tab,P_CODE
    P_CODE.append('CMP')
    p[0]=p[1]+p[3]+1

parser = yacc.yacc(debug=True)

if __name__=='__main__':
    data = '''begin
        x := read*3;
        y := read;
        a := (34+34)*13;
        z := (x-y+a)/a;
        if x <= y then
            write(x);
            write(y);
        fi;
    end
    '''
    lexer.input(data)
    for tok in lexer:
        if tok.type=='NUMBER':
            if not tok.value in const_tab:
                const_tab[tok.value] = ('INT', const_num)
                const_num+=1
        if tok.type=='IDENTIFIER':
            if not tok.value in var_tab:
                var_tab[tok.value] = ('INT', var_num)
                var_num+=1
    for key in const_tab:
        mem_tab[key] = const_tab[key]
    for key in var_tab:
        mem_tab[key] = (var_tab[key][0], var_tab[key][1]+len(const_tab))
    print(mem_tab)
    parser.parse(data, lexer=lexer)
    print(P_CODE)
    print(['a']+['b'])
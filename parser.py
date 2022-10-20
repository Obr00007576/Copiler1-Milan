from ply import yacc
from lex import lexer,tokens
var_tab = {}
var_num = 0
const_tab = {}
const_num = 0
mem_tab = {}
P_CODE=[]

def p_program(p):
    'program : BEGIN statementList END'
    global P_CODE
    p[0]=p[2]+['STOP']
    P_CODE+=p[0]
    print(len(p[0]))

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
        p[0]=[]

def p_statement(p):
    '''statement : IDENTIFIER ASSIGN expression
                 | IF relation THEN statementList FI
                 | IF relation THEN statementList ELSE statementList FI
                 | WHILE relation DO statementList OD
                 | WRITE LPAREN expression RPAREN
    '''
    global mem_tab
    p[0]=[]
    if p[2]==':=':
        mem_address = mem_tab[p[1]][1]
        p[0]=p[3]+[f"STORE {mem_address}"]
    if p[1]=='write':
        p[0]=p[3]+['OUT']
    if p[1]=='if':
        if len(p)==6:
            p[0]=p[2]+[f'JMP_NO {len(p[4])+1}']+p[4]
        elif len(p)==8:
            p[0]=p[2]+[f'JMP_NO {len(p[4])+2}']+p[4]+[f'JMP {len(p[6])+1}']+p[6]
    if p[1]=='while':
        p[0]=p[2]+[f"JMP_NO {len(p[4])+2}"]+p[4]+[f"JMP {-1-len(p[2])-len(p[4])}"]

def p_expression(p):
    '''expression : term
                  | expression ADDOP term
    '''
    if len(p)==4:
        if p[2]=='A_PLUS':
            p[0]=p[1]+p[3]+['ADD']
        elif p[2]=='A_MINUS':
            p[0]=p[1]+p[3]+['SUB']
    else:
        p[0]=p[1]

def p_term(p):
    '''term : factor
            | factor MULOP factor
    '''
    if len(p)==4:
        if p[2]=='A_MULTIPLY':
            p[0]=p[1]+p[3]+['MULT']
        elif p[2]=='A_DIVIDE':
            p[0]=p[1]+p[3]+['DIV']
    else:
        p[0]=p[1]

def p_factor(p):
    '''factor : IDENTIFIER
              | NUMBER
              | READ
              | LPAREN expression RPAREN
    '''
    global mem_tab
    if len(p)==2:
        if p[1]=='read':
            p[0]=['INPUT']
        else:
            mem_address = mem_tab[p[1]][1]
            p[0]=[f"LOAD {mem_address}"]
    else:
        p[0]=p[2]

def p_relation(p):
    'relation : expression CMP expression'
    if p[2]=='C_EQ':
        p[0]=p[1]+p[3]+['CMP 0']
    elif p[2]=='C_LT':
        p[0]=p[1]+p[3]+['CMP 1']
    elif p[2]=='C_LE':
        p[0]=p[1]+p[3]+['CMP 2']
    elif p[2]=='C_GT':
        p[0]=p[1]+p[3]+['CMP 3']
    elif p[2]=='C_GE':
        p[0]=p[1]+p[3]+['CMP 4']

parser = yacc.yacc(debug=True)

if __name__=='__main__':
    data = '''begin
        x := 3;
        y := 4;
        if x <= y then
            write(x);
            write(y);
            while x<5 do
                x:=x+1;
            od;
        else
            write(y);
            write(x);
            if x=3 then
                write(3);
                x:=x+3;
                write((x*x)/4);
            else
                write(4);
                x:=x+4;
                write(x);
            fi;
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
    i=0
    for p in P_CODE:
        print(f"{i}: {p}")
        i+=1
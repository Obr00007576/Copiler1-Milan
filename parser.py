from ply import yacc
from lex import lexer,tokens
mem_tab = {}
P_CODE=[]

def p_program(p):
    'program : BEGIN statementList END'
    global P_CODE
    p[0]=p[2]+['STOP']
    P_CODE+=p[0]

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
                 | IDENTIFIERS ASSIGN expression
                 | TYPE IDENTIFIER ASSIGN expression
                 | TYPE IDENTIFIERS ASSIGN expression
                 | IF relation THEN statementList FI
                 | IF relation THEN statementList ELSE statementList FI
                 | WHILE relation DO statementList OD
                 | WRITE LPAREN expression RPAREN
    '''
    global mem_tab
    p[0]=[]
    if p[2]==':=':
        if type(p[1]) is str:
            if p[3][-1]=='i':
                mem_tab[p[1]][0]='INT'
            elif p[3][-1]=='f':
                mem_tab[p[1]][0]='FLOAT'
            mem_address = mem_tab[p[1]][1]
            p[0]=p[3][:-1]+[f"STORE {mem_address}"]
        else:
            p[0]=p[3][:-1]
            for n in range(len(p[1])):
                vn = p[1][n]
                if p[3][-1]=='i':
                    mem_tab[vn][0]='INT'
                elif p[3][-1]=='f':
                    mem_tab[vn][0]='FLOAT'
                mem_address = mem_tab[vn][1]
                if n<len(p[1])-1:
                    p[0]+=[f"STORE {mem_address}", f"LOAD {mem_address}"]
                else:
                    p[0]+=[f"STORE {mem_address}"]
    if p[3]==':=':
        if type(p[2]) is str:
            mem_address = mem_tab[p[2]][1]
            mem_tab[p[2]][0]=p[1].upper()
            if p[1]=='int' and p[4][-1]=='i':
                p[0]=p[4][:-1]+[f"STORE {mem_address}"]
            elif p[1]=='float' and p[4][-1]=='i':
                p[0]=p[4][:-1]+['ITOF']+[f"STORE {mem_address}"]
            elif p[1]=='int' and p[4][-1]=='f':
                p[0]=p[4][:-1]+['FTOI']+[f"STORE {mem_address}"]
            elif p[1]=='float' and p[4][-1]=='f':
                p[0]=p[4][:-1]+[f"STORE {mem_address}"]
        else:
            mem_address = mem_tab[p[2][0]][1]
            mem_tab[p[2][0]][0]=p[1].upper()
            if p[1]=='int' and p[4][-1]=='i':
                p[0]=p[4][:-1]+[f"STORE {mem_address}"]
            elif p[1]=='float' and p[4][-1]=='i':
                p[0]=p[4][:-1]+['ITOF']+[f"STORE {mem_address}"]
            elif p[1]=='int' and p[4][-1]=='f':
                p[0]=p[4][:-1]+['FTOI']+[f"STORE {mem_address}"]
            elif p[1]=='float' and p[4][-1]=='f':
                p[0]=p[4][:-1]+[f"STORE {mem_address}"]
            p[0]+=[f"LOAD {mem_address}"]
            for n in range(1, len(p[2])):
                vn = p[2][n]
                mem_address = mem_tab[vn][1]
                mem_tab[vn][0]=p[1].upper()
                if n<len(p[2])-1:
                    p[0] += [f"STORE {mem_address}", f"LOAD {mem_address}"]
                else:
                    p[0] += [f"STORE {mem_address}"]
    if p[1]=='write':
        p[0]=p[3][:-1]+['OUT']
    if p[1]=='if':
        if len(p)==6:
            p[0]=p[2]+[f'JMP_NO {len(p[4])+1}']+p[4]
        elif len(p)==8:
            p[0]=p[2]+[f'JMP_NO {len(p[4])+2}']+p[4]+[f'JMP {len(p[6])+1}']+p[6]
    if p[1]=='while':
        p[0]=p[2]+[f"JMP_NO {len(p[4])+2}"]+p[4]+[f"JMP {-1-len(p[2])-len(p[4])}"]

def p_identifiers(p):
    '''IDENTIFIERS : IDENTIFIER COMMA IDENTIFIERS
                   | IDENTIFIER
    '''
    if len(p)==4:
        p[0]=[p[1]]+p[3]
    else:
        p[0]=[p[1]]
def p_expression(p):
    '''expression : term
                  | expression ADDOP term
    '''
    if len(p)==4:
        if p[2]=='A_PLUS':
            if p[1][-1]=='f' and p[3][-1]=='f':
                p[0]=p[1][:-1]+p[3][:-1]+['ADD','f']
            elif p[1][-1]=='i' and p[3][-1]=='i':
                p[0]=p[1][:-1]+p[3][:-1]+['ADD','i']
            elif p[1][-1]=='f' and p[3][-1]=='i':
                p[0]=p[1][:-1]+p[3][:-1]+['ITOF']+['ADD','f']
            elif p[1][-1]=='i' and p[3][-1]=='f':
                p[0]=p[1][:-1]+['ITOF']+p[3][:-1]+['ADD','f']
        elif p[2]=='A_MINUS':
            if p[1][-1]=='f' and p[3][-1]=='f':
                p[0]=p[1][:-1]+p[3][:-1]+['SUB','f']
            elif p[1][-1]=='i' and p[3][-1]=='i':
                p[0]=p[1][:-1]+p[3][:-1]+['SUB','i']
            elif p[1][-1]=='f' and p[3][-1]=='i':
                p[0]=p[1][:-1]+p[3][:-1]+['ITOF']+['SUB','f']
            elif p[1][-1]=='i' and p[3][-1]=='f':
                p[0]=p[1][:-1]+['ITOF']+p[3][:-1]+['SUB','f']
    else:
        p[0]=p[1]

def p_term(p):
    '''term : factor
            | factor MULOP factor
    '''
    if len(p)==4:
        if p[2]=='A_MULTIPLY':
            if p[1][-1]=='f' and p[3][-1]=='f':
                p[0]=p[1][:-1]+p[3][:-1]+['MULT','f']
            elif p[1][-1]=='i' and p[3][-1]=='i':
                p[0]=p[1][:-1]+p[3][:-1]+['MULT','i']
            elif p[1][-1]=='f' and p[3][-1]=='i':
                p[0]=p[1][:-1]+p[3][:-1]+['ITOF']+['MULT','f']
            elif p[1][-1]=='i' and p[3][-1]=='f':
                p[0]=p[1][:-1]+['ITOF']+p[3][:-1]+['MULT','f']
        elif p[2]=='A_DIVIDE':
            if p[1][-1]=='f' and p[3][-1]=='f':
                p[0]=p[1][:-1]+p[3][:-1]+['DIV','f']
            elif p[1][-1]=='i' and p[3][-1]=='i':
                p[0]=p[1][:-1]+p[3][:-1]+['DIV','i']
            elif p[1][-1]=='f' and p[3][-1]=='i':
                p[0]=p[1][:-1]+p[3][:-1]+['ITOF']+['DIV','f']
            elif p[1][-1]=='i' and p[3][-1]=='f':
                p[0]=p[1][:-1]+['ITOF']+p[3][:-1]+['DIV','f']
    else:
        p[0]=p[1]

def p_factor(p):
    '''factor : IDENTIFIER
              | LPAREN TYPE RPAREN IDENTIFIER
              | NUMBER_INT
              | NUMBER_FLOAT
              | READ
              | LPAREN expression RPAREN
              | LPAREN TYPE RPAREN LPAREN expression RPAREN
    '''
    global mem_tab
    if len(p)==2:
        if p[1]=='read':
            p[0]=['INPUT']
        else:
            mem_address = mem_tab[p[1]][1]
            if type(p[1]) is int:
                p[0]=[f"LOAD {mem_address}"]+['i']
            elif type(p[1]) is float:
                p[0]=[f"LOAD {mem_address}"]+['f']
            else:
                if mem_tab[p[1]][0]=='INT':
                    p[0]=[f"LOAD {mem_address}"]+['i']
                elif mem_tab[p[1]][0]=='FLOAT':
                    p[0]=[f"LOAD {mem_address}"]+['f']
    elif len(p)==4:
        p[0]=p[2]
    elif len(p)==5:
        mem_address = mem_tab[p[4]][1]
        if p[2]=='int' and  mem_tab[p[1]][0]=='INT':
            p[0]=[f"LOAD {mem_address}"]+['i']
        elif p[2]=='float' and mem_tab[p[1]][0]=='FLOAT':
            p[0]=[f"LOAD {mem_address}"]+['f']
        elif p[2]=='float' and mem_tab[p[1]][0]=='INT':
            p[0]=[f"LOAD {mem_address}"]+['ITOF', 'f']
        elif p[2]=='int' and mem_tab[p[1]][0]=='FLOAT':
            p[0]=[f"LOAD {mem_address}"]+['FTOI', 'i']
    elif len(p)==7:
        if p[2]=='int' and  p[5][-1]=='i':
            p[0]=p[5][:-1]+['i']
        elif p[2]=='float' and p[5][-1]=='f':
            p[0]=p[5][:-1]+['f']
        elif p[2]=='float' and p[5][-1]=='i':
            p[0]=p[5][:-1]+['ITOF', 'f']
        elif p[2]=='int' and p[5][-1]=='f':
            p[0]=p[5][:-1]+['FTOI', 'i']

def p_relation(p):
    'relation : expression CMP expression'
    if p[1][-1]=='i' and p[3][-1]=='i':
        p[0] = p[1][:-1]+p[3][:-1]
    elif p[1][-1]=='f' and p[3][-1]=='i':
        p[0] = p[1][:-1]+p[3][:-1]+['ITOF']
    elif p[1][-1]=='f' and p[3][-1]=='f':
        p[0] = p[1][:-1]+p[3][:-1]
    elif p[1][-1]=='i' and p[3][-1]=='f':
        p[0] = p[1][:-1]+['ITOF']+p[3][:-1]
    if p[2] == 'C_EQ':
        p[0] += ['CMP 0']
    elif p[2] == 'C_LT':
        p[0] += ['CMP 1']
    elif p[2] == 'C_LE':
        p[0] += ['CMP 2']
    elif p[2] == 'C_GT':
        p[0] += ['CMP 3']
    elif p[2] == 'C_GE':
        p[0] += ['CMP 4']
    elif p[2] == 'C_NE':
        p[0] += ['CMP 5']

parser = yacc.yacc(debug=True)

def parse(code):
    var_num = 0
    const_num = 0
    var_tab = {}
    const_tab = {}
    global P_CODE, mem_tab
    lexer.input(code)
    for tok in lexer:
        if tok.type=='NUMBER_INT':
            if not tok.value in const_tab:
                const_tab[tok.value] = ['INT', const_num]
                const_num+=1
        if tok.type=='NUMBER_FLOAT':
            if not tok.value in const_tab:
                const_tab[tok.value] = ['FLOAT', const_num]
                const_num+=1
        if tok.type=='IDENTIFIER':
            if not tok.value in var_tab:
                var_tab[tok.value] = ['INT', var_num]
                var_num+=1
    for key in const_tab:
        mem_tab[key] = const_tab[key]
    for key in var_tab:
        mem_tab[key] = [var_tab[key][0], var_tab[key][1]+len(const_tab)]
    lexer.lineno=0
    parser.parse(code, lexer=lexer)
    return (P_CODE, mem_tab)
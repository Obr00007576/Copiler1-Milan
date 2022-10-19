from ply import lex
from ply import yacc

class MyLexer(object):
    tokens = (
        'NUMBER',
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
        'LPAREN', 'RPAREN',
    )

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    ...

    def __init__(self):
        # Build the lexer
        self.lexer = lex.lex(module=self)


class MyParser(object):

    tokens = MyLexer.tokens

    ...

    def p_expression_binop(self, t):
        '''
        expression : expression PLUS expression
                   | expression MINUS expression
                   | expression TIMES expression
                   | expression DIVIDE expression
        '''
        left_hand_side = t[1]
        right_hand_side = t[3]
        operator = t[2]
        if operator == '+':
            value = left_hand_side + right_hand_side
        elif operator == '-':
            value = left_hand_side - right_hand_side
        elif operator == '*':
            value = left_hand_side * right_hand_side
        elif operator == '/':
            value = left_hand_side / right_hand_side
        else:
            raise AssertionError('Unknown operator: {}'.format(operator))

        t[0] = value

    ...

    def __init__(self):
        self.lexer = MyLexer()
        self.parser = yacc.yacc(module=self)

parser=MyParser()
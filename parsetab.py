
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDOP ASSIGN BEGIN CMP COMMA DO ELSE END FI IDENTIFIER IF LPAREN MULOP NUMBER_FLOAT NUMBER_INT OD READ RPAREN SEMICOLON THEN TYPE WHILE WRITEprogram : BEGIN statementList ENDempty :statementList : statement SEMICOLON statementList\n                     | empty\n    statement : IDENTIFIER ASSIGN expression\n                 | IDENTIFIERS ASSIGN expression\n                 | TYPE IDENTIFIER ASSIGN expression\n                 | TYPE IDENTIFIERS ASSIGN expression\n                 | IF relation THEN statementList FI\n                 | IF relation THEN statementList ELSE statementList FI\n                 | WHILE relation DO statementList OD\n                 | WRITE LPAREN expression RPAREN\n    IDENTIFIERS : IDENTIFIER COMMA IDENTIFIERS\n                   | IDENTIFIER\n    expression : term\n                  | expression ADDOP term\n    term : factor\n            | factor MULOP factor\n    factor : IDENTIFIER\n              | LPAREN TYPE RPAREN IDENTIFIER\n              | NUMBER_INT\n              | NUMBER_FLOAT\n              | READ\n              | LPAREN expression RPAREN\n              | LPAREN TYPE RPAREN LPAREN expression RPAREN\n    relation : expression CMP expression'
    
_lr_action_items = {'BEGIN':([0,],[2,]),'$end':([1,12,],[0,-1,]),'IDENTIFIER':([2,8,9,10,13,14,15,16,24,29,35,36,37,38,39,40,43,51,56,57,],[6,17,23,23,6,23,32,23,23,23,23,23,6,23,23,23,6,58,6,23,]),'TYPE':([2,13,24,37,43,56,],[8,8,41,8,8,8,]),'IF':([2,13,37,43,56,],[9,9,9,9,9,]),'WHILE':([2,13,37,43,56,],[10,10,10,10,10,]),'WRITE':([2,13,37,43,56,],[11,11,11,11,11,]),'END':([2,3,5,13,30,],[-2,12,-4,-2,-3,]),'SEMICOLON':([4,21,22,23,25,26,27,31,34,45,46,49,50,52,54,55,58,59,62,63,],[13,-15,-17,-19,-21,-22,-23,-5,-6,-7,-8,-16,-18,-24,-12,-9,-20,-11,-10,-25,]),'FI':([5,13,30,37,47,56,60,],[-4,-2,-3,-2,55,-2,62,]),'ELSE':([5,13,30,37,47,],[-4,-2,-3,-2,56,]),'OD':([5,13,30,43,53,],[-4,-2,-3,-2,59,]),'ASSIGN':([6,7,17,18,32,33,],[14,16,35,36,-14,-13,]),'COMMA':([6,17,32,],[15,15,15,]),'LPAREN':([9,10,11,14,16,24,29,35,36,38,39,40,51,57,],[24,24,29,24,24,24,24,24,24,24,24,24,57,24,]),'NUMBER_INT':([9,10,14,16,24,29,35,36,38,39,40,57,],[25,25,25,25,25,25,25,25,25,25,25,25,]),'NUMBER_FLOAT':([9,10,14,16,24,29,35,36,38,39,40,57,],[26,26,26,26,26,26,26,26,26,26,26,26,]),'READ':([9,10,14,16,24,29,35,36,38,39,40,57,],[27,27,27,27,27,27,27,27,27,27,27,27,]),'THEN':([19,21,22,23,25,26,27,48,49,50,52,58,63,],[37,-15,-17,-19,-21,-22,-23,-26,-16,-18,-24,-20,-25,]),'CMP':([20,21,22,23,25,26,27,49,50,52,58,63,],[38,-15,-17,-19,-21,-22,-23,-16,-18,-24,-20,-25,]),'ADDOP':([20,21,22,23,25,26,27,31,34,42,44,45,46,48,49,50,52,58,61,63,],[39,-15,-17,-19,-21,-22,-23,39,39,39,39,39,39,39,-16,-18,-24,-20,39,-25,]),'RPAREN':([21,22,23,25,26,27,41,42,44,49,50,52,58,61,63,],[-15,-17,-19,-21,-22,-23,51,52,54,-16,-18,-24,-20,63,-25,]),'DO':([21,22,23,25,26,27,28,48,49,50,52,58,63,],[-15,-17,-19,-21,-22,-23,43,-26,-16,-18,-24,-20,-25,]),'MULOP':([22,23,25,26,27,52,58,63,],[40,-19,-21,-22,-23,-24,-20,-25,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statementList':([2,13,37,43,56,],[3,30,47,53,60,]),'statement':([2,13,37,43,56,],[4,4,4,4,4,]),'empty':([2,13,37,43,56,],[5,5,5,5,5,]),'IDENTIFIERS':([2,8,13,15,37,43,56,],[7,18,7,33,7,7,7,]),'relation':([9,10,],[19,28,]),'expression':([9,10,14,16,24,29,35,36,38,57,],[20,20,31,34,42,44,45,46,48,61,]),'term':([9,10,14,16,24,29,35,36,38,39,57,],[21,21,21,21,21,21,21,21,21,49,21,]),'factor':([9,10,14,16,24,29,35,36,38,39,40,57,],[22,22,22,22,22,22,22,22,22,22,50,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> BEGIN statementList END','program',3,'p_program','parser.py',7),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',13),
  ('statementList -> statement SEMICOLON statementList','statementList',3,'p_statementList','parser.py',17),
  ('statementList -> empty','statementList',1,'p_statementList','parser.py',18),
  ('statement -> IDENTIFIER ASSIGN expression','statement',3,'p_statement','parser.py',26),
  ('statement -> IDENTIFIERS ASSIGN expression','statement',3,'p_statement','parser.py',27),
  ('statement -> TYPE IDENTIFIER ASSIGN expression','statement',4,'p_statement','parser.py',28),
  ('statement -> TYPE IDENTIFIERS ASSIGN expression','statement',4,'p_statement','parser.py',29),
  ('statement -> IF relation THEN statementList FI','statement',5,'p_statement','parser.py',30),
  ('statement -> IF relation THEN statementList ELSE statementList FI','statement',7,'p_statement','parser.py',31),
  ('statement -> WHILE relation DO statementList OD','statement',5,'p_statement','parser.py',32),
  ('statement -> WRITE LPAREN expression RPAREN','statement',4,'p_statement','parser.py',33),
  ('IDENTIFIERS -> IDENTIFIER COMMA IDENTIFIERS','IDENTIFIERS',3,'p_identifiers','parser.py',100),
  ('IDENTIFIERS -> IDENTIFIER','IDENTIFIERS',1,'p_identifiers','parser.py',101),
  ('expression -> term','expression',1,'p_expression','parser.py',108),
  ('expression -> expression ADDOP term','expression',3,'p_expression','parser.py',109),
  ('term -> factor','term',1,'p_term','parser.py',140),
  ('term -> factor MULOP factor','term',3,'p_term','parser.py',141),
  ('factor -> IDENTIFIER','factor',1,'p_factor','parser.py',172),
  ('factor -> LPAREN TYPE RPAREN IDENTIFIER','factor',4,'p_factor','parser.py',173),
  ('factor -> NUMBER_INT','factor',1,'p_factor','parser.py',174),
  ('factor -> NUMBER_FLOAT','factor',1,'p_factor','parser.py',175),
  ('factor -> READ','factor',1,'p_factor','parser.py',176),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','parser.py',177),
  ('factor -> LPAREN TYPE RPAREN LPAREN expression RPAREN','factor',6,'p_factor','parser.py',178),
  ('relation -> expression CMP expression','relation',3,'p_relation','parser.py',218),
]


# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left+-CONCATleft*/ALEATORIO CONCAT ENTRADA ESCREVER FIM FOLD FUNCAO LIST MAP NUM STRING VARstart : statement\n                 | expressionstatement : VAR "=" expression ";"statement : expression ";"statement : ESCREVER "(" expression ")" ";"\n                     | ESCREVER "(" STRING ")" ";"\n                     | ESCREVER "(" VAR ")" ";"expression : expression \'+\' expression\n                      | expression \'-\' expression\n                      | expression \'*\' expression\n                      | expression \'/\' expressionexpression : expression CONCAT expressionexpression : "(" expression ")"expression : NUMexpression : VARexpression : STRINGexpression : LISTexpression : ENTRADA "(" ")"expression : ALEATORIO "(" NUM ")"\n                      | ALEATORIO "(" VAR ")"expression : FUNCAO VAR "(" params ")" "," ":" expression ";"params : VAR\n                  | VAR "," paramsexpression : VAR "(" arguments ")"arguments : expression\n                     | expression "," arguments'
    
_lr_action_items = {'VAR':([0,6,12,14,15,16,17,18,19,20,21,25,42,45,57,61,],[4,23,26,23,23,23,23,23,23,23,37,41,51,23,51,23,]),'ESCREVER':([0,],[5,]),'(':([0,4,5,6,10,11,14,15,16,17,18,19,20,21,23,26,37,45,61,],[6,20,21,6,24,25,6,6,6,6,6,6,6,6,20,42,20,6,6,]),'NUM':([0,6,14,15,16,17,18,19,20,21,25,45,61,],[8,8,8,8,8,8,8,8,8,8,40,8,8,]),'STRING':([0,6,14,15,16,17,18,19,20,21,45,61,],[7,7,7,7,7,7,7,7,7,36,7,7,]),'LIST':([0,6,14,15,16,17,18,19,20,21,45,61,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'ENTRADA':([0,6,14,15,16,17,18,19,20,21,45,61,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'ALEATORIO':([0,6,14,15,16,17,18,19,20,21,45,61,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'FUNCAO':([0,6,14,15,16,17,18,19,20,21,45,61,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'$end':([1,2,3,4,7,8,9,13,23,27,28,29,30,31,38,39,43,44,49,50,54,55,56,63,],[0,-1,-2,-15,-16,-14,-17,-4,-15,-8,-9,-10,-11,-12,-13,-18,-3,-24,-19,-20,-5,-6,-7,-21,]),';':([3,4,7,8,9,23,27,28,29,30,31,32,38,39,44,46,47,48,49,50,62,63,],[13,-15,-16,-14,-17,-15,-8,-9,-10,-11,-12,43,-13,-18,-24,54,55,56,-19,-20,63,-21,]),'+':([3,4,7,8,9,22,23,27,28,29,30,31,32,34,35,36,37,38,39,44,49,50,62,63,],[14,-15,-16,-14,-17,14,-15,-8,-9,-10,-11,-12,14,14,14,-16,-15,-13,-18,-24,-19,-20,14,-21,]),'-':([3,4,7,8,9,22,23,27,28,29,30,31,32,34,35,36,37,38,39,44,49,50,62,63,],[15,-15,-16,-14,-17,15,-15,-8,-9,-10,-11,-12,15,15,15,-16,-15,-13,-18,-24,-19,-20,15,-21,]),'*':([3,4,7,8,9,22,23,27,28,29,30,31,32,34,35,36,37,38,39,44,49,50,62,63,],[16,-15,-16,-14,-17,16,-15,16,16,-10,-11,16,16,16,16,-16,-15,-13,-18,-24,-19,-20,16,-21,]),'/':([3,4,7,8,9,22,23,27,28,29,30,31,32,34,35,36,37,38,39,44,49,50,62,63,],[17,-15,-16,-14,-17,17,-15,17,17,-10,-11,17,17,17,17,-16,-15,-13,-18,-24,-19,-20,17,-21,]),'CONCAT':([3,4,7,8,9,22,23,27,28,29,30,31,32,34,35,36,37,38,39,44,49,50,62,63,],[18,-15,-16,-14,-17,18,-15,-8,-9,-10,-11,-12,18,18,18,-16,-15,-13,-18,-24,-19,-20,18,-21,]),'=':([4,],[19,]),')':([7,8,9,22,23,24,27,28,29,30,31,33,34,35,36,37,38,39,40,41,44,49,50,51,52,53,59,63,],[-16,-14,-17,38,-15,39,-8,-9,-10,-11,-12,44,-25,46,47,48,-13,-18,49,50,-24,-19,-20,-22,58,-26,-23,-21,]),',':([7,8,9,23,27,28,29,30,31,34,38,39,44,49,50,51,58,63,],[-16,-14,-17,-15,-8,-9,-10,-11,-12,45,-13,-18,-24,-19,-20,57,60,-21,]),':':([60,],[61,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'statement':([0,],[2,]),'expression':([0,6,14,15,16,17,18,19,20,21,45,61,],[3,22,27,28,29,30,31,32,34,35,34,62,]),'arguments':([20,45,],[33,53,]),'params':([42,57,],[52,59,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> statement','start',1,'p_start','grammar.py',29),
  ('start -> expression','start',1,'p_start','grammar.py',30),
  ('statement -> VAR = expression ;','statement',4,'p_statement_assign','grammar.py',34),
  ('statement -> expression ;','statement',2,'p_statement_expr','grammar.py',38),
  ('statement -> ESCREVER ( expression ) ;','statement',5,'p_statement_write','grammar.py',42),
  ('statement -> ESCREVER ( STRING ) ;','statement',5,'p_statement_write','grammar.py',43),
  ('statement -> ESCREVER ( VAR ) ;','statement',5,'p_statement_write','grammar.py',44),
  ('expression -> expression + expression','expression',3,'p_expression_binop','grammar.py',48),
  ('expression -> expression - expression','expression',3,'p_expression_binop','grammar.py',49),
  ('expression -> expression * expression','expression',3,'p_expression_binop','grammar.py',50),
  ('expression -> expression / expression','expression',3,'p_expression_binop','grammar.py',51),
  ('expression -> expression CONCAT expression','expression',3,'p_expression_concat','grammar.py',55),
  ('expression -> ( expression )','expression',3,'p_expression_group','grammar.py',59),
  ('expression -> NUM','expression',1,'p_expression_num','grammar.py',63),
  ('expression -> VAR','expression',1,'p_expression_var','grammar.py',67),
  ('expression -> STRING','expression',1,'p_expression_string','grammar.py',71),
  ('expression -> LIST','expression',1,'p_expression_list','grammar.py',75),
  ('expression -> ENTRADA ( )','expression',3,'p_expression_entrada','grammar.py',79),
  ('expression -> ALEATORIO ( NUM )','expression',4,'p_expression_aleatorio','grammar.py',83),
  ('expression -> ALEATORIO ( VAR )','expression',4,'p_expression_aleatorio','grammar.py',84),
  ('expression -> FUNCAO VAR ( params ) , : expression ;','expression',9,'p_expression_function','grammar.py',88),
  ('params -> VAR','params',1,'p_params','grammar.py',92),
  ('params -> VAR , params','params',3,'p_params','grammar.py',93),
  ('expression -> VAR ( arguments )','expression',4,'p_expression_func_call','grammar.py',100),
  ('arguments -> expression','arguments',1,'p_arguments','grammar.py',104),
  ('arguments -> expression , arguments','arguments',3,'p_arguments','grammar.py',105),
]

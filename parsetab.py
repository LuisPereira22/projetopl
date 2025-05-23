
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDORnonassocLTLEGTGEEQNEQAND AS CALL COMMA CREATE DISCARD DO END EQ EXPORT FROM GE GT ID IMPORT JOIN LE LIMIT LPAREN LT NEQ NUMBER ON OR PRINT PROCEDURE RENAME RPAREN SELECT SEMICOLON STAR STRING TABLE USING WHEREprogram : command_listcommand_list : command SEMICOLON\n| command SEMICOLON command_listcommand : import_command\n| export_command\n| discard_command\n| rename_command\n| print_command\n| select_command\n| create_command\n| procedure_declaration\n| procedure_callimport_command : IMPORT TABLE ID FROM STRINGexport_command : EXPORT TABLE ID AS STRINGdiscard_command : DISCARD TABLE IDrename_command : RENAME TABLE ID IDprint_command : PRINT TABLE IDselect_command : SELECT select_fields FROM ID\n| SELECT select_fields FROM ID WHERE condition\n| SELECT select_fields FROM ID WHERE condition LIMIT NUMBERselect_fields : STAR\n| field_listfield_list : ID\n| ID COMMA field_listcondition : expression\n| condition AND condition\n| condition OR conditionexpression : ID operator valueoperator : EQ\n| NEQ\n| LT\n| GT\n| LE\n| GEvalue : ID\n| NUMBER\n| STRINGcreate_command : CREATE TABLE ID select_command\n| CREATE TABLE ID FROM ID JOIN ID USING LPAREN ID RPAREN\n| CREATE TABLE ID FROM ID JOIN ID ON IDprocedure_declaration : PROCEDURE ID DO command_list ENDprocedure_call : CALL ID'
    
_lr_action_items = {'IMPORT':([0,22,44,],[13,13,13,]),'EXPORT':([0,22,44,],[14,14,14,]),'DISCARD':([0,22,44,],[15,15,15,]),'RENAME':([0,22,44,],[16,16,16,]),'PRINT':([0,22,44,],[17,17,17,]),'SELECT':([0,22,43,44,],[18,18,18,18,]),'CREATE':([0,22,44,],[19,19,19,]),'PROCEDURE':([0,22,44,],[20,20,20,]),'CALL':([0,22,44,],[21,21,21,]),'$end':([1,2,22,35,],[0,-1,-2,-3,]),'SEMICOLON':([3,4,5,6,7,8,9,10,11,12,34,38,40,47,48,50,53,54,57,59,60,73,74,75,76,77,78,79,83,85,],[22,-4,-5,-6,-7,-8,-9,-10,-11,-12,-42,-15,-17,-16,-18,-38,-13,-14,-41,-19,-25,-35,-28,-36,-37,-20,-26,-27,-40,-39,]),'TABLE':([13,14,15,16,17,19,],[23,24,25,26,27,32,]),'STAR':([18,],[30,]),'ID':([18,20,21,23,24,25,26,27,32,39,41,42,51,55,61,62,63,64,65,66,67,68,70,71,81,82,],[29,33,34,36,37,38,39,40,43,47,48,29,56,58,72,73,-29,-30,-31,-32,-33,-34,58,58,83,84,]),'END':([22,35,52,],[-2,-3,57,]),'FROM':([28,29,30,31,36,43,49,],[41,-23,-21,-22,45,51,-24,]),'COMMA':([29,],[42,]),'DO':([33,],[44,]),'AS':([37,],[46,]),'STRING':([45,46,62,63,64,65,66,67,68,],[53,54,76,-29,-30,-31,-32,-33,-34,]),'WHERE':([48,],[55,]),'JOIN':([56,],[61,]),'EQ':([58,],[63,]),'NEQ':([58,],[64,]),'LT':([58,],[65,]),'GT':([58,],[66,]),'LE':([58,],[67,]),'GE':([58,],[68,]),'LIMIT':([59,60,73,74,75,76,78,79,],[69,-25,-35,-28,-36,-37,-26,-27,]),'AND':([59,60,73,74,75,76,78,79,],[70,-25,-35,-28,-36,-37,-26,-27,]),'OR':([59,60,73,74,75,76,78,79,],[71,-25,-35,-28,-36,-37,-26,-27,]),'NUMBER':([62,63,64,65,66,67,68,69,],[75,-29,-30,-31,-32,-33,-34,77,]),'USING':([72,],[80,]),'ON':([72,],[81,]),'LPAREN':([80,],[82,]),'RPAREN':([84,],[85,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'command_list':([0,22,44,],[2,35,52,]),'command':([0,22,44,],[3,3,3,]),'import_command':([0,22,44,],[4,4,4,]),'export_command':([0,22,44,],[5,5,5,]),'discard_command':([0,22,44,],[6,6,6,]),'rename_command':([0,22,44,],[7,7,7,]),'print_command':([0,22,44,],[8,8,8,]),'select_command':([0,22,43,44,],[9,9,50,9,]),'create_command':([0,22,44,],[10,10,10,]),'procedure_declaration':([0,22,44,],[11,11,11,]),'procedure_call':([0,22,44,],[12,12,12,]),'select_fields':([18,],[28,]),'field_list':([18,42,],[31,49,]),'condition':([55,70,71,],[59,78,79,]),'expression':([55,70,71,],[60,60,60,]),'operator':([58,],[62,]),'value':([62,],[74,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> command_list','program',1,'p_program','cql_parser.py',14),
  ('command_list -> command SEMICOLON','command_list',2,'p_command_list','cql_parser.py',18),
  ('command_list -> command SEMICOLON command_list','command_list',3,'p_command_list','cql_parser.py',19),
  ('command -> import_command','command',1,'p_command','cql_parser.py',26),
  ('command -> export_command','command',1,'p_command','cql_parser.py',27),
  ('command -> discard_command','command',1,'p_command','cql_parser.py',28),
  ('command -> rename_command','command',1,'p_command','cql_parser.py',29),
  ('command -> print_command','command',1,'p_command','cql_parser.py',30),
  ('command -> select_command','command',1,'p_command','cql_parser.py',31),
  ('command -> create_command','command',1,'p_command','cql_parser.py',32),
  ('command -> procedure_declaration','command',1,'p_command','cql_parser.py',33),
  ('command -> procedure_call','command',1,'p_command','cql_parser.py',34),
  ('import_command -> IMPORT TABLE ID FROM STRING','import_command',5,'p_import_command','cql_parser.py',38),
  ('export_command -> EXPORT TABLE ID AS STRING','export_command',5,'p_export_command','cql_parser.py',42),
  ('discard_command -> DISCARD TABLE ID','discard_command',3,'p_discard_command','cql_parser.py',46),
  ('rename_command -> RENAME TABLE ID ID','rename_command',4,'p_rename_command','cql_parser.py',50),
  ('print_command -> PRINT TABLE ID','print_command',3,'p_print_command','cql_parser.py',54),
  ('select_command -> SELECT select_fields FROM ID','select_command',4,'p_select_command','cql_parser.py',58),
  ('select_command -> SELECT select_fields FROM ID WHERE condition','select_command',6,'p_select_command','cql_parser.py',59),
  ('select_command -> SELECT select_fields FROM ID WHERE condition LIMIT NUMBER','select_command',8,'p_select_command','cql_parser.py',60),
  ('select_fields -> STAR','select_fields',1,'p_select_fields','cql_parser.py',69),
  ('select_fields -> field_list','select_fields',1,'p_select_fields','cql_parser.py',70),
  ('field_list -> ID','field_list',1,'p_field_list','cql_parser.py',74),
  ('field_list -> ID COMMA field_list','field_list',3,'p_field_list','cql_parser.py',75),
  ('condition -> expression','condition',1,'p_condition','cql_parser.py',82),
  ('condition -> condition AND condition','condition',3,'p_condition','cql_parser.py',83),
  ('condition -> condition OR condition','condition',3,'p_condition','cql_parser.py',84),
  ('expression -> ID operator value','expression',3,'p_expression','cql_parser.py',91),
  ('operator -> EQ','operator',1,'p_operator','cql_parser.py',95),
  ('operator -> NEQ','operator',1,'p_operator','cql_parser.py',96),
  ('operator -> LT','operator',1,'p_operator','cql_parser.py',97),
  ('operator -> GT','operator',1,'p_operator','cql_parser.py',98),
  ('operator -> LE','operator',1,'p_operator','cql_parser.py',99),
  ('operator -> GE','operator',1,'p_operator','cql_parser.py',100),
  ('value -> ID','value',1,'p_value','cql_parser.py',104),
  ('value -> NUMBER','value',1,'p_value','cql_parser.py',105),
  ('value -> STRING','value',1,'p_value','cql_parser.py',106),
  ('create_command -> CREATE TABLE ID select_command','create_command',4,'p_create_command','cql_parser.py',110),
  ('create_command -> CREATE TABLE ID FROM ID JOIN ID USING LPAREN ID RPAREN','create_command',11,'p_create_command','cql_parser.py',111),
  ('create_command -> CREATE TABLE ID FROM ID JOIN ID ON ID','create_command',9,'p_create_command','cql_parser.py',112),
  ('procedure_declaration -> PROCEDURE ID DO command_list END','procedure_declaration',5,'p_procedure_declaration','cql_parser.py',125),
  ('procedure_call -> CALL ID','procedure_call',2,'p_procedure_call','cql_parser.py',129),
]

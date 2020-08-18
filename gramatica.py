from ply import lex
import ply.yacc as yacc
from Nodo import *
tokens=[
    'entero',
    'pa_cerrado',
    'pa_abierto',
    'menos',
    'mas',
    'por',  
    'div'
     
]
# Tokens


t_mas        = r'\+'
t_menos      = r'-'
t_por        = r'\*'
t_div        = r'/'
t_pa_cerrado = r'\)'
t_pa_abierto = r'\('
def t_entero(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
cont = 0
precedence = (
    ( 'left', 'mas', 'menos' ),
    ( 'left', 'por', 'div' )
)

    
def p_S_( p ):
    '''init : E'''
    p[0]=S("S",p[1])
    
def p_operaciones( p ):
     '''E  : E mas E
           | E menos E 
           | E por E
           | E div E
           | pa_abierto E pa_cerrado  
           '''
     if p[2] == '+':
           p[0]=Suma("E",p[1],"+",p[3])  
      
     elif p[2] == '-':

           p[0]=Resta("E",p[1],"-",p[3])
     elif p[2] == '*':

           p[0]=Multiplicacion("E",p[1],"*",p[3])
     elif  p[2] == '/':

           p[0]=Division("E",p[1],"/",p[3])  
     elif  p[1]=='(' and p[3]==')':
           p[0]=Pa_Entero_PC("E",p[2]) 

def p_Entero( p ) :
    'E : entero'
    p[0]=Entero(p[1])
      
    
def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()

def Analizador(cadenaentrada=""):
   
   res = parser.parse(cadenaentrada) # the input
   #print(res.Resultado())   
   return res  




# mapeia os codigos do projeto para converter em codigo
MAPEAMENTO = {
    'inteiro': 'int',
    'letras': 'str',
    'real': 'float',
    'logico': 'bool',
    
    'recebe': 'input',
    'escreva': 'print',
    'se': 'if',
    'casoNao': 'elif',
    'nadaAcima': 'else',
    
    'para': 'for',
    'em': 'in',
    'conta': 'range',
    'enquanto': 'while',
    'quebre': 'break',
    'continue': 'continue',
    
    'funcao': 'def',
    'retornar': 'return'
}

#codigos que não são permitidos ter no .jota
CONSTRUCOES_PYTHON_NAO_PERMITIDAS = ['print', 'input']

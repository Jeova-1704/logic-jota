#funçao que abre o arquivo e manda como parametro para a outra função
def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        codigo_jota = arquivo.read()
        codigo_python = interpretar_logica_jota(codigo_jota)
        
        try:
            exec(codigo_python)
        except Exception as e:
            print(f"Erro na execução: {e}")
            
            
            
            
#script para interpretar comandos em "logic.jota" e executar em Python
def interpretar_logica_jota(codigo_jota):
    # Implementa e analisador léxico e sintático aqui (usando ANTLR, PLY, etc.)
    # Converte os comandos para código Python
    # mapeamento 
    mapeamento = {
        'inteiro': 'int',
        'letras': 'str',
        'real':'float',
        'logico':'bool',
        'recebe': 'input',
        'escreva': 'print',
        'se': 'if',
        'casoNao': 'else'
        
    }
    
    codigo_python = ""
    linhas = codigo_jota.split('\n')
    
    for linha in linhas:
        for comando, equivalente_python in mapeamento.items():
            linha = linha.replace(comando, equivalente_python)
        codigo_python += linha + '\n'
    print(codigo_python)
    return codigo_python
     
            
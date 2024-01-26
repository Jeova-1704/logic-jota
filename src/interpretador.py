#funçao que abre o arquivo e manda como parametro para a outra função
def main(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        codigo_jota = arquivo.read()
        codigo_python, jota_response = interpretar_logica_jota(codigo_jota)
        executa = tratamento_erro(jota_response)
        
        if executa:
            executar_codigo(codigo_python)
            
            
            
#script para interpretar comandos em "logic.jota" e executar em Python
def interpretar_logica_jota(codigo_jota):

    # mapeamento
    mapeamento = {
        'inteiro': 'int',
        'letras': 'str',
        'real': 'float',
        'logico': 'bool',
        
        'recebe': 'input',
        'escreva': 'print',
        'se': 'if',
        'casoNao': 'else',
        
        'para': 'for',
        'enquanto': 'while',
        'quebre': 'break',
        'continue': 'continue'
    }

    # Adiciona construções Python específicas que não são permitidas
    construcoes_python_nao_permitidas = ['print', 'input']

    codigo_python = ""
    linhas = codigo_jota.split('\n')

    for linha in linhas:

        # Verifica construções Python não permitidas
        if any(construct in linha for construct in construcoes_python_nao_permitidas):
            return None, 400

        for comando, equivalente_python in mapeamento.items():
            linha = linha.replace(comando, equivalente_python)

        codigo_python += linha + '\n'
        
    print(codigo_python)
    print("=======================================================================")
    print()
    return codigo_python, 200
  


#Executa o codigo python
def executar_codigo(codigo):
    try:
        codigo_compilado = compile(codigo, "<string>", "exec")
        exec(codigo_compilado, {}, {})
    except Exception as e:
        print(f"Erro na execução: {e}")



def tratamento_erro(response):
    if response == 200:
        return True
    elif response == 400:
        print("sintaxe invalida! Aceitamos apenas codigos da linguagem Jota.")
        return False
    
import os

def listar_arquivos_jota():
    diretorio = "src/jota"
    arquivos_jota = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith(".jota")]

    print("Arquivos Jota disponíveis:")
    for i, arquivo in enumerate(arquivos_jota, start=1):
        print(f"{i}. {arquivo}")

    escolha = int(input("Escolha o número do arquivo que deseja executar: "))
    if 1 <= escolha <= len(arquivos_jota):
        nome_arquivo = arquivos_jota[escolha - 1]
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        return caminho_arquivo
    else:
        print("Escolha inválida.")
        return None


if __name__ == "__main__":
    arquivo_escolhido = listar_arquivos_jota()

    if arquivo_escolhido:
        # Executa o interpretador.py com o arquivo escolhido
        import subprocess
        subprocess.run(["python", "interpretador.py", arquivo_escolhido])

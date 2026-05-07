import platform
import subprocess

#Função
def nome_so():
    return platform.system()

#Procedimento
def media_ping():
    so = nome_so()

    if so == "Windows":
        comando = ["ping", "-4", "-n", "10", "www.google.com.br"]
    else:
        comando = ["ping", "-4", "-c", "10", "www.google.com.br"]

    resultado = subprocess.run(comando, capture_output=True, text=True)

    linhas = resultado.stdout.split("\n")

    for linha in reversed(linhas):
        if "=" in linha:

            if so == "Windows":
                partes = linha.split("=")
                media = partes[-1].strip()
                print("Média do ping:", media)
                return

            else:
                partes = linha.split("=")[1].strip()
                valores = partes.split("/")
                media = valores[1]
                print("Média do ping:", media, "ms")
                return

    print("Não foi possível encontrar a média.")
    
media_ping()
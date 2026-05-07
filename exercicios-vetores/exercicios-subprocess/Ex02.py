import platform
import subprocess

#Função que retorna o nome do SO
def os():
    return platform.system()


#Procedimento que executa comandos
def executar_processo(acao, valor=None):
    sistema = os()

    if sistema == "Windows":

        if acao == 1:
            comando = ["TASKLIST", "/FO", "TABLE"]

        elif acao == 2:
            comando = ["TASKKILL", "/PID", str(valor)]

        elif acao == 3:
            comando = ["TASKKILL", "/IM", valor]

    else:  #Linux

        if acao == 1:
            comando = ["ps", "-ef"]

        elif acao == 2:
            comando = ["kill", "-9", str(valor)]

        elif acao == 3:
            comando = ["pkill", "-f", valor]

    resultado = subprocess.run(comando, capture_output=True, text=True)

    print(resultado.stdout)
    print(resultado.stderr)


def main():
    while True:
        print("\n1 - Listar processos")
        print("2 - Matar por PID")
        print("3 - Matar por nome")
        print("9 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            executar_processo(1)

        elif opcao == "2":
            pid = input("Digite o PID: ")
            executar_processo(2, pid)

        elif opcao == "3":
            nome = input("Digite o nome do processo: ")
            executar_processo(3, nome)

        elif opcao == "9":
            print("Encerrando")
            break

        else:
            print("Opção inválida")

main()
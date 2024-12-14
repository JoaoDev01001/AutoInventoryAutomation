import pyautogui as py
import time as espera
from threading import Thread

py.FAILSAFE = True
py.PAUSE = 0

codigo = "codigo.txt"
derivacao = "derivacao.txt"
sequencia = "sequencia.txt"
quantidade = "quantidade.txt"
log = "Log_Execucao.txt"

for arquivo in [codigo, log, derivacao, sequencia, quantidade]:
    with open(arquivo, "a") as f:
        pass

print("\n>> Aguardando 5 segundos para preparar o ambiente... (Mova o mouse para o canto superior esquerdo para cancelar)")
espera.sleep(5)

buffer_log = []

def log_atividade_buffer(mensagem):
    """Adiciona mensagens ao buffer e grava em lotes para reduzir escrita no disco."""
    global buffer_log
    buffer_log.append(mensagem)
    if len(buffer_log) >= 50:
        with open(log, "a") as arquivo_log:
            arquivo_log.write("\n".join(buffer_log) + "\n")
        buffer_log = []

def finalizar_logs():
    """Grava qualquer log restante no buffer ao final do programa."""
    global buffer_log
    if buffer_log:
        with open(log, "a") as arquivo_log:
            arquivo_log.write("\n".join(buffer_log) + "\n")
        buffer_log = []

def calcular_tempo(func):
    """Decora funções para calcular o tempo de execução."""
    def wrapper(*args, **kwargs):
        inicio = espera.time()
        resultado = func(*args, **kwargs)
        fim = espera.time()
        print(f"Tempo total para a operação: {fim - inicio:.2f} segundos.")
        return resultado
    return wrapper

@calcular_tempo
def processar_arquivo(acao, intervalo, linhas):
    for i, linha in enumerate(linhas):
        linha = linha.strip()
        py.write(linha)
        py.press(acao)
        log_atividade_buffer(f"Linha {i+1} processada: {linha}")
        if intervalo > 0:
            espera.sleep(intervalo)
    print(f"\n>> Total de itens digitados: {len(linhas)}.")
    print("\n>> Finalizado! Verifique o log para mais detalhes.\n")
    finalizar_logs()

def gerar_sequencia():
    try:
        with open(codigo, "r") as arquivo:
            linhas = arquivo.readlines()
            sequencia_gerada = [str(i + 1) for i in range(len(linhas))]
        with open(sequencia, "w") as seq_file:
            seq_file.write("\n".join(sequencia_gerada))
        print(">> Sequência gerada com sucesso no arquivo 'sequencia.txt'.")
        log_atividade_buffer("Sequência gerada no arquivo 'sequencia.txt'.")
    except Exception as e:
        print(f">> ERRO ao gerar sequência: {e}")
        log_atividade_buffer(f"ERRO ao gerar sequência: {e}")

def digitar_sequencia(sequencia):
    for numero in sequencia:
        py.write(numero)
        py.press("enter")
        log_atividade_buffer(f"Número {numero} digitado.")

def sub_menu_sequencia():
    print("""
OPÇÕES DE SEQUÊNCIA:
    1 - Usar índices como sequência e digitar automaticamente
    2 - Gerar sequência no arquivo e depois digitar
    """)
    opcao = input("Escolha a opção: ")
    if opcao == "1":
        try:
            with open(codigo, "r") as arquivo:
                linhas = arquivo.readlines()
                sequencia_gerada = [str(i + 1) for i in range(len(linhas))]
            print("Começando em 5 segundos...")
            espera.sleep(5)
            print("\n>> Iniciando digitação da sequência...")
            digitar_sequencia(sequencia_gerada)
        except Exception as e:
            print(f">> ERRO ao digitar sequência: {e}")
            log_atividade_buffer(f"ERRO ao digitar sequência: {e}")
    elif opcao == "2":
        gerar_sequencia()
        with open(sequencia, "r") as seq_file:
            linhas = seq_file.readlines()
        print("Começando em 5 segundos...")
        espera.sleep(5)
        processar_arquivo("enter", 4, linhas)
    else:
        print("Opção inválida! Voltando ao menu principal...")
        menu()

def sub_menu(arqu):
    print("""
TIPO DE DIGITAÇÃO:
    1 - Press 'enter'
    2 - Press 'down' (seta para baixo)
    """)
    opcao = input("Escolha a opção: ")
    if opcao == "1":
        digt = "enter"
        intervalo = 4
    elif opcao == "2":
        digt = "down"
        intervalo = 0
    else:
        print("Opção inválida! Voltando ao menu principal...")
        menu()
        return
    with open(arqu, "r") as arquivo:
        linhas = arquivo.readlines()
    print("Começando em 5 segundos...")
    espera.sleep(5)
    thread = Thread(target=processar_arquivo, args=(digt, intervalo, linhas))
    thread.start()
    thread.join()

def menu():
    print("\n" + "="*45)
    print("MENU PRINCIPAL - DIGITAÇÃO DE INVENTÁRIO")
    print("="*45 + "\n")
    print("""
OPÇÕES:
    1 - DIGITAR CODIGO
    2 - DIGITAR DERIVAÇÃO
    3 - DIGITAR SEQUÊNCIA
    4 - DIGITAR QUANTIDADE
    5 - SAIR
    """)
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        sub_menu(codigo)
    elif opcao == "2":
        sub_menu(derivacao)
    elif opcao == "3":
        sub_menu_sequencia()
    elif opcao == "4":
        sub_menu(quantidade)
    elif opcao == "5":
        print(">> Encerrando programa... Até mais!")
        exit()
    else:
        print(">> Opção inválida! Tente novamente.")
        menu()

menu()

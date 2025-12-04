import os
import platform
import random


# Configurações

RESET = "\033[0m"
VERMELHO = "\033[91m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CIANO = "\033[96m"


# Sistema / Som

sistema = platform.system()

if sistema == "Windows":
    try:
        import winsound
        def beep():
            winsound.Beep(600, 120)
    except Exception:
        def beep():
            print("\a", end="")
else:
    def beep():
        print("\a", end="")

# Limpar Tela

def limpar():
    os.system("cls" if sistema == "Windows" else "clear")


# Tabuleiro / Tema
def mostrar_tabuleiro(tab, tema=1):
    if tema == 1:  # Clássico
        linha = "---+---+---"
    elif tema == 2:  # Neon
        linha = AMARELO + "═══╬═══╬═══" + RESET
    else:  # Futurista
        linha = MAGENTA + "≡≡≡╬≡≡≡╬≡≡≡" + RESET

    cor = AZUL if tema == 1 else (VERDE if tema == 2 else MAGENTA)

    print("\n")
    print(f" {cor}{tab[0]}{RESET} | {cor}{tab[1]}{RESET} | {cor}{tab[2]}{RESET}")
    print(linha)
    print(f" {cor}{tab[3]}{RESET} | {cor}{tab[4]}{RESET} | {cor}{tab[5]}{RESET}")
    print(linha)
    print(f" {cor}{tab[6]}{RESET} | {cor}{tab[7]}{RESET} | {cor}{tab[8]}{RESET}")
    print("\n")


# Funções do jogo
def venceu(tab, j):
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(tab[a] == tab[b] == tab[c] == j for a,b,c in combos)

def movimentos_disponiveis(tab):
    return [i for i, v in enumerate(tab) if v == " "]


# IA Difícil
def minimax(tab, jogador):
    if venceu(tab, "O"):
        return 1
    if venceu(tab, "X"):
        return -1
    if " " not in tab:
        return 0

    if jogador == "O":
        melhor = -99
        for m in movimentos_disponiveis(tab):
            tab[m] = "O"
            valor = minimax(tab, "X")
            tab[m] = " "
            melhor = max(melhor, valor)
        return melhor
    else:
        pior = 99
        for m in movimentos_disponiveis(tab):
            tab[m] = "X"
            valor = minimax(tab, "O")
            tab[m] = " "
            pior = min(pior, valor)
        return pior

def melhor_jogada(tab):
    melhor = -99
    move = None
    for m in movimentos_disponiveis(tab):
        tab[m] = "O"
        valor = minimax(tab, "X")
        tab[m] = " "
        if valor > melhor:
            melhor = valor
            move = m
    return move


# Placar

placar = {"X": 0, "O": 0, "empates": 0}


# Modo: Player vs IA
def jogar_vs_ia(nivel, tema):
    tab = [" "] * 9
    jogador_atual = "X"

    while True:
        limpar()
        print(CIANO + f"JOGO DA VELHA — IA ({nivel})" + RESET)
        mostrar_tabuleiro(tab, tema)

        if jogador_atual == "X":
            try:
                pos = int(input("Sua jogada (1-9): ")) - 1
            except ValueError:
                continue

            if pos not in range(9) or tab[pos] != " ":
                print(VERMELHO + "Jogada inválida!" + RESET)
                input("ENTER para continuar...")
                continue

            beep()
            tab[pos] = "X"

        else:
            print(AMARELO + "IA pensando..." + RESET)

            if nivel == "Fácil":
                pos = random.choice(movimentos_disponiveis(tab))
            elif nivel == "Médio":
                if random.random() < 0.5:
                    pos = random.choice(movimentos_disponiveis(tab))
                else:
                    pos = melhor_jogada(tab)
            else:  # Difícil
                pos = melhor_jogada(tab)

            tab[pos] = "O"
            beep()

        # Resultado
        if venceu(tab, jogador_atual):
            limpar()
            mostrar_tabuleiro(tab, tema)
            if jogador_atual == "X":
                print(VERDE + "🎉 Você venceu!" + RESET)
                placar["X"] += 1
            else:
                print(VERMELHO + "🤖 A IA venceu!" + RESET)
                placar["O"] += 1
            break

        if " " not in tab:
            limpar()
            mostrar_tabuleiro(tab, tema)
            print(AMARELO + "Empate!" + RESET)
            placar["empates"] += 1
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

    input("ENTER para voltar ao menu...")


# Modo: 2 JOGADORES
def jogar_2p(tema):
    tab = [" "] * 9
    jogador_atual = "X"

    while True:
        limpar()
        print(MAGENTA + "JOGO DA VELHA — 2 JOGADORES" + RESET)
        mostrar_tabuleiro(tab, tema)

        try:
            pos = int(input(f"Jogador {jogador_atual}, escolha (1-9): ")) - 1
        except ValueError:
            continue

        if pos not in range(9) or tab[pos] != " ":
            print(VERMELHO + "Jogada inválida!" + RESET)
            input("ENTER para continuar...")
            continue

        beep()
        tab[pos] = jogador_atual

        if venceu(tab, jogador_atual):
            limpar()
            mostrar_tabuleiro(tab, tema)
            print(VERDE + f"🎉 Jogador {jogador_atual} venceu!" + RESET)
            placar[jogador_atual] += 1
            break

        if " " not in tab:
            limpar()
            mostrar_tabuleiro(tab, tema)
            print(AMARELO + "Empate!" + RESET)
            placar["empates"] += 1
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

    input("ENTER para voltar ao menu...")


# Menu Principal

def menu():
    tema = 1
    while True:
        limpar()
        print(CIANO + "===== JOGO DA VELHA =====" + RESET)
        print(f"Tema atual: {tema}")
        print(f"Placar: X={placar['X']}  O={placar['O']}  Empates={placar['empates']}\n")
        print("[1] Jogar vs IA — Fácil")
        print("[2] Jogar vs IA — Médio")
        print("[3] Jogar vs IA — Difícil")
        print("[4] Dois Jogadores (2P)")
        print("[5] Mudar Tema")
        print("[6] Resetar Placar")
        print("[7] Sair")

        op = input("\nEscolha: ").strip()

        if op == "1":
            jogar_vs_ia("Fácil", tema)
        elif op == "2":
            jogar_vs_ia("Médio", tema)
        elif op == "3":
            jogar_vs_ia("Difícil", tema)
        elif op == "4":
            jogar_2p(tema)
        elif op == "5":
            tema = tema % 3 + 1
        elif op == "6":
            placar["X"] = placar["O"] = placar["empates"] = 0
            input("Placar resetado. ENTER...")
        elif op == "7":
            limpar()
            print("Saindo... Até logo!")
            break
        else:
            input("Opção inválida. ENTER...")

if __name__ == "__main__":
    menu()

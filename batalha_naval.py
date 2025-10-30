import random

tabuleiro_jogador = []
tabuleiro_computador = []


def gerar_matriz():
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append("~")
        tabuleiro.append(linha)

    return tabuleiro


def preencher_tabuleiro_jogador(matriz):
    tabuleiro_jogador = gerar_matriz()

    for linha, coluna in matriz:
        tabuleiro_jogador[linha][coluna] = "<->"
    print("=====" * 10)
    print("\nCampo montado:\n")
    for linha in tabuleiro_jogador:
        print(" ".join(linha))

    return tabuleiro_jogador


def preencher_tabuleiro_computador(embarcasoes=5):
    tabuleiro_computador = gerar_matriz()
    colocados = 0

    while colocados < embarcasoes:
        linha_c = random.randint(0, 9)
        coluna_c = random.randint(0, 9)
        if tabuleiro_computador[linha_c][coluna_c] == "~":
            tabuleiro_computador[linha_c][coluna_c] = "<->"
            colocados += 1

    return tabuleiro_computador


def ataque_jogador(att_linha, att_coluna, tabuleiro_computador):
    if tabuleiro_computador[att_linha][att_coluna] == "~":
        print("=====" * 10)
        print("Errou!\nAcertou na água!\n")
        tabuleiro_computador[att_linha][att_coluna] = "o"
        acerto_jogador = False

    elif tabuleiro_computador[att_linha][att_coluna] == "<->":
        print("=====" * 10)
        print("Parabens! Acertou uma embarcação! Tente novamente!\n")
        tabuleiro_computador[att_linha][att_coluna] = "X"
        acerto_jogador = True

    else:
        print("=====" * 10)
        print("Você já atacou nessa posição.\n")
        acerto_jogador = False

    return acerto_jogador


def ataque_computador(x, y, tabuleiro_jogador):
    if tabuleiro_jogador[x][y] == "~":
        print("=====" * 10)
        print("Computador Errou!\nAcertou na água!\n")
        tabuleiro_jogador[x][y] = "o"
        acerto_computador = False
    elif tabuleiro_jogador[x][y] == "<->":
        print("=====" * 10)
        print("Parabens! Computador Acertou uma embarcação! Tente novamente!\n")
        tabuleiro_jogador[x][y] = "X"
        acerto_computador = True
    else:
        print("=====" * 10)
        print("Computador já atacou nessa posição.\n")
        acerto_computador = False

    print("\nTabuleiro do jogador:\n")
    for linha in tabuleiro_jogador:
        print(" ".join(linha))
    print("=====" * 10)

    return acerto_computador


def imprimir_tabuleiro(tabuleiro):
    print("\n\tTabuleiro do computador:\n")
    for linha in tabuleiro:
        print(" ".join(linha))


campo_jogador = gerar_matriz()
campo_computador = gerar_matriz()

embarcasao_jogador_posicionada = False
embarcasao_computador_posicionada = False

while True:
    try:
        print("=====" * 10)
        print("\n\tBATALHA NAVAL\n")
        print("1 - Posicionar embarcações.\n2 - Atacar.\n3 - Mostrar tabuleiro do computador.\n0 - Sair")
        opsao = int(input("\nOpção: "))
        print("=====" * 10)
        match (opsao):
            case 1:
                embarcasao = []
                print("=====" * 10)
                print("\n\t1 - Posicinar embarcações:\n")

                for i in range(5):
                    while True:
                        try:
                            linha = int(input(f"Escreva a posição da linha (0-9) do barco {i+1}: "))
                            coluna = int(input(f"Escreva a posição da coluna (0-9) do barco {i+1}: "))

                            # Verifica se está dentro dos limites do tabuleiro
                            if not (0 <= linha < 10 and 0 <= coluna < 10):
                                print("Posição inválida! Escolha valores entre 0 e 9.\n")
                                print("=====" * 10)
                                continue

                            # Verifica se já há um barco nessa posição
                            if (linha, coluna) in embarcasao:
                                print("Já existe uma embarcação nessa posição! Escolha outra.\n")
                                print("=====" * 10)
                                continue

                            embarcasao.append((linha, coluna))
                            break
                        except ValueError:
                            print("Entrada inválida! Digite números inteiros de 0 a 9.\n")
                            print("=====" * 10)

                campo_jogador = preencher_tabuleiro_jogador(embarcasao)
                campo_computador = preencher_tabuleiro_computador()
                embarcasao_jogador_posicionada = True
                embarcasao_computador_posicionada = True
                print("=====" * 10)

            case 2:
                print("=====" * 10)
                print("\n\t2 - Hora do ataque!\n")

                if not embarcasao_jogador_posicionada:
                        print("Você precisa posicionar as embarcações antes de atacar!")
                        print("=====" * 10)
                        break
                
                turno_jogador = True
                while True:
                    
                    if turno_jogador:
                        print("\nSua vez de atacar!\n")

                        try:
                            att_linha = int(input("Escreva a posição da linha (0-9): "))
                            att_coluna = int(input("Escreva a posição da coluna (0-9): "))

                            if not (0 <= att_linha < 10 and 0 <= att_coluna < 10):
                                print("Posição inválida! Escolha valores entre 0 e 9.")
                                continue
                        except ValueError:
                            print("Entrada inválida! Digite números inteiros de 0 a 9.")
                            continue

                        acerto_jogador = ataque_jogador(att_linha, att_coluna, campo_computador)

                        if not acerto_jogador:  # se errar, passa pro computador
                            turno_jogador = False

                    else:
                        posisao_x = random.randint(0, 9)
                        posisao_y = random.randint(0, 9)

                        acerto_computador = ataque_computador(
                            posisao_x, posisao_y, campo_jogador)

                        if not acerto_computador:
                            turno_jogador = True

                    # verifica vitória
                    jogador_venceu = all("<->" not in linha for linha in campo_computador)
                    computador_venceu = all("<->" not in linha for linha in campo_jogador)

                    if jogador_venceu:
                        print("=====" * 10)
                        print("\nParabens! Você venceu!")
                        imprimir_tabuleiro(campo_computador)
                        print("=====" * 10)
                        break
                    elif computador_venceu:
                        print("=====" * 10)
                        print("\nO computador venceu!")
                        imprimir_tabuleiro(campo_jogador)
                        print("=====" * 10)
                        break
                

            case 3:
                print("=====" * 10)
                imprimir_tabuleiro(campo_computador)
                print("=====" * 10)

            case 0:
                print("=====" * 10)
                print("Saindo.\nAgradeço por ter jogado.")
                print("=====" * 10)
                break

            case _:
                print("=====" * 10)
                print("Opção inválida!")
                print("=====" * 10)

    except ValueError:
        print("=====" * 10)
        print("Opção inválida!")
        print("=====" * 10)
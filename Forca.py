def forca():
    print("----X----X---- JOGO DA FORCA ----X----X----")
    print("----- ADIVINHE O NOME DE UMA FRUTA -----\n")

    import random as rd
    
    lista = ["LIMAO", "ABACAXI", "JABUTICABA", "UVA", "MELANCIA", "ABACATE", "MORANGO", "MACA", "LARANJA",
             "ABACAXI", "ACAI", "ACEROLA", "AMEIXA", "AMORA", "BANANA", "CAJU", "CAQUI", "CARAMBOLA",
             "CEREJA", "COCO", "CUPUACU", "FIGO", "FRAMBOESA", "GOIABA", "JACA", "KIWI", "MAMAO", "MANGA",
             "MARACUJA", "MELANCIA", "MELAO", "MEXERICA", "PERA", "PESSEGO", "PITAIA", "PITANGA", "ROMA",
             "TAMARINDO", "TANGERINA", "TOMATE", "TORANJA", "TAMARA", "ALFARROBA", "PINHA", "ATEMOITA", "CAFE",
             "BABACU", "CACAU", "BERGAMOTA", "BIRIBA", "CABELUDINHA", "CRANBERRY", "DAMASCO", "DURIAO", "GRAVIOLA",
             "GROSELHA", "GUARANA", "MIRTILO", "LIMA", "LICHIA", "MACADAMIA", "MIRTILO", "OXICOCO", "PEQUI",
             "UMBU"]

    def palavra_aleatoria(lista):
        tamanho = len(lista)
        sorteio = rd.randint(1, tamanho)
        palavra_aleatoria = lista[sorteio]
        return palavra_aleatoria
    
    def localizar(texto, palavra):
        posicoes = []
        for i in range(0, len(texto)):
            if texto[i] == palavra:
                posicoes.append(i)
        return posicoes
    
    palavra = palavra_aleatoria(lista)
    print(f"DICA: A palavra tem {len(palavra)} letras")

    chances = 0
    pal_secreta = list("_" * len(palavra))
    while chances <= 10:
        letra_digitada = input("Digite somente uma letra ").upper()
        if letra_digitada in palavra:
            print(f"A letra {letra_digitada} está contida na palavra")
            posicao = localizar(palavra, letra_digitada)
            for i in posicao:
                pal_secreta[i] = letra_digitada
            print(pal_secreta)
            if "_" not in pal_secreta:
                print("--------X--------X--------")
                print(f"Parabéns!\nA palavra correta e {palavra}!")
                print("--------X--------X--------")
                input("Digite qualquer coisa para encerrar o jogo ")
                break
            opcao = input("Você já sabe qual é a palavra? (S ou N): ")
            if opcao.upper() == "S":
                resposta = input("Digite a palavra: ")
                if resposta.upper() == palavra:
                    print("--------X--------X--------")
                    print(f"Parabéns!\nA palavra correta e {palavra}!")
                    print("--------X--------X--------")
                    fechar = input("Digite qualquer coisa para encerrar o jogo ")
                    break
                else:
                    print("Você errou!")
                    print(f"A palavra correta era {palavra}")
                    print("--------X GAME OVER X--------")
                    fechar = input("Digite qualquer coisa para encerrar o jogo ")
                    break
            else:
                print("--------X--------X--------\n")
                print(f"Você ainda tem mais {9-int(chances)} chances")
        else:
            print(f"A letra {letra_digitada} NÃO está contida na palavra")
            print(pal_secreta)
            opcao = input("Você ja sabe qual é a palavra? (S ou N): ")
            if opcao.upper() == "S":
                resposta = input("Digite a palavra: ")
                if resposta.upper() == palavra:
                    print("--------X--------X--------")
                    print(f"Parabéns!\nA palavra correta é {palavra}!")
                    print("--------X--------X--------")
                    fechar = input("Digite qualquer coisa para encerrar o jogo ")
                    break
                else:
                    print("Você errou!")
                    print(f"A palavra correta era {palavra}")
                    print("--------X GAME OVER X--------")
                    fechar = input("Digite qualquer coisa para encerrar o jogo ")
                    break
            else:
                print(f"Você ainda tem mais {9-int(chances)} chances")
                print("--------X--------X--------\n")
        chances += 1
        if chances >= 10:
            print("--------X GAME OVER X--------")
            print(f"A palavra correta era {palavra}")
            fechar = input("Digite qualquer coisa para encerrar o jogo ")
            break
forca()

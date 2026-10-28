
with open("entrada.txt", "r") as arquivo:
    dados = arquivo.read().split()

with open("saida.txt", "w") as arquivo:
    i = 0
    direcoes = ["N", "L", "S", "O"]

    while i < len(dados):
        n = int(dados[i])
        i += 1

        if n == 0:
            break

        comandos = dados[i]
        i += 1

        posicao = 0

        for comando in comandos:
            if comando == "D":
                posicao = (posicao + 1) % 4
            else:
                posicao = (posicao - 1) % 4

        arquivo.write(direcoes[posicao] + "\n")

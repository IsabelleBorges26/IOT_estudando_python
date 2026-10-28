
with open("entrada.txt", "r") as arquivo:
    dados = arquivo.read().split()

with open("saida.txt", "w") as arquivo:
    i = 0

    while i < len(dados):
        n = int(dados[i])
        f = int(dados[i + 1])
        i += 2

        if n == 0 and f == 0:
            break

        volume = (f * 50) / 1000 / n

        arquivo.write(f"{volume:.2f}\n")


with open("entrada.txt", "r") as arquivo:
    dados = arquivo.read().split()

with open("saida.txt", "w") as arquivo:
    for valor in dados:
        n = int(valor)

        if n == 0:
            break

        portas = []

        i = 1
        while i * i <= n:
            portas.append(str(i * i))
            i += 1

        arquivo.write(" ".join(portas) + "\n")

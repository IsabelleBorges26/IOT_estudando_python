
with open("entrada.txt", "r") as arquivo:
    dados = arquivo.read().split()

with open("saida.txt", "w") as arquivo:
    i = 0

    while i < len(dados):
        n = int(dados[i])
        i += 1

        if n == 0:
            break

        erros = {}
        resolvidos = 0
        tempo_total = 0

        for j in range(n):
            problema = dados[i]
            tempo = int(dados[i + 1])
            resultado = dados[i + 2]
            i += 3

            if problema not in erros:
                erros[problema] = 0

            if resultado == "incorrect":
                erros[problema] += 1
            else:
                resolvidos += 1
                tempo_total += tempo + erros[problema] * 20

        arquivo.write(f"{resolvidos} {tempo_total}\n")

# Esquerda, Volver!

## Descrição

O desafio consiste em descobrir para qual direção um recruta estará olhando depois de executar uma sequência de comandos para virar à esquerda ou à direita.

O recruta começa olhando para o norte.

## Lógica utilizada

Utilizei uma lista com as quatro direções. Cada comando altera a posição atual do recruta na lista. O operador `% 4` permite que as posições continuem corretas mesmo quando o recruta passa do início ou do final da lista.

## Arquivos

- `esquerda.py`: código em Python.
- `entrada.txt`: dados de entrada.
- `saida.txt`: resultados do programa.
import random

print("Olá vamos jogar?")

print("Faça sua jogada de acordo com a numeração")

print("_ _ _")
print("_ _ _")
print("_ _ _")

print("As jogadas são feitas por numeração da esquerda para direita em ordem crescente.")


def imprime_grid(grid):
    for indice in range(len(grid)):
        print(grid[indice], end=" ")
        if indice == 2 or indice == 5 or indice == 8:
            print("")


def verifica_grid(grid, jogador):
    # Testando Linhas
    if grid[0] == jogador and grid[1] == jogador and grid[2] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2

    if grid[3] == jogador and grid[4] == jogador and grid[5] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2
    if grid[6] == jogador and grid[7] == jogador and grid[8] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2

    # Testando Colunas
    if grid[0] == jogador and grid[3] == jogador and grid[6] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2
    if grid[1] == jogador and grid[4] == jogador and grid[7] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2

    if grid[2] == jogador and grid[5] == jogador and grid[8] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2

    # Testando Diagonais
    if grid[0] == jogador and grid[4] == jogador and grid[8] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2
    if grid[2] == jogador and grid[4] == jogador and grid[6] == jogador:
        if jogador == "X":
            return 1
        else:
            return 2

    return 0

quantidades_de_jogadas = 0

grid = ["_"] * 9

while True:

    escolha = int(input('Faça sua jogada:'))

    while grid[escolha-1] != "_":
        print("Sua escolha foi invalida, pois essa casa já está ocupada")
        escolha = int(input('Faça sua jogada:'))

    grid[escolha-1] = "X"
    quantidades_de_jogadas += 1
    vencedor = verifica_grid(grid, "X")

    if vencedor != 0:
        break

    imprime_grid(grid)    
    if quantidades_de_jogadas == 9:
        break

    print("Vez do computador")    
    escolha_computador = random.randint(1, 9)

    while grid[escolha_computador-1] != "_":
        escolha_computador = random.randint(1, 9)

    grid[escolha_computador-1] = "O"
    quantidades_de_jogadas += 1    
    vencedor = verifica_grid(grid, "O")

    if vencedor != 0:
        break

    imprime_grid(grid)

if vencedor == 1:
    print("Parabens você ganhou!")

elif vencedor == 2:
    print("Não foi dessa vez, você perdeu!")

else:
    print("Deu velha!")

imprime_grid(grid)

print("A quantidade de jogadas foi", quantidades_de_jogadas)


  
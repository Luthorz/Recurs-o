def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    print(f"Iniciando busca binária por {alvo} na lista {lista}")

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        print(f"Verificando índice {meio}, valor {lista[meio]}")

        if lista[meio] == alvo:
            print(f"Elemento {alvo} encontrado no índice {meio}")
            return meio  # retorna o índice do elemento
        elif lista[meio] < alvo:
            print(f"{alvo} é maior que {lista[meio]}, buscando à direita")
            esquerda = meio + 1
        else:
            print(f"{alvo} é menor que {lista[meio]}, buscando à esquerda")
            direita = meio - 1

    print(f"Elemento {alvo} não encontrado na lista")
    return -1  # se não encontrar



numeros = [1, 3, 5, 7, 9, 11]

print("\n--- Teste 1 ---")
busca_binaria(numeros, 7)  #  encontrar no índice 3

print("\n--- Teste 2 ---")
busca_binaria(numeros, 2)  # não existe, retorna -1


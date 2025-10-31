def fatorial(n):
    print(f"Entrou na funçao: n = " , n) #mostra chamada

    if n == 0 or n == 1: 
        print(f"Caso base alcançado: n =", n , "retornando 1")          #base
        return 1 
    else: 
        resultado = n *  fatorial(n - 1)  
        print(f"Saindo da função: n =", n , "fatorial = ", resultado)
        return resultado


print(fatorial(4)) #Exibe 4! 
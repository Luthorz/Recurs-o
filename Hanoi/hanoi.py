def torres_hanoi(n, origem, destino, auxiliar):

    """
    Move n discos da torre 'origem' para a torre 
    'destino' usando a torre 'auxiliar'.
    """

    if n == 1:  # Caso base: apenas 1 disco
        print(f"Mover disco 1 de {origem} para {destino}")
        return
    
    torres_hanoi(n-1, origem, auxiliar, destino) 
    print(f"Mover disco {n} de {origem} para {destino}")  
    torres_hanoi(n-1, auxiliar, destino, origem)  
    
# Exemplo de execução
n = 3  # Número de discos
torres_hanoi(n, 'A', 'C', 'B')


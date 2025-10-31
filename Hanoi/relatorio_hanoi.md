
# Universidade Federal de Santa Catarina - UFSC
## Fundamentos Matematicos



<p align="center">
<strong>Daniela T Medeiros</strong>
</p>


<p align="center">
Torres de Hanoi
</p>


<p align="center">
Araranguá
</p>
<p align="center">
2025
</p>  


## Resumo

Este relatório apresenta a implementação da **Torre de Hanói** em Python, demonstrando o uso da **recursão** para resolver problemas de movimentação de discos entre três torres.  

O trabalho detalha o **código principal**, o **caso base e o passo recursivo**, e inclui um **rastreio manual da execução**, permitindo visualizar o funcionamento do algoritmo passo a passo.  

O estudo evidencia a importância da recursão para resolver problemas matemáticos e computacionais de forma estruturada e eficiente.
  

## Sumário  

1. [Introdução](#introdução)  
2. [Desenvolvimento](#desenvolvimento)  
 2.1 [Código da Torre de Hanói](#código-da-torre-de-hanói)  
 2.2 [Caso Base e Passo Recursivo](#caso-base-e-passo-recursivo)  
 2.3 [Rastreio Manual](#rastreio-manual) 
3. [Conclusão](#conclusã)


## 1. Introdução

A Torre de Hanói é um problema clássico da computação e da matemática que ilustra de forma clara o conceito de **recursão**.  
O desafio consiste em mover uma pilha de discos de uma torre para outra, utilizando uma torre auxiliar e obedecendo a duas regras principais:  
1. Apenas um disco pode ser movido por vez.  
2. Um disco maior nunca pode ser colocado sobre um disco menor.

A implementação desse problema em **Python** permite compreender como funções recursivas funcionam na prática, uma vez que a solução é naturalmente expressa em termos de si mesma.  
Neste relatório, é apresentada a implementação do algoritmo recursivo para a Torre de Hanói, juntamente com a explicação do **caso base**, o **passo recursivo** e o **rastreio manual** de sua execução.
  

## 2. Desenvolvimento

### 2.1 Código da Torre de Hanói

A seguir, apresenta-se o código em Python que resolve o problema da Torre de Hanói utilizando uma abordagem recursiva.  
O algoritmo exibe, passo a passo, os movimentos necessários para transferir todos os discos da **torre A** para a **torre C**, utilizando a **torre B** como auxiliar.

```python
def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    torre_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    torre_hanoi(n - 1, auxiliar, destino, origem)

# Exemplo de execução com 3 discos
torre_hanoi(3, 'A', 'C', 'B')  
```  

### 2.2 Caso Base e Passo Recursivo

O algoritmo da Torre de Hanói é construído de forma recursiva, o que significa que ele chama a si mesmo até atingir uma condição de parada — o **caso base**.

- **Caso Base:**  
  Ocorre quando há apenas um disco a ser movido (`n == 1`).  
  Nesse ponto, o algoritmo realiza o movimento diretamente, sem necessidade de novas chamadas recursivas:  

  ```python
  if n == 1:
      print(f"Mova o disco 1 de {origem} para {destino}")
      return
     ```
### Passo Recursivo:

Quando há mais de um disco  **(n > 1)**  , o problema é dividido em três etapas menores:

```
1. Mover os n-1 discos superiores da torre de origem para a torre auxiliar.

2. Mover o último disco (o maior) da torre de origem para a torre de destino.

3. Mover os n-1 discos da torre auxiliar para a torre de destino.
```

Essa decomposição é expressa pelas chamadas recursivas:

```python
torre_hanoi(n - 1, origem, auxiliar, destino)
print(f"Mova o disco {n} de {origem} para {destino}")
torre_hanoi(n - 1, auxiliar, destino, origem)
``` 

### 2.3 Rastreio Manual

A seguir é apresentado o rastreio manual da execução do algoritmo para o caso de **3 discos**, ilustrando a sequência de chamadas recursivas e os movimentos realizados.

```python
def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    torre_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    torre_hanoi(n - 1, auxiliar, destino, origem)

torre_hanoi(3, 'A', 'C', 'B')
```

Durante a execução, o programa exibe o seguinte resultado:

```
Mova o disco 1 de A para C
Mova o disco 2 de A para B
Mova o disco 1 de C para B
Mova o disco 3 de A para C
Mova o disco 1 de B para A
Mova o disco 2 de B para C
Mova o disco 1 de A para C
```

Esse rastreio demonstra claramente o funcionamento da recursão, mostrando que o problema é decomposto em subproblemas menores até atingir o caso base, e então as chamadas são resolvidas em ordem inversa (de volta na pilha de chamadas).  

## 3. Conclusão

A implementação da **Torre de Hanói** demonstrou de forma prática o conceito de **recursão**, mostrando como um problema complexo pode ser decomposto em subproblemas menores até atingir um **caso base** simples.  

O rastreio manual evidenciou claramente o **fluxo de execução**, permitindo acompanhar passo a passo como os discos são movidos entre as torres, obedecendo às regras do problema.  

Dessa forma, o algoritmo recursivo não apenas resolve o problema de forma eficiente, mas também reforça o entendimento de **estruturas de controle, chamadas recursivas e pensamento lógico** aplicado à programação e à matemática.








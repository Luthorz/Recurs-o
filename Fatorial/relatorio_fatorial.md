# Universidade Federal de Santa Catarina - UFSC
## Fundamentos Matematicos



<p align="center">
<strong>Daniela T Medeiros</strong>
</p>


<p align="center">
Função Fatorial Recursiva
</p>


<p align="center">
Araranguá
</p>
<p align="center">
2025
</p>


## RESUMO 

Este relatório apresenta a implementação da função **fatorial** de forma **recursiva** em Python.  
O objetivo é demonstrar o funcionamento da recursão, identificar o **caso base** e o **passo recursivo**, além de realizar o **rastreio manual** das chamadas da função para n = 4.  
Este trabalho integra conceitos matemáticos fundamentais com programação, permitindo comprrender o cálculo do fatorial de maneira prática e visual.

## Sumário

1. [Introdução](#introdução)  
2. [Desenvolvimento](#desenvolvimento)  
    2.1 [Caso Base](#caso-base)  
    2.2  [Passo Recursivo](#passo-recursivo)  
    2.3 [Rastreio Manual](#rastreio-manual)  
3.  [Conclusão](#conclusão)

## Introdução   
O **fatorial** de um número inteiro n, representado por n!, é definido com o produto de todos os inteiros positivos de 1 até n:  

n! =  n x (n - 1) x (n -  2) x ...x 2 x 1  

O fatorial é um conceito fundamental em matématica, sendo utilizado em combninatória, probabilidade e análise de algoritmos.  

A **recursão** é uma técnica de programação na qual uma função chama a si mesma para resolver subproblemas menores.  
Neste relatório, aplicamos a recursão para calcular o fatorial, permitindo compreender o cálculo de maneira prática e visual, integrando conceitos matemáticos com programação.  


##  Desenvolvimento

### 2.1 Caso Base  
O **caso base** é a condição que interrompe a recursão e evita que a função entre em loop infinito.  
Para a função fatorial:

```Python
fatorial(0) = 1
fatorial(1) = 1  
``` 
Sem o caso base, a função chamaria a si mesma indefinidamente.  

### 2.2 Passo Recursivo  
O **passo recursivo** reduz o problema maior para um problema menor, permitindo que a função resolva o fatorial de qualquer número inteiro positivo.  

Fórmula geral:

```python  
fatorial(n) = n * fatorial(n-1)  

Exemplo para n = 4:
fatorial(4) = 4 * fatorial(3)
fatorial(3) = 3 * fatorial(2)
fatorial(2) = 2 * fatorial(1)
fatorial(1) = 1 #caso base
```
### 2.3 Rastreio Manual 

**Descida (chamadas recursivas):**  
fatorial(4) → espera fatorial(3)  
fatorial(3) → espera fatorial(2)  
fatorial(2) → espera fatorial(1)  
fatorial(1) = 1   

**Subida (resolvendo cada chamada):**  
fatorial(2) = 2 * 1 = 2  
fatorial(3) = 3 * 2 = 6  
fatorial(4) = 4 * 6 = 24  

**Resultado final:** 24  

## Conclusão

A implementação da função **fatorial recursiva** em Python permitiu compreender de forma prática como a **recursão** atua na decomposição de um problema em partes menores.  
O **caso base** foi essencial para interromper as chamadas sucessivas, evitando uma recursão infinita, enquanto o **passo recursivo** demonstrou como cada etapa depende do resultado anterior.

O rastreio manual mostrou claramente o fluxo de chamadas, a descida até o caso base e a subida com o cálculo dos resultados,reforçando a relação entre o raciocínio matemático e a lógica computacional.  
Portanto, o estudo do fatorial recursivo contribui para consolidar o entendimento da recursão como conceito fundamental em algoritmos e matemática aplicada.





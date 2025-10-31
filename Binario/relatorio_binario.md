
# Universidade Federal de Santa Catarina - UFSC
## Fundamentos Matematicos



<p align="center">
<strong>Daniela T Medeiros</strong>
</p>


<p align="center">
Busca Binária
</p>


<p align="center">
Araranguá
</p>
<p align="center">
2025
</p>


## Resumo 

Este relatório apresenta a implementação da **busca binária** em Python.  
O objetivo é demonstrar como a técnica de **dividir para conquistar** permite encontrar um elemento em uma lista ordenada de forma eficiente.   
O relatório inclui o **rastreio passo a passo das comparações realizadas**, facilitando a compreensão da lógica do algoritmo.  


## Sumário   

1. [Introdução](#introdução)
2. [Desenvolvimento](#desenvolvimento)  
    2.1[Princípio da Busca Binária](#21-princípio-da-busca-binária)  
    2.2[Algoritmo e Passo a Passo](#22-algoritmo-e-passo-a-passo)  
    2.3[Rastreio Manual](#23-rastreio-manual)  

3. [Conclusão](#conclusão)


## Introdução  

A **busca binária** é um dos algoritmos fundamentais utilizados em estruturas de dados e análise matemática de algoritmos.  
Seu princípio baseia-se na técnica de **dividir para conquistar**, reduzindo progressivamente o espaço de busca até localizar o elemento desejado.

Para que o algoritmo funcione corretamente, é necessário que os dados estejam **ordenados**, permitindo eliminar metade do conjunto a cada comparação.  
Dessa forma, o tempo de execução é significativamente menor em relação à busca linear, tornando a busca binária uma ferramenta essencial na resolução de problemas computacionais.

Neste relatório, será apresentada a **implementação da busca binária em Python**, juntamente com o **rastreio detalhado** do processo de execução, com o objetivo de compreender a lógica matemática por trás do algoritmo e sua eficiência.   


## Desenvolvimento

### 2.1 Princípio da Busca Binária

A busca binária baseia-se na divisão sucessiva de uma lista **ordenada**.  
A cada passo, o algoritmo compara o elemento central da lista com o valor procurado (*alvo*).  
Caso sejam iguais, a busca termina; caso contrário, elimina-se metade dos elementos da lista:

- Se o **alvo** for **menor** que o elemento central → busca continua na metade **esquerda**.  
- Se o **alvo** for **maior** → busca continua na metade **direita**.

Esse método segue o princípio matemático da **recorrência**, em que o problema inicial é reduzido a um subproblema menor até alcançar o resultado final.

---

### 2.2 Algoritmo e Passo a Passo

O algoritmo da busca binária foi implementado em Python conforme mostrado a seguir:

```python
def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1
```

## 2.3 Rastreio Manual 

Abaixo está o código com prints explicativos, que permitem acompanhar o funcionamento do algoritmo passo a passo.

```python
def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    print(f"Iniciando busca binária por {alvo} na lista {lista}")

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        print(f"Verificando índice {meio}, valor {lista[meio]}")

        if lista[meio] == alvo:
            print(f"Elemento {alvo} encontrado no índice {meio}")
            return meio
        elif lista[meio] < alvo:
            print(f"{alvo} é maior que {lista[meio]}, buscando à direita")
            esquerda = meio + 1
        else:
            print(f"{alvo} é menor que {lista[meio]}, buscando à esquerda")
            direita = meio - 1

    print(f"Elemento {alvo} não encontrado na lista")
    return -1


numeros = [1, 3, 5, 7, 9, 11]

print("\n--- Teste 1: elemento existente ---")
busca_binaria(numeros, 7)

print("\n--- Teste 2: elemento não existente ---")
busca_binaria(numeros, 2)
```  

Durante a execução, o rastreio exibe mensagens como:

```python
Iniciando busca binária por 7 na lista [1, 3, 5, 7, 9, 11]
Verificando índice 2, valor 5
7 é maior que 5, buscando à direita
Verificando índice 4, valor 9
7 é menor que 9, buscando à esquerda
Verificando índice 3, valor 7
Elemento 7 encontrado no índice 3
```  
Esse rastreio permite visualizar claramente como o algoritmo reduz espaço de busca a cada iteração até encontrar o elemento desejado ou concluir que ele não esta presente na lista.  
  

## Conclusão  

A implementação da **busca binária** demonstrou como a técnica de **dividir para conquistar** reduz significativamente o número de comparações necessárias para localizar um elemento em uma lista ordenada.  

O rastreio manual, com prints explicativos, evidenciou o **fluxo de execução**, mostrando como o intervalo de busca é continuamente ajustado até encontrar o valor desejado ou determinar que ele não está presente.  

Dessa forma, a busca binária se apresenta como uma alternativa muito mais eficiente que a busca linear, especialmente em listas grandes, consolidando conceitos fundamentais de **algoritmos e raciocínio matemático**.  

A experiência de implementação reforçou a compreensão do **processo iterativo**, da importância da **ordenção prévia dos dados** e da aplicação prática de estruturas de controle em Python, permitindo uma análise detalhada do comportamento do algoritmo.



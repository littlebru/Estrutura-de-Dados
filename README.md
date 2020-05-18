<h1>
<img src="https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/tree-structure.png" width="3%;" alt="" title="Mestre Masanori"/>     Estrutura de Dados - Vale a Pena Ordenar?</h1>

![Algoritmo desenvolvido](https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/Algoritmo.gif "Saída do programa")
---
O algoritmo desenvolvido ([EP1.py](https://github.com/littlebru/Estrutura-de-Dados/blob/master/EP1.py)) e ([EP1_timeit](https://github.com/littlebru/Estrutura-de-Dados/blob/master/EP1_timeit.py))tem por objetivo calcular o tempo que as funções de ordenação levam para ordenar listas de **5000**, **10000** e **15000** elementos ou mais (dentro do tempo de 30 segundos de execução), e também calcular quantas buscas são realizadas durante a ordenação dos dados.

> **Obs:** A versão do Python utilizada neste programa é ```3.6```
<br>

## Bibliotecas utilizadas
 
 ##### ``` import time  ```
 Biblioteca que auxilia no manuseio do tempo do sistema, neste programa foi utilizado o método  ``` time.time() ```, ele retorna o tempo em segundos e o método ```process_time()``` que retorna a soma do tempo de execução com o tempo de processamento,e os dois foram utilizados para marcar o tempo de execução de cada função de ordenação e de busca.
 ##### ``` import math  ```
 Biblioteca que permite fazer calculos matematicos e funções de calculo de média por exemplo, neste programa ela foi utilizada para identificar o valor minimo dentro da lista, na função Seleção ``` m = min(v) ```
 ##### ``` import random  ```
 Biblioteca que permite a criação de numeros e listas compostas por numeros aleatórios, neste programa ele foi utilizado para gerar numeros aleatórios com o metodo ```randint``` e embaralhar a lista com o método ```shuffle```.
<br>

## Funções de Ordenação Utilizadas

### ```Seleção```
Realiza a ordenação de uma lista olhando apenas para a Direita, fazendo comparações de elemento por elemento.

<img src="https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/Selecao.gif" width="50%;" alt="" title="Simulação da função Seleção"/>

*Simulação da ordenação da função Seleção*

# 
### ```Inserção```
Realiza a ordenação de uma lista da Esquerda para a Direita, ou seja, pego o elemento da posição atual **B**  e comparo com o elemento seguinte **A**, caso:<br><br>**B < A** (**B** for menor que **A**) -> **B** continua na mesma posição e eu comparo o próximo da lista  com o elemento **A**<br>**A < B** (**A** for menor que **B**) -> **A** troca de posição com **B** e eu pego o próximo da lista e comparo com o **B**

<br><br>
<img src="https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/Insercao.gif" width="40%;" alt="" title="Simulação da função Inserção"/>

*Simulação da ordenação da função Inserção* 

# 
### ```MergeSort``` (dividir, misturar e Intercalar)
Realiza a ordenação de uma lista **A** utilizando um vetor auxiliar **B**, divide a lista em dois e ordena cada pedaço de forma individual, no final reune os dados, formando uma lista novamente tudo isso dentro do vetor **B** auxiliar, depois é enviado para o vetor original **A**.<br>

<img src="https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/MergeSort.gif" width="40%;" alt="" title="Simulação do MergeSort"/>

*Simulação da ordenação da função MergeSort*

# 
### ```QuickSort```
Realiza a ordenação de uma lista com a ajuda de um pivô ou numero de referência para auxiliar na ordenação.
<br><br>
<img src="https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/QuickSort.gif" width="50%;" alt="" title="Simulação do QuickSort"/>

*Simulação da ordenação da função QuickSort*

# 
### ```Sort Nativo```
Função embutida da linguagem Python, realiza a ordenação de uma lista comparando os elementos de maior valor com os elementos seguintes.<br><br>
<img src="https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/TimSort.gif" width="50%;" alt="" title="Simulação do método sort()"/>

*Simulação da ordenação do método Sort*
<br>

## Funções de Busca
No programa também foram utilizados dois algoritmos de busca, para calcular quantas buscas são realizadas durante a ordenação das listas.

### ```Busca Binária```
Realiza a busca de um elemento dividindo a lista ao meio tendo o ponto maximo, o ponto minimo e o ponto médio (ou ponto central) que é o responsável por buscar o elemento procurado.
<br><br>
<img src="https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/Busca_Binaria.gif" width="80%;" alt="" title="Simulação de Busca Binária"/><br>
*Simulação de buscas da função Busca Binária - Buscando pelo numero 714 na demonstração*
#
### ```Busca Sequencial```
Realiza a busca de elemento em elemento dentro da lista, até encontrar o valor procurado.
<br><br>
<img src="https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/Busca_Sequencial.gif" width="80%;" alt="" title="Simulação da Busca Sequencial"/><br>

*Simulação de buscas da função Busca Sequencial - Buscando pelo numero 714 na demonstração*
<br>

## Observações
A função **Seleção** na teoria é a pior de todas, pois ela demanda muito processamento e tem um tempo de ordenação muito lento, porém no algoritmo, podemos visualizar que a **Seleção** esta tendo um *tempo de execução* e *quantidade de buscas* menores do que a **Inserção**.

Isto aconteceu porque no código a função Seleção utiliza uma estrutura auxiliar para procura do menor numero, no método min ``` m = min(v) ```, e a estrutura auxiliar utilizada é chamada de **HEAP**.


### ```Min Heap``` ou ```Binary Heap```
<img src="https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/BinaryHeap.gif" width="90%;" alt="" title="Simulação da estrutura Heap"/>

*Simulação do heap máximo*
<h1>                                                                 </h1>

O Heap Binário é um tipo de estrutura de dados utilizado para ordenar os elementos a medida que são inseridos na estrutura. Assim, ao final das inserções, os elementos podem ser sucessivamente removidos da raiz da heap, na ordem desejada.  

- Um ```heap binário``` é uma árvore binária mantida na forma de um vetor.  

- O ```heap``` é gerado e mantido no próprio vetor a ser ordenado.  

Para uma ordenação crescente, deve ser construído um **heap máximo** (o maior elemento fica na raiz). Para uma ordenação decrescente, deve ser construído um **heap mínimo** (o menor elemento fica na raiz).
<br>

## Bibliografia
- Auxilio do Professor Fernando Masanori

#### Simulações
 * [VisuAlgo](https://visualgo.net/en)
 * [UFSCA.edu](https://www.cs.usfca.edu/~galles/visualization/Search.html)

#### Pesquisas
 * [ufrj - aula 09](https://www.cos.ufrj.br/~rfarias/cos121/aula_09.html)
 * [Doc Python - Timsort](https://docs.python.org/3/howto/sorting.html?highlight=timsort)
 * [Doc Python - time()](https://docs.python.org/3/library/time.html)
 * [Geeks-for-Geeks](https://www.geeksforgeeks.org/python-format-function/)
<br>

## Autora
<table>
  <tr>
    <td align="center"><a href="https://github.com/littlebru"><img src="https://avatars3.githubusercontent.com/u/41810923?s=460&u=c2196ec3a4f76218d7b11bb2a9cf025d2d2e9fdc&v=4" width="70px;" alt="" title="Olha eu ai"/></td>
 </tr>
</table>
 
[Bruna Larissa Clemente Gomes](https://github.com/littlebru)<br>
3º Semestre - Análise e Desenvolvimento de Sistemas-**FATEC São José dos Campos 2020**

## Orientador
<table>
  <tr>
    <td align="center"><a href="https://github.com/fmasanori"><img src="https://avatars1.githubusercontent.com/u/977887?s=460&u=d68c50c6ac3f2845bbb48efff7c37742d3a010d0&v=4" width="70px;" alt="" title="Mestre Masanori"/></td>
  </tr>
</table>

 [Fernando Masanori Ashikaga](https://github.com/fmasanori)

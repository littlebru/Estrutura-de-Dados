# Estrutura de Dados - Vale a Pena Ordenar? :1234:
Este programa tem como objetivo calcular o tempo que as funções de ordenação levam para ordenar listas de **10000**, **20000** e **30000** elementos em sua composição.


## Funções de Ordenação Utilizadas

### Seleção
Realiza a ordenação de uma lista da Esquerda para a Direita, ou seja, pego o elemento da posição atual **A**  e comparo com o elemento seguinte **B**, caso:<br><br>**A < B** (**A** for menor que **B**) -> **A** continua na mesma posição e eu comparo o elemento **B** com o próximo da lista<br>**B < A** (**B** for menor que **A**) -> **B** troca de posição com **A** e eu comparo com o próximo da lista

![Simulação Seleção](https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/Selecao.gif)<br>
*Simulação da ordenação da função Seleção*

### Inserção
Realiza a ordenação de uma lista olhando apenas para a Direita, fazendo comparações de elemento por elemento.<br><br>**A** compara com **B**<br>**A** compara com **C**<br>**A** compara com **D**<br>
.
.
.

![Simulação Inserção](https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/Insercao.gif)<br>                            *Simulação da ordenação da função Inserção* 

### MergeSort (dividir, misturar e Intercalar)
Realiza a ordenação de uma lista **A** utilizando um vetor auxiliar **B**, divide a lista em dois e ordena cada pedaço de forma individual, no final reune os dados, formando uma lista novamente tudo isso dentro do vetor **B** auxiliar, depois é enviado para o vetor original **A**.<br>

![Simulação MergeSort](https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/MergeSort.gif)<br>
*Simulação da ordenação da função MergeSort*

### QuickSort
Realiza a ordenação de uma lista com a ajuda de um pivô ou numero de referência para auxiliar na ordenação.<br><br>
![Simulação Inserção](https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/QuickSort.gif)<br>
*Simulação da ordenação da função QuickSort*

### Sort Nativo
Função embutida da linguagem Python, realiza a ordenação de uma lista comparando os elementos de maior valor com os elementos seguintes.<br><br>
![Simulação SortNativo](https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/TimSort.gif)<br>
*Simulação da ordenação do método Sort*

## Funções de Busca
No programa também foram utilizados dois algoritmos de busca, para calcular quantas buscas são realizadas durante a ordenação das listas.

### Busca Binária
Realiza a busca de um elemento dividindo a lista em pares<br>
![Simulação Busca Binária](https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/Busca_Binaria.gif)<br>
*Simulação de buscas da função Busca Binária - Buscando pelo numero 714 na demonstração*

### Busca Sequencial
Realiza a busca de um elemento procurando de elemento por elemento<br>
![Simulação Busca Sequencial](https://github.com/littlebru/Estrutura-de-Dados/blob/master/simulacoes/Busca_Sequencial.gif)<br>
*Simulação de buscas da função Busca Sequencial - Buscando pelo numero 714 na demonstração*

------

## Bibliotecas utilizadas
 
 ##### ``` import time  ```
 Biblioteca que auxilia no manuseio do tempo do sistema, neste programa foi utilizado o comando  ``` time.time() ```, ele retorna o tempo em segundos, foi utilizado para marcar o tempo de execução de cada função de ordenação e de busca.
 ##### ``` import math  ```
 Biblioteca que permite fazer calculos matematicos e funções de calculo de média por exemplo, neste programa ela foi utilizada para identificar o valor minimo dentro da lista, na função Seleção ``` m = min(v) ```
 ##### ``` import random  ```
 Biblioteca que permite a criação de numeros e listas compostas por numeros aleatórios, neste programa ele foi utilizado para gerar numeros aleatórios. 

###### *Comando dentro da função Principal*
 ``` numero = randint(1,qtd_elementos) ``` <br> 
###### *Embaralhando a lista com o método shuffle*
 ``` shuffle(lista)``` <br> 
 ###### *Contagem de um numero x até y-1*
 ``` range(x, y-1) ``` <br>
 
------

## Autor
[Bruna Larissa Clemente Gomes](https://github.com/littlebru)<br>
Análise e Desenvolvimento de Sistemas<br>
**3º Semestre - 2020**<br>
## Orientador
[Fernando Masanori](https://github.com/fmasanori)

------
 
## Bibliografia

#### Simulações
As simulações foram realizadas nas plataformas:
- [VisuAlgo](https://visualgo.net/bn/sorting)
- [UFSCA.edu](https://www.cs.usfca.edu/~galles/visualization/Search.html)

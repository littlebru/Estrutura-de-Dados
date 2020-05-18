# EP1 utilizando a biblioteca timeit para calcular o tempo das funções

# Importanto bibliotecas

import math
from random import random
from random import randint
from random import shuffle
from time import time
from timeit import timeit


# -- Função Principal -------------------------
def principal():

  cabecalho()

  inicio = time()             # Tempo inicial do programa
  fim = time()                # Tempo final do programa

  qtd_elementos = 5000        # Quantidade de elementos para ordenar
  
  while(fim - inicio <= 100):  # Previsão de 30 segundos de execução

    tempos_ordenacao = []       # tempo das funções de ordenação
    buscas_totais = []          # quantidade de buscas feitas pelas funcoes

    lista_original = gera_lista_embaralhada(qtd_elementos)  # Gerando lista embaralhada
    lista_copia = lista_original.copy()                    # Lista que sera ordenada

    tempos_ordenacao = calcula_tempo_ordenacao(lista_copia)

    for tempo in tempos_ordenacao:
      buscas = calcula_buscas(tempo, lista_original, lista_copia, qtd_elementos)
      buscas_totais.append(buscas)

    imprime_resultados(qtd_elementos, tempos_ordenacao, buscas_totais)    # Imprimindo resultados obtidos

    qtd_elementos += 5000     # Acrescentando mais 5000 elementos

    fim = time()      # Armazenando tempo do fim do algoritmo

  print('|----------------------------------------------------------------------------------------------------|')


def calcula_tempo_ordenacao(lista):
  funcoes = ['insercao', 'selecao', 'mergesort', 'quicksort','sort_nativo'] # Funções de ordenação
  tempos = []

  for f in funcoes:
    tempos.append(timeit(f"{f}({lista})", setup=f"from  __main__ import {f}", number = 1)) # Armazenando tempo de execução das funções

  return tempos     # retornando lista com o tempo de todas as funções


def calcula_tempo_buscas(funcao, lista):
  return timeit(f"{funcao}({lista})", setup=f"from  __main__ import {funcao}")

def calcula_buscas(tempo_ordenacao, lista_embaralhada, lista_ordenada, qtd_elementos):
  qtd_buscas = 0
  tempo_binaria = 0
  tempo_sequencial = 0
  tempo_total = 0
  
  while(tempo_total < tempo_ordenacao):
    
    num_aleatorio = randint(1,qtd_elementos)  # Gerando um numero aleatorio
    
    tempo_binaria += timeit(f"busca_binaria({lista_ordenada}, {num_aleatorio})", setup="from  __main__ import busca_binaria", number=1)
    tempo_sequencial += timeit(f"busca_sequencial({lista_embaralhada}, {num_aleatorio})", setup="from  __main__ import busca_sequencial", number=1)

    qtd_buscas += 1
    
    tempo_total = tempo_total + (tempo_sequencial + tempo_binaria)

  return qtd_buscas


# ----------------- Funções de Ordenação -------------------

# Função: Ordena comparando valores da esquerda para a direita

def insercao(v):
  for j in range(1, len(v)):
    x = v[j]
    i = j - 1
    while i >= 0 and v[i] > x:
      v[i+1] = v[i]
      i = i - 1
    v[i + 1] = x
  return v


# Função: Ordena comparando o valor atual com os valores a frente

def selecao(v):
  r = []
  while v:
    m = v[0]
    for num in v:
      if num < m: m = num     # Armazenando o menor numero
    r.append(m)
    v.remove(m)
  return r


# Função: Ordena a lista com paralelismo utilizando um vetor auxiliar

def mergesort(v):
    if len(v) <= 1: return v  #Pior caso: Vetor com poucos elementos
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

def merge(e, d):
    r = []          # vetor auxiliar
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r



# Função: Ordena as lista com o auxilio de um pivô

def quicksort(v):
    if len(v) <= 1: # Pior caso: Se vetor ja estiver ordenado
      return v
    pivô = v[0] 
    iguais  = [x for x in v if x == pivô]
    menores = [x for x in v if x <  pivô]
    maiores = [x for x in v if x >  pivô]
    return quicksort(menores) + iguais + quicksort(maiores)



# Função nativa da linguagem para ordenação de listas

def sort_nativo(v):
  v.sort()
  return v


# ----------------- Funções de Buscas -------------------

# Função: Busca por um elemento dividindo a lista

cont = 0
def busca_binaria(v, x):
  global cont
  e = -1
  d = len(v)
  while e < d-1:
    m = (e + d) // 2
    cont = cont + 1
    if v[m] < x:
      e = m
    else:
      d = m
  return d


# Função: Busca de elemento por elemento

i = 0
def busca_sequencial(v, x):
  global i
  # Percorrendo a lista
  while i < len(v):
    if v[i] == x:
      return i
    i += 1
  return -1

    
# --------------------------------------------------------

# Função: Gera uma lista com os elementos embaralhados
def gera_lista_embaralhada(elementos):
  lista = list(range(1,elementos))
  shuffle(lista)
  return lista

# Função: Imprime cabeçalho do programa
def cabecalho():
    print()
    print('|------------------------------------[EP1 - Vale a pena ordenar?]------------------------------------|')
    print('|                Aluna: Bruna Larissa Clemente Gomes - FATEC Sao Jose dos Campos                     |')
    print('|                Disciplina: Estrutura de Dados                  Turma: ADS - 3º Semestre B          |')
    print('|                Algoritmo escolhido:   Todos                    Duracao dos testes:   30.00s        |')
    print('|                                                                                                    |')
    print('|                       Tempos de Ordenacao                          Numero de Buscas                |')
    print('|----------------------------------------------------------------------------------------------------|')
    print('|     n     | Insercao   Selecao   Merge.   Quick.   Sort  |  Insercao Selecao  Merge.  Quick.  Sort |')
    print('|----------------------------------------------------------------------------------------------------|')



# Função: Imprimindo resultados em formato tabela
def imprime_resultados(qtd_elementos, lista_de_tempo, lista_de_buscas):

  # caso o numero de elementos esteja entre 0 - 9999
  if len(str(qtd_elementos)) < 5 :
    if len(str(lista_de_buscas[1])) < 3:
      print(f'|       {qtd_elementos}|   {lista_de_tempo[0]:.2f}     {lista_de_tempo[1]:.2f}      {lista_de_tempo[2]:.2f}     {lista_de_tempo[3]:.2f}     {lista_de_tempo[4]:.2f}  |   {lista_de_buscas[0]}       {lista_de_buscas[1]}       {lista_de_buscas[2]}       {lista_de_buscas[3]}     {lista_de_buscas[4]}  |')
    else:
      print(f'|       {qtd_elementos}|   {lista_de_tempo[0]:.2f}     {lista_de_tempo[1]:.2f}      {lista_de_tempo[2]:.2f}     {lista_de_tempo[3]:.2f}     {lista_de_tempo[4]:.2f}  |   {lista_de_buscas[0]}      {lista_de_buscas[1]}       {lista_de_buscas[2]}       {lista_de_buscas[3]}     {lista_de_buscas[4]}  |')

  # caso o numero de elementos seja maior que 9999
  if len(str(qtd_elementos)) >= 5 : 
    
    # Caso: o resultado de buscas tenha mais de 3 digitos
    if len(str(lista_de_buscas[0]) and str(lista_de_buscas[1])) == 3:   

      if lista_de_tempo[0] < 10.0:
        print(f'|      {qtd_elementos}|   {lista_de_tempo[0]:.2f}     {lista_de_tempo[1]:.2f}      {lista_de_tempo[2]:.2f}     {lista_de_tempo[3]:.2f}     {lista_de_tempo[4]:.2f}  |   {lista_de_buscas[0]}      {lista_de_buscas[1]}       {lista_de_buscas[2]}       {lista_de_buscas[3]}     {lista_de_buscas[4]}  |')

      elif lista_de_tempo[0] > 10.0:
        print(f'|      {qtd_elementos}|   {lista_de_tempo[0]:.2f}    {lista_de_tempo[1]:.2f}      {lista_de_tempo[2]:.2f}     {lista_de_tempo[3]:.2f}     {lista_de_tempo[4]:.2f}  |   {lista_de_buscas[0]}      {lista_de_buscas[1]}       {lista_de_buscas[2]}       {lista_de_buscas[3]}     {lista_de_buscas[4]}  |')





# Iniciando o programa
principal()

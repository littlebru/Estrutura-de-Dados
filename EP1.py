# Importando bibliotecas
from random import randint
from random import random
from random import shuffle
from time import process_time
from time import time
import math

# -- Função Principal-----------------------------

def principal():

  # Marcadores de tempo de execução do programa
  tempo_exec_inicial = time()
  tempo_exec_final = time()

  lista_de_tempo = [0,0,0,0,0]  # Armazena tempo das funções
  lista_de_buscas = [0,0,0,0,0] # Armazena numero de buscas das funções

# Funções utilizadas
  funcoes_ordenacao = ['insercao','selecao','mergesort','quicksort','sortNativo'] 
# Numero inicial de elementos
  qtd_elementos = 5000  

# Imprimindo o cabeçalho
  cabecalho()
  
# Tempo limite de 30 segundos
  while((tempo_exec_final - tempo_exec_inicial) < 30):  
    
# Gerando lista embaralhada
    lista_original = lista_aleatoria(qtd_elementos)
# Gerando uma cópia da lista
    lista_copia = lista_original.copy()
    
    for posicao in range(0,5):
      
    # Pegando uma função da lista
      funcao = funcoes_ordenacao[posicao]
     
    # Calculando e armazenando o tempo de ordenação da função
      tempo_ordenacao = cronometro_ordenacao(funcao, lista_copia)
      lista_de_tempo[posicao] = tempo_ordenacao
      
    # Calculando numero de buscas da função
      total_busca = quantidade_buscas(lista_original, lista_copia, tempo_ordenacao, qtd_elementos)
      lista_de_buscas[posicao] = total_busca
    
    # Marcador de tempo
      tempo_exec_final = time() 

    # Imprimindo os resultados
    imprime_resultados(qtd_elementos, lista_de_tempo, lista_de_buscas)  
    
    # Adicionando mais elementos a lista
    qtd_elementos += 5000

  print('|----------------------------------------------------------------------------------------------------|')


# ----------------- Funções de Cronometragem -----------------


# Função: Calcula o tempo de ordenação

def cronometro_ordenacao(funcao, lista):
  tempo_inicial = process_time()
  exec(f'{funcao}({lista})')    # Executando a função
  tempo_final = process_time()
      
  return (tempo_final - tempo_inicial)    # Retornando o tempo de execução


# Função: Calcula o tempo de buscas  

def cronometra_busca(funcao,lista, numero):
  tempo_inicial = process_time()
  exec(f'{funcao}({lista}, {numero})')  # Executando a função
  tempo_final = process_time()
  
  return (tempo_final - tempo_inicial)    # Retornando o tempo de execução



# --------------- Função de Contagem de Buscas --------------

def quantidade_buscas(lista_original, lista_copia, tempo_ordenacao, qtd_elementos):
  funcoes_busca = ['busca_binaria','busca_sequencial']
  qtd_buscas = 0
  tempo_binaria = 0
  tempo_sequencial = 0

  while(tempo_sequencial <= tempo_ordenacao):
    
    numero_aleatorio = randint(1,qtd_elementos)  # Gerando um numero aleatorio
    
    # Calculando tempo de busca das funções
    tempo_binaria = tempo_binaria + cronometra_busca(funcoes_busca[0], lista_original, numero_aleatorio)
    tempo_sequencial = tempo_sequencial + cronometra_busca(funcoes_busca[1], lista_copia, numero_aleatorio)

    # Contagem de buscas
    qtd_buscas += 1

  return qtd_buscas

# ----------------- Função Gera Listas --------------

# Função: Gera lista embaralhada

def lista_aleatoria(num_elementos):
  lista = list(range(1,num_elementos)) # Gerando uma lista ordenada

  shuffle(lista)    # Embaralhando a lista
  return lista


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
    m = min(v)
    r.append(m)
    v.remove(m)
  return r


# Função: Ordena a lista com paralelismo utilizando um vetor auxiliar

def mergesort(v):
    if len(v) <= 1: return v  #Pior caso: Vetor ja estiver ordenado
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

def sortNativo(v):
  sorted(v)


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

# ----------- Cabeçalho da Aplicação -----------------------
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



# Função: imprime resultados com texto formatado

def imprime_resultados(qtd_elementos, lista_de_tempo, lista_de_buscas):

  # caso o numero de elementos esteja entre 0 - 9999
  if len(str(qtd_elementos)) < 5 :  
    print(f'|       {qtd_elementos}|   {lista_de_tempo[0]:.2f}      {lista_de_tempo[1]:.2f}      {lista_de_tempo[2]:.2f}     {lista_de_tempo[3]:.2f}     {lista_de_tempo[4]:.2f} |     {lista_de_buscas[0]}      {lista_de_buscas[1]}       {lista_de_buscas[2]}       {lista_de_buscas[3]}     {lista_de_buscas[4]}   |')

  # caso o numero de elementos seja maior que 9999
  if len(str(qtd_elementos)) >= 5 : 
    
    # Caso: o resultado de buscas tenha mais de 3 digitos
    if len(str(lista_de_buscas[0]) and str(lista_de_buscas[1])) >= 3:   
      print(f'|      {qtd_elementos}|   {lista_de_tempo[0]:.2f}      {lista_de_tempo[1]:.2f}      {lista_de_tempo[2]:.2f}     {lista_de_tempo[3]:.2f}     {lista_de_tempo[4]:.2f} |     {lista_de_buscas[0]}      {lista_de_buscas[1]}      {lista_de_buscas[2]}       {lista_de_buscas[3]}     {lista_de_buscas[4]}   |')
    
    #Caso o resultado de buscas tenha menos de 3 digitos
    else:   
      print(f'|      {qtd_elementos}|   {lista_de_tempo[0]:.2f}      {lista_de_tempo[1]:.2f}      {lista_de_tempo[2]:.2f}     {lista_de_tempo[3]:.2f}     {lista_de_tempo[4]:.2f} |     {lista_de_buscas[0]}      {lista_de_buscas[1]}       {lista_de_buscas[2]}       {lista_de_buscas[3]}     {lista_de_buscas[4]}   |')



# --------------------------------------------------------

# Iniciando programa
principal()

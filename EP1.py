# Importando bibliotecas
from random import randint
from random import random
from random import shuffle
import time
import math

# -- Função Principal-----------------------------
def principal():
  
  # Declarando variaveis globais
  global v_tempo
  global v_buscas
  global funcoes_ordenacao
  global qtd_elementos
  global tempo_inicial
  global tempo_final

  # Inicializando variaveis
  v_tempo = [0,0,0,0,0]
  v_buscas = [0,0,0,0,0]
  funcoes_ordenacao = ['insercao','selecao','mergesort','quicksort','sortNativo']
  qtd_elementos = 10000


  cabecalho()     # Imprimindo o cabeçalho
  
  
  while(qtd_elementos <= 30000):

    # Marcadores de tempo
    tempo_total = 0
    tempo_inicial = time.time()
    tempo_final = time.time()
    
    while(tempo_final - tempo_inicial < 0.30): #duração de 30 segundos
      
      lista_al = lista_aleatoria(qtd_elementos)    # Gerando lista embaralhada
      numero = randint(1,qtd_elementos)            # Gerando um numero aleatorio
      
      for posicao in range(0,5):
        
        funcao = funcoes_ordenacao[posicao]       # Pegando uma função da lista
        
        # -- Calculando e armazenando o tempo de ordenação da função
        tempo_total = cronometro_ordenacao(funcao,lista_al)
        v_tempo[posicao] = tempo_total
        
        
        # -- Calculando numero de buscas da função
        total_busca = quantidade_buscas(qtd_elementos, numero, tempo_total)
        v_buscas[posicao] = total_busca
        
        tempo_final = time.time()
  
    print(f'|   {qtd_elementos}    |   {v_tempo[0]:.2f}     {v_tempo[1]:.2f}     {v_tempo[2]:.2f}     {v_tempo[3]:.2f}     {v_tempo[4]:.2f}  |     {v_buscas[0]}     {v_buscas[1]}       {v_buscas[2]}       {v_buscas[3]}     {v_buscas[4]}   |')
    
    qtd_elementos += 10000

  print('|------------------------------------------------------------------------------------------------|')

# ----------- Cabeçalho da Aplicação -----------------------
def cabecalho():
    print()
    print('|-------------------------------------[EP1 - Vale a pena ordenar?]------------------------------------|')
    print('|                 Aluna: Bruna Larissa Clemente Gomes - FATEC Sao Jose dos Campos                     |')
    print('|                 Disciplina: Estrutura de Dados                  Turma: ADS - 3º Semestre B          |')
    print('|                 Algoritmo escolhido:   Todos                    Duracao dos testes:    30.00        |')
    print('|                                                                                                     |')
    print('|                        Tempos de Ordenacao                          Numero de Buscas                |')
    print('|-----------------------------------------------------------------------------------------------------|')
    print('|     n      | Insercao   Selecao   Merge.   Quick.   Sort  |  Insercao Selecao  Merge.  Quick.  Sort |')
    print('|-----------------------------------------------------------------------------------------------------|')



# ----------------- Funções Geradoras de Listas --------------


# Função: Gera lista embaralhada
def lista_aleatoria(num_elementos):
  lista = list(range(1,num_elementos)) # Gerando uma lista ordenada
  shuffle(lista)    # Embaralhando a lista
  return lista


# ----------------- Funções de Cronometragem -----------------


# Função: Calcula o tempo de ordenação
def cronometro_ordenacao(funcao, lista):
  tempo_inicial = time.time()
  exec(f'{funcao}({lista})')    # Executando a função
  tempo_final = time.time()
      
  return (tempo_final - tempo_inicial)    # Retornando o tempo de execução


# Função: Calcula o tempo de buscas      
def cronometra_busca(funcao,lista, numero):
  tempo_inicial = time.time()
  exec(f'{funcao}({lista}, {numero})')
  tempo_final = time.time()
  
  return (tempo_final - tempo_inicial)    # Retornando o tempo de execução



# --------------- Função de Contagem de Buscas --------------

def quantidade_buscas(elementos, num, tempo_ordenacao):
  lista = list(range(1,elementos))
  funcoes_busca = ['busca_binaria','busca_sequencial']
  qtd_buscas = 0
  tempo_binaria = 0     # Tempo total busca_binaria
  tempo_sequencial = 0  # Tempo total busca_sequencial

  while(tempo_sequencial < tempo_ordenacao):
    
    tempo_binaria = tempo_binaria + cronometra_busca(funcoes_busca[0], lista, num)
    tempo_sequencial = tempo_sequencial + cronometra_busca(funcoes_busca[1], lista, num)
    
    qtd_buscas += 1
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
    r = []
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

# Iniciando programa
principal()

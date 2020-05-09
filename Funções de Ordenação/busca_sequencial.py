i = 0
def busca_sequencial(v, x):
  global i
  # Percorrendo a lista
  while i < len(v):
    if v[i] == x:
      return i
    i += 1
  return -1

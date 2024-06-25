def obter_valor(atual: int, anterior:int):
  if atual % 2 == 0:
    return atual + anterior

  return atual - anterior


def transformar_lista(n: int) -> int:
   if n % 2 == 0:
      return n + 2

   return n - 1

def retornar_lista(entrada: list) -> list:
    saida = []

    for i, n in enumerate(entrada):
      if i == 0:
        valor = obter_primer


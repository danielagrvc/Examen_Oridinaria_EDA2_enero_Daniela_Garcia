
def usar_la_fuerza(mochila):
      # Si la mochila está vacía, no hay más objetos que sacar
  if not mochila:
    return False, 0
  # Sacar el primer objeto de la mochila
  objeto = mochila.pop(0)
  # Si el objeto es un sable de luz, retornar True y el número de objetos necesarios para encontrarlo
  if objeto == "sable de luz":
    return True, len(mochila)
  # Si no es un sable de luz, seguir buscando en la mochila
  return usar_la_fuerza(mochila)

mochila = ["armas", "sable de luz", "monedas", "cuchillo"]
encontrado, objetos_sacados = usar_la_fuerza(mochila)

if encontrado:
  print(f"Se encontró el sable de luz después de sacar {objetos_sacados} objetos de la mochila")
else:
  print("No se encontró el sable de luz en la mochila")

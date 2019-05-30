# -*- coding: utf-8 -*-

""" Caída """
""" Un programita"""

print("Estamos ante un pozo.")
print("Queremos saber qué tan profundo es.")
print("Lanzamos una piedra...")
t = int(input("¿Cuántos segundos tardó en caer? "))

g = 10 # aceleración gravitacional
# 10 metros por segundo cada segundo

s = (g * (t ** 2)) * .5

# donde s es profundidad, t, tiempo
# y g (gravedad)

print("El pozo tiene ", int(s), " metros de profundidad.")

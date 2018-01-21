import math

def pozicija(x, y, r, koordinate):
    for fi in range (360):
        seznam = []
        x = lokacijax
        y = lokacijay
        y += math.sin(math.radians(fi)) * r
        x += math.cos(math.radians(fi)) * r
        seznam.append((x))
        seznam.append((y))
        koordinate.append(seznam)
        print(seznam)
    return koordinate 

t = int(input("Vstavi čas:"))
r = t 
lokacijax = 0
lokacijay = 0
koordinate1 = []
pozicija (lokacijax, lokacijay, r, koordinate1)

r = t 
lokacijax = 10
lokacijay = 10
koordinate2 = []
print("DRUGI MIKROFON")
pozicija (lokacijax, lokacijay, r, koordinate2)
for element in koordinate1:
    if element in koordinate2:
        print(element)

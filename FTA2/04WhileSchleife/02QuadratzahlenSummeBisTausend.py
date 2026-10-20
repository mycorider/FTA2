# Aufgabe 2:
#
# Gib aus, wie viele unterschiedliche Quadratzahlen
# beginnend bei 1 aufsummiert werden können, damit die Summe
# 1000 nicht überschreitet.
# Gib sowohl die Summe als auch die letzte Quadratzahl aus.

# Wir definieren unsere Laufzahl
i = 1

# Wir definieren unsere Grenze
grenze = 1000

# wir definiere unsere Summe
summe = 0

# Summiere solange summe kleiner grenze
while (summe + i*i) < grenze:
    summe = summe + i*i
    i = i + 1

print(summe)
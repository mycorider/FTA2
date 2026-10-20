# Aufgabe 1:
#
# Erzeuge folgende ausgabe mit Hilfe einer Schleifenstruktur.
# Es darf nur 1 Schleife verwendet werden.

# Wir setzen zu Beginn x auf 1
x = 1

# In der Variable y legen wir den Wert ab, der aufaddiert wird.
y = 1

# Wiederhole solange x > 0
while x > 0:
    print(x, end=" ")

    # Wenn x identisch mit dem Wert 5 ist
    # setze y auf -1. 
    # Die Konsequenz ist ein Herunterzählen

    if x == 5:
        y = -1

    x = x + y

print()
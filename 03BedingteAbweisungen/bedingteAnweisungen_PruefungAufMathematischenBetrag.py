# Beispiel: Ausgabe des mathematischen Betrags einer Zahl
#                                      
# 1. Schritt: Eingabe des Wertes

wert = int(input("Bitte gib einen Wert ein: "))

# 2. Schritt: Wir prüfen, ob die Zahl negativ ist

if wert < 0:
    wert = wert *(-1)

# 3. Schritt: Ausgabe des mathematischen Betrages

print("Der mathematische Betrag lautet " + str(wert))


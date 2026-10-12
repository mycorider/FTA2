# Aufgabe 1:
#
# Erstelle ein Programm, das überprüft, ob eine eingegebene Zahl positiv oder
# negativ ist. Gib dies als Meldung aus.

# Wir lesen von Benutzer eine Ganzzahl ein:

# 1. input erwartet eine Benutzereingabe in der Codierung
#    als Zeichenkette
#
# 2. int wandelt die Benutzereingabe in eine Ganzzahl um.
#
# 3. Die als Ganzzahl umgewandelte Information wird der
#    Speicherstelle eingabe zugewiesen.

eingabe = int(input("Geben Sie eine Ganzzahl ein: "))

# Wir definieren die Meldung vor
#
meldung = "Die eingegebene Zahl ist "
wertung = "positiv"

# Wir prüfen, ob die Zahl negativ ist

if eingabe < 0:
    wertung = "negativ"

# Wir konstruieren die Ausgabe

print(meldung + wertung)

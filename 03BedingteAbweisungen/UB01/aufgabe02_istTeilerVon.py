# Aufgabe 2:
#
# Erstelle ein Programm, das zwei Zahlen einliest und ausgibt, ob die zweite Zahl ein
# Teiler der ersten Zahl ist.
#
# Wir lesen die erste Zahl ein:
#
eingabe = int(input("Geben Sie einen ersten Wert ein: "))
#
# Wir lesen den Teiler ein
#
teiler = int(input("Geben Sie nun den Teiler ein: "))
#
# Wir definieren die Ausgabe und behaupten, dass die zweite Zahl ein Teiler der
# ersten eingegebenen Zahl ist.
#
meldung = str(teiler) + " ist kein Teiler von " + str(eingabe)
#
# Wir überprüfen unsere Behauptung, indem wir mit Hilfe des Restwertoperators % auf einen
# Divisionsrest von 0 prüfen
# 
if eingabe%teiler==0:
    meldung = str(teiler) + " ist ein Teiler von " + str(eingabe)

# ...und geben das Ergebnis der Auswertung aus:

print(meldung)
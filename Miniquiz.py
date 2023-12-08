#Miniquiz

punkte = 0


def quiz():
    global punkte
    antwort = input(frage)
    if antwort == loesung:
        print("Das ist richtig!")
        punkte= punkte + 1
    else:
        print("Das ist leider falsch")
        print("Richtig wäre: ", loesung)

frage = "Welche Programmiersprache lernen wir gerade?"
loesung= "Python"
quiz()

frage = "Welchen Befehl brauch man um einen Variablenwert in einer Funktion aufzurufen?"
loesung = "global"
quiz()

frage = "Ist elif ein resaviertes Wort?"
loesung = "Ja"
quiz()

if punkte == 3:
    print("Du hast die maximale Punktzahl erreicht! Super!")
elif punkte > 0:
    print("Du hast", punkte, "von 3 möglichen Punkten erreicht!")
else:
    print("Leider hast du keine Punkte! Lerne nächstes mal ein bisschen mehr!")
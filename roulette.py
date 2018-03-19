import random

a = int(input('Wie hoch ist dein Budget? '))
h = int(input('Auf wieviele Felder der insgesamt 37 willst du setzen? '))
b = int(input('Wie hoch ist dein Einsatz pro Feld? '))
x = int(input('Wieviele Durchläufe soll es geben? '))
t = (input('Ab welchem erreichten Guthaben willst du das Spiel verlassen? (Falls gar nicht, lasse dieses Feld leer) '))

print()
print()


# Damit die Anz. der zu besetzenden Felder in der Variable j konstant festgehalten wird  (u. nicht durch untere while-Schleife verändert)

j = h
BudgetAnfang = a

gespielteDurchlaeufe = 0


Budget = a


while x > 0:
    x = x - 1

    gespielteDurchlaeufe = gespielteDurchlaeufe + 1

    # für while-Schleife
    k = 0





    print('##### RUNDE ' + str(gespielteDurchlaeufe) + ' #####')
    print()


    number = random.randint(0,36)
    print('Gezogene Zahl: ' + str(number))

    print()


    liste = list(range(0,37))

    h = j

    while h < 37:

        del liste[random.randint(0,(36 - k))]

        # h = Eingabe: wieviele Felder sind zu besetzen
        h = h + 1

        # es muss immer eine um 1 größere Zahl abgezogen werden, weil die Anz. der Elemente aus der Liste imer um 1 weniger wird
        k = k + 1




    if len(liste) == 1:
        print('Deine Zahl:')
    else: print('Deine ' + str(len(liste)) + ' Zahlen:')

    print(liste)


    if number in liste:
        print('Treffer.')
    else: print ('Leider daneben.')



    Einsatz = b

    if number in liste:
        Budget = Budget - j*b + b*36
    else: Budget = Budget - j*b

    print('Aktuelles Guthaben: ' + str(Budget))
    print()
    print()

    if t != str(''):
        if Budget >= int(t):
            print('Das als Ziel markierte Guthaben wurde erreicht. Du hast das Spiel verlassen.')
            break


    if Budget < j*b:
        print('Du hast ' + str(gespielteDurchlaeufe) + ' Durchläufe gespielt und hast nun zu wenig Geld für den nächsten Einsatz.')
        break

print()
print('Das Anfangsbudget war: ' + str(BudgetAnfang))

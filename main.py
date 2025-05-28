import random

SZEKEK_SZAMA = 8

def udvozlo_uzenet(szekek):
    print(f"Üdvözöllek a mozi székfoglaló felületén! Összes szék: {SZEKEK_SZAMA}. Rendelkezésre álló székek száma: {szekek.count(0)}")
    print("🟩: Szabadon foglalható hely\n🔴: Foglalt hely\n⬛: Oszlop, itt nincsen szék.", end="\n\n")

def szekek_kiiras(szekek):
    print("Székek:") 
    for szek in szekek:
        if szek == 0:
            print('🟩', end=' ')
        elif szek == 1:
            print('🔴', end=' ')
        else:
            print('⬛', end=' ')
    print()

def helyes_e(szekek, foglalt, oszlop):
    if not (1 <= foglalt <= 8):
        print("Helytelen bevitel. Próbáld újra.")
        return False
    elif szekek[foglalt - 1] == 2:
        print("Itt nincsen szék. Próbálj meg máshol széket foglalni.")
        return False
    elif szekek[foglalt - 1] == 1:
        print("Ez a szék már foglalt. Próbáld meg más széket foglalni.")
        return False
    elif (foglalt == 2 and szekek[0] != 1) or (foglalt == 7 and szekek[SZEKEK_SZAMA - 1] != 1):
        print("A szélső két széket nem hagyhatod szabadon. Kérlek próbálj meg ennek megfelelően foglalni.")
    else:
        return True

def foglalas_bekeres(szekek, oszlop):
    foglalt_szek = int(input('Hányadik széket szeretnéd lefoglalni? [1-8]: '))

    while not helyes_e(szekek, foglalt_szek, oszlop):
        foglalt_szek = int(input('Hányadik széket szeretnéd lefoglalni? [1-8]: '))

    return foglalt_szek

def foglalas_feldolgozas(szekek, foglalt):
    szekek_foglalassal = szekek
    szekek_foglalassal[foglalt - 1] = 1

    return szekek_foglalassal

def main():
    foglalas = True
    szekek_lista = [0 for _ in range(SZEKEK_SZAMA)]
    oszlop = random.randint(0, SZEKEK_SZAMA - 1)
    szekek_lista[oszlop] = 2

    udvozlo_uzenet(szekek_lista)
    
    szekek_kiiras(szekek_lista)

    while foglalas:
        foglalt_szek = foglalas_bekeres(szekek_lista, oszlop)
        szekek_lista = foglalas_feldolgozas(szekek_lista, foglalt_szek)
        print(f"Rendben, lefoglaltam neked a {foglalt_szek}. széket.")
        szekek_kiiras(szekek_lista)

        uj_foglalas = input("Szeretnél mégegy széket foglalni? [i ; n]: ")

        if uj_foglalas == 'n':
            foglalas = False

    print("Köszönöm, hogy foglaltál széket!")


main()

SZEKEK_SZAMA = 8

def udvozlo_uzenet(szekek):
    print(f"Üdvözöllek a mozi székfoglaló felületén! Összes szék: {SZEKEK_SZAMA}. Rendelkezésre álló székek száma: {szekek.count(0)}")
    print("🟩: Szabadon foglalható hely\n🔴: Foglalt hely.", end="\n\n")

def szekek_kiiras(szekek):
    print("Székek:") 
    for szek in szekek:
        if szek == 0:
            print('🟩', end=' ')
        else:
            print('🔴', end=' ')
    print()

def foglalas_bekeres(szekek):
    foglalt_szek = int(input('Hányadik széket szeretnéd lefoglalni? [1-8]: '))

    while not (1 <= foglalt_szek <= 8 and szekek[foglalt_szek - 1] == 0):
        if not (1 <= foglalt_szek <= 8):
            print("Érvénytelen bevitel, próbáld újra.")
        elif szekek[foglalt_szek - 1] == 1:
            print("Ez a szék már foglald. Próbálj meg más széket foglalni.")
        foglalt_szek = int(input('Hányadik széket szeretnéd lefoglalni? [1-8]: '))

    return foglalt_szek

def foglalas_feldolgozas(szekek, foglalt):
    szekek_foglalassal = szekek
    szekek_foglalassal[foglalt - 1] = 1

    return szekek_foglalassal

def main():
    foglalas = True
    szekek_lista = [0 for _ in range(SZEKEK_SZAMA)]

    udvozlo_uzenet(szekek_lista)
    
    szekek_kiiras(szekek_lista)

    while foglalas:
        foglalt_szek = foglalas_bekeres(szekek_lista)
        szekek_lista = foglalas_feldolgozas(szekek_lista, foglalt_szek)
        print(f"Rendben, lefoglaltam neked a {foglalt_szek}. széket.")
        szekek_kiiras(szekek_lista)

        uj_foglalas = input("Szeretnél mégegy széket foglalni? [i ; n]: ")

        if uj_foglalas == 'n':
            foglalas = False

    print("Köszönöm, hogy foglaltál széket!")


main()
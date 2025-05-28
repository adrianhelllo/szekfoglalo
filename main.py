SZEKEK_SZAMA = 8

def udvozlo_uzenet():
    print(f"Üdvözöllek a mozi székfoglaló felületén! Összes szék: {SZEKEK_SZAMA}. Rendelkezésre álló székek száma: {szekek.count(0)}")
    print("🟩: Szabadon foglalható hely\n🔴: Foglalt hely.", end="\n\n")

def szekek_kiiras():
    print("Székek:") 
    for szek in szekek:
        if szek == 0:
            print('🟩', end=' ')
        else:
            print('🔴', end=' ')
    print()

def foglalas_bekeres():
    foglalt_szek = int(input('Hányadik széket szeretnéd lefoglalni? [1-8]: '))

    while not (1 <= foglalt_szek <= 8):
        print("Érvénytelen bevitel, próbáld újra.")
        foglalt_szek = int(input('Hányadik széket szeretnéd lefoglalni? [1-8]: '))

    return foglalt_szek

def main():
    udvozlo_uzenet()
    szekek_kiiras()
    foglalt_szek = foglalas_bekeres()
    print(f"Rendben, lefoglaltuk neked a {foglalt_szek}. széket.")
    szekek = [0 for _ in range(SZEKEK_SZAMA)]



main()

#extra commit
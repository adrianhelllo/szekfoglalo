SZEKEK_SZAMA = 8
szekek = [0 for _ in range(SZEKEK_SZAMA)]

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

def main():
    udvozlo_uzenet()
    szekek_kiiras()


main()
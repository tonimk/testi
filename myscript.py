i = 0
while i < 3:
    nimi = input("Anna nimesi: ")
    print("Sinä olet " + nimi)
    ikä = int(input("Anna ikäsi: "))
    print("Ikäsi on:",ikä)
    kaverikä = int(input("Kuinka vanha mielikuvituskaverisi on? "))
    if ikä > kaverikä:
        print("Sinä olet vanhempi")
    elif ikä < kaverikä:
        print("Kaveri on vanhempi")
    else:
        print("Olette yhtä vanhoja")
    i = i + 1
    if i < 3:
        print("Tämä käydään vielä", 3 - i,"kertaa")
    else:
        print("Loppu!")

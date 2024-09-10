import time
#slovník knih, název, autor, ISBN, dostupnost
knihy={
    "kniha1" : {"nazev": "1984","autor": "Orwell","ISBN": "69420","dostupnost": False},
    "kniha2" : {"nazev": "princ","autor": "","ISBN": "65321","dostupnost": True},
    "kniha3" : {"nazev": "SSS","autor": "Kafka","ISBN": "69420","dostupnost": True}
}
uzivatele={
    "user1" : {"jmeno": "A","id": 1,"vypujcene": "", "password": "1234"},
    "user2" : {"jmeno": "B","id": 2,"vypujcene": "","password": "1234"},
    "user3" : {"jmeno": "C","id": 3,"vypujcene": "","password": "1234"}
}
prihlasen = False


def pujcit_knihu(nazev_knihy):
    if prihlasen:
        for keys, kniha in knihy.items():  # Prochází každou knihu ve slovníku
            if kniha["nazev"] == nazev_knihy and kniha["dostupnost"]:
                print(f"Chcete si vypůjčit knihu '{nazev_knihy}'? y/n")
                volba = input("")
                if volba == "Y".lower():
                    print("kniha půjčena")
                    kniha["dostupnost"] = False
                    uzivatel["vypujcene"] = nazev_knihy
                    print(uzivatel)
                    return  # Vrátí se z funkce po úspěšném nalezení
                else: 
                    pass
        print(f"Kniha '{nazev_knihy}' není dostupná nebo neexistuje.")
    else:
        print("Pro půjčení knihy se musíte přihlásit.")
        main()
        
def vypsat_knihy():
    print("---------------")
    print("Dostupné knihy:")
    print("---------------")
    for keys, kniha in knihy.items():
        if kniha["dostupnost"] == True:
            print(kniha["nazev"])
        else:
            pass
    print("---------------")
    main()

def vytvorit_ucet():
    jmeno = input("zadejte své jméno: ")
    heslo = input("zadejte své heslo: ")
    uzivatele.append({"jmeno": jmeno, "password": heslo})
    print("účet byl vytvořen")
    main()

def login():
    global prihlasen
    global uzivatel
    for keys, uzivatel in uzivatele.items():
        jmeno = input("zadejte sem své přihlašovací jméno: ")
        if jmeno == uzivatel["jmeno"]:
            heslo = input("zadejte své heslo: ")
            if heslo == uzivatel["password"]:
                print("úspěšně jste byl přihlášen")
                prihlasen = True
                main()
            else:
                print("špatné heslo")
                print("chcete to zkusit znovu?")
                volba = input("y/n")
                if volba == "Y".lower():
                    login()
                else:       
                    main()
        else:
            print("uživatel nenalezen, chcete si založit nový účet? y/n")
            volba = input("")
            if volba== "Y".lower():
                vytvorit_ucet()
            else:
                print("fuck off")
                main()

    

def main():
    print("vítejte v knihovně")
    time.sleep(1)
    print("vyberte si akci co chcete provést")
    time.sleep(1)
    print("1) přihlásit se")
    print("2) zobrazit seznam dostupných knih (doporučujeme před půjčením knihy)")
    print("3) půjčit si knihu (pro půjčení musíte být přihlášen)")

    print("zadejte 1 / 2 / 3:")
    volba = input("")
    if volba == "1":
        print("login")
        login()
    elif volba == "2":
        print("akce 2")
        vypsat_knihy()
    elif volba == "3":
        pujcit_knihu()
        
main()




import time
uzivatele={
    "user1" : {"jmeno": "A","id": 1,"vypujcene": "", "password": "1234"},
    "user2" : {"jmeno": "B","id": 2,"vypujcene": "","password": "1234"},
    "user3" : {"jmeno": "C","id": 3,"vypujcene": "","password": "1234"}
}
prihlasen = False
def login():
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
                pass
                # vytvorit_ucet()
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
    if volba == 1:
        print("login")
        login()
    elif volba == 2:
        print("akce 2")
        # vypsat_knihy()
    elif volba == 3:
        # pujcit_knihu(input("zadejte název knihy"))
        print("akce 3")
main()

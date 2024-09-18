import csv

def login():
    username = input('Zadejte uzivatelske jmeno: ')
    password = input('Zadejte heslo: ')
    
    with open('uzivatele.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for user in csv_reader:
            if user['jmeno'] == username and user['heslo'] == password:
                print('Uspesne prihlaseni')
                menu()  # spusti menu
                return
        
    print("Neplatne jmeno nebo heslo!")
    if input("Chcete se zaregistrovat? (y/n): ") == 'y':
        registrace()
    else:
        print("Konec programu.")

def registrace():
    username = input('Zadejte uzivatelske jmeno: ')
    
    # Check for duplicate username
    with open('uzivatele.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for user in csv_reader:
            if user['jmeno'] == username:
                print(f"Uzivatelske jmeno '{username}' je jiz obsazene.")
                menu()
    
    password = input('Zadejte heslo: ')
    user_id = assign_id()
    
    # Append new user to the file
    with open('uzivatele.csv', 'a', newline='') as csv_file:
        fieldnames = ['jmeno', 'id', 'vypujcene', 'heslo']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writerow({'jmeno': username, 'id': user_id, 'vypujcene': '[]', 'heslo': password})
    
    print(f"Uzivatel {username} byl zaregistrovan.")
    menu()
    
def pujcit_knihy():
    nazev_knihy = input("Zadejte nazev knihy, kterou si chcete pujcit: ")

    with open('knihy.csv', 'r', newline='') as csv_file:
        knihy = list(csv.DictReader(csv_file))

    for kniha in knihy:
        if kniha['nazev'] == nazev_knihy and kniha['dostupnost'] == 'True':
            kniha['dostupnost'] = 'False'
            break
    else:
        print("Kniha neni dostupna nebo neexistuje.")
        menu()
        return

    # Update knihy.csv
    with open('knihy.csv', 'w', newline='') as csv_file:
        fieldnames = ['nazev', 'autor', 'ISBN', 'dostupnost']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(knihy)

    username = input('Zadejte uzivatelske jmeno: ')
    password = input('Zadejte heslo: ')

    with open('uzivatele.csv', 'r', newline='') as csv_file:
        users = list(csv.DictReader(csv_file))

    for user in users:
        if user['jmeno'] == username and user['heslo'] == password:
            vypujcene = eval(user['vypujcene'])
            vypujcene.append(nazev_knihy)
            user['vypujcene'] = str(vypujcene)
            break

    # Update uzivatele.csv
    with open('uzivatele.csv', 'w', newline='') as csv_file:
        fieldnames = ['jmeno', 'id', 'vypujcene', 'heslo']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(users)

    print(f"Kniha '{nazev_knihy}' byla uspesne vypujcena.")
    menu()
def pridat_knihy():
    with open('knihy.csv', 'a', newline='') as csv_file:
        fieldnames = ['nazev', 'autor', 'ISBN', 'dostupnost']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        nazev = input('Zadejte nazev knihy: ')
        autor = input('Zadejte autora knihy: ')
        ISBN = input('Zadejte ISBN knihy: ')
        csv_writer.writerow({'nazev': nazev, 'autor': autor, 'ISBN': ISBN, 'dostupnost': 'True'})
        print(f"Kniha '{nazev}' byla pridana.")
    menu()
        
def vratit_knihy():
    username = input('Zadejte uzivatelske jmeno: ')
    password = input('Zadejte heslo: ')
    
    with open('uzivatele.csv', 'r', newline='') as csv_file:
        users = list(csv.DictReader(csv_file))
    
    for user in users:
        if user['jmeno'] == username and user['heslo'] == password:
            vypujcene = eval(user['vypujcene'])
            if not vypujcene:
                print("Nemate zadne vypujcene knihy.")
                menu()
                return
            
            print(f"Vase vypujcene knihy: {vypujcene}")
            kniha_na_vraceni = input('Zadejte nazev knihy, kterou chcete vratit: ')
            
            if kniha_na_vraceni in vypujcene:
                vypujcene.remove(kniha_na_vraceni)
                user['vypujcene'] = str(vypujcene)
                print(f"Kniha '{kniha_na_vraceni}' byla vracena.")
                # Update knihy.csv to mark the book as available again
                with open('knihy.csv', 'r', newline='') as csv_file:
                    knihy = list(csv.DictReader(csv_file))
                for kniha in knihy:
                    if kniha['nazev'] == kniha_na_vraceni:
                        kniha['dostupnost'] = 'True'
                        break
                with open('knihy.csv', 'w', newline='') as csv_file:
                    fieldnames = ['nazev', 'autor', 'ISBN', 'dostupnost']
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerows(knihy)
                break
            else:
                print("Tuto knihu nemate vypujcenou.")
                return

    with open('uzivatele.csv', 'w', newline='') as csv_file:
        fieldnames = ['jmeno', 'id', 'vypujcene', 'heslo']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(users)

    menu()

def menu():
    print('Vyberte si co chcete provést:')
    print('1) Vypsat volné knihy')
    print('2) Půjčit si knihu')
    print('3) Vrátit knihu')
    print('4) Přidat novou knihu')
    print('5) Ukončit program')

    choice = input('Zadejte volbu: ')
    if choice == '1':
        nacti_knihy()
    elif choice == '2':
        pujcit_knihy()
    elif choice == '3':
        vratit_knihy()
    elif choice == '4':
        pridat_knihy()
    else:
        print("Nashledanou.")

def assign_id():
    with open('uzivatele.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        max_id = max([int(user['id']) for user in csv_reader], default=0)
    return max_id + 1

def nacti_knihy():
    print("Dostupne knihy:")
    with open('knihy.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for kniha in csv_reader:
            if kniha['dostupnost'] == 'True':
                print(f"- {kniha['nazev']}")
    menu()

# Start the program by calling login
menu()

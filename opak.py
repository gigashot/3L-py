
#slovník knih, název, autor, ISBN, dostupnost

kniha1 = {
    "nazev": "1984",
    "autor": "Orwell",
    "ISBN": "69420",
    "dostupnost": True
}
kniha2 = {
    "nazev": "princ",
    "autor": "",
    "ISBN": "65321",
    "dostupnost": True
}

kmiha3 = {
    "nazev": "SSS",
    "autor": "Kafka",
    "ISBN": "69420",
    "dostupnost": True
}

knihy = {
    "kniha1": kniha1,
    "kniha2": kniha2,
    "kniha3": kniha3
    }


print("Vítejte v Knihovně")
print("zvolte akci")
print("1) vypiš knihu")
akce = input("vyberte si akci, kterou chcete provést")

if akce == 1:
    print("zadejte nazev knihy")
    knihy.get
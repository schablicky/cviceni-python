

def vstup(vyber):
    if vyber == 1:
        jmeno = input("Zadej sve jmeno: ")
        return jmeno
    if vyber == 2:
        prijmeni = input("Zadej sve prijmeni: ")
        return prijmeni
    if vyber == 3:
        mamka = input("Zadej cislo svoji mamky: ")
        return mamka

jmeno = vstup(1)
prijmeni = vstup(2)
mamka = vstup(3)

print(f"Jmenujes se {jmeno} {prijmeni} a tvoje mamka ma cislo {mamka}")
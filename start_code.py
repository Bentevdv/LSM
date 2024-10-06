from database_wrapper import Database

db = Database(host="localhost", gebruiker="user", wachtwoord="password", database="attractiepark_software")

def overzicht_attracties():
    # altijd verbinding openen om query's uit te voeren
    db.connect()

    select_query = "SELECT naam, type FROM voorziening"
    results = db.execute_query(select_query)

    # altijd verbinding sluiten met de database als je klaar bent
    db.close()

    return results

# vraag aan de gebruiker wat hij wil doen
# dus: tonen van voorzieningen (UC1), toevoegen van voorzieningen (UC2), etc.. etc...

print("Welkom bij de beheerapplicatie van LSM!")
print("----------- MENU -----------")
print("a) Overzicht voorzieningen")
print("b) Toevoegen van voorzieningen")

keuze = input("Selecteer optie: ")

if keuze == "a":    
    list_met_voorzieningen = overzicht_attracties()

    c = 0
    print("Het overzicht:")
    for voorziening in list_met_voorzieningen:
        print("Rij " + str(c) + ":")
        print("  - " + voorziening["naam"])
        print("  - " + voorziening["type"])
        c += 1
    
    # programmeer verder...
    #shoutout naar mijn persoonlijke teaching assistent Jordy
    # Hij heeft de code ook aangepast ivm leesbaarheidsproblemen.     
elif keuze == "b":
    print("----------- TYPES -----------")
    print("horeca")
    print("attractie")
    print("winkel")
    voorziening_type = input("\nSelecteer type voorziening: ")
    if voorziening_type != "horeca" and voorziening_type != "attractie" and voorziening_type != "winkel":
        print("Dit is geen geldig type voor een voorziening")
        exit()
    print("Voorziening maken van type; " + voorziening_type)
    

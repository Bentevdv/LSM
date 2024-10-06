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
    print("Het overzicht:")
    
    list_met_voorzieningen = overzicht_attracties()
    print(list_met_voorzieningen)

    print("Eerste rij:")
    print(list_met_voorzieningen[0]["naam"])
    print(list_met_voorzieningen[0]["type"])
    
    # programmeer verder...


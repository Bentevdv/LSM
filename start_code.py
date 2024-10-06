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
print("c) Aanpassen van voorzieningen")
print("d) Verwijderen van voorzieningen")


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
    type_voorziening = input("\nSelecteer type voorziening: ")
    if type_voorziening != "horeca" and type_voorziening != "attractie" and type_voorziening != "winkel":
        print("Dit is geen geldig type voor een voorziening")
        exit()
    # print("Voorziening maken van type; " + voorziening_type)
    
    naam_voorziening = input("Benoem voorziening: ")
    overdekt_voorziening =bool(input("Is overdekt: "))
    geschatte_wachttijd = int(input("Geschatte wachttijd: "))
    doorlooptijd = int(input("Voeg geschatte doorlooptijd toe: "))
    actief = bool(input("Is actief: "))
    
    db.connect()
    result = db.execute_query(f"""
        INSERT INTO voorziening (naam, type, overdekt, geschatte_wachttijd, doorlooptijd, actief) 
        VALUES ('{naam_voorziening}', '{type_voorziening}', {overdekt_voorziening}, {geschatte_wachttijd}, {doorlooptijd}, {actief})
    """)
    db.close()

    if result:
        print(f"Voorziening toegevoegd: {naam_voorziening}, {type_voorziening}")
     #je kan nu dingen toevoegen aan de database, nu nog bewerken en verwijderen
     #vergeet je database niet te refreshen:)

elif keuze == "d":
    print("----------- DELETE -----------")
    type_voorziening = input("\nSelecteer type voorziening: ")  
    naam_voorziening= input("Selecteer naam voorziening: ")  

    db.connect()
    result = db.execute_query(f"""
        DELETE FROM voorziening
        WHERE naam = '{naam_voorziening}' AND type = '{type_voorziening}'
    """)
    db.close()

    if result:
        print(f"Voorziening verwijderd: {naam_voorziening}, {type_voorziening}")
#Je kan nu dingen verwijderen'
#Ik kom er nu net achter dat ik c heb overgeslagen, oepsie
elif keuze == "c":
    print("----------- EDIT -----------")
    type_voorziening = input("\nSelecteer type voorziening: ")  
    naam_voorziening= input("Selecteer naam voorziening: ")

    column = input("Selecteer kolom: ")
    new_value = input("Geef nieuwe waarde: ")

    db.connect()
    result = db.execute_query(f"""
        UPDATE voorziening 
        SET {column} = {new_value} 
        WHERE naam = '{naam_voorziening}' AND type = '{type_voorziening}'
    """)
    db.close()

    print(result)

    if result:
        print(f"Voorziening aangepast: {naam_voorziening}, {type_voorziening}")

#Waarom komt hier een false uit??
#Er komt ook geen error uit en Jordy (mijn Teaching assistant komt dr ook niet uit)
#Dus ik laat het voor gezien voor nu, vooral omdat het half 2 is :)







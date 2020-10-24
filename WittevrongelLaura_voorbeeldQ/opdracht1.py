def geef_provincie(postcode):
    if postcode >= 8000 and postcode <= 8999:
        return "West-Vlaanderen"
    elif postcode >= 9000 and postcode <= 9999: 
        return "Oost-Vlaanderen"
    elif postcode >= 2000 and postcode <= 2999:
        return "Antwerpen"
    elif postcode >= 3500 and postcode <= 3999:
        return "Limburg"
    elif (postcode >= 1500 and postcode <= 1999) or (postcode >= 3000 and postcode <= 3499):
        return "Vlaams-Brabant"
    else:
        return "Geef een geldige postcode in"

ingegeven_postcode = int(input("Geef een postcode op: "))
print(f"De provincie van de postcode {ingegeven_postcode} is {geef_provincie(ingegeven_postcode)}")


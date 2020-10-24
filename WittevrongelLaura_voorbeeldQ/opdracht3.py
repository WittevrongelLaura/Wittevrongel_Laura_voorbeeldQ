# Vul onderstaande functies aan. Vergeet de parameters niet aan te vullen (zie opgave)!!!
# Test onderaan alle functies voldoende uit
def geef_provincie(postcode):
    if postcode > 8000 and postcode <= 8999:
        return "West-Vlaanderen"
    elif postcode > 9000 and postcode <= 9999: 
        return "Oost-Vlaanderen"
    elif postcode > 2000 and postcode <= 2999:
        return "Antwerpen"
    elif postcode > 3500 and postcode <= 3999:
        return "Limburg"
    elif (postcode > 1500 and postcode <= 1999) or (postcode > 3000 and postcode <= 3499):
        return "Vlaams-Brabant"
    else:
        return "Geef een geldige postcode in"




def geef_aantallen_per_provincie(dict_missen):
    dict_aantal_per_provincie = {}
    for naam, postcode in dict_missen.items():
        provincie = geef_provincie(postcode)
        return provincie




misses_2019 = {"Marieke": 8800, "Delfien": 8500, "Mieke": 8531, "Els": 9070, "Lola":  2500,
               "Dolly": 9999, "Marianne": 9000, "Claudine": 2800, "Lies": 3080, "Jacqueline": 3720, "Jozefien": 8700}
misses_2018 = {"Tine": 3700, "Anke": 8700, "Claudia": 8530, "Marijn": 9000,
               "Sofie":  2650, "Marie": 9870, "Leen": 9000, "Conny": 2800}

# Test hier bovenstaande functies uit (zie opgave voor meer detail)
ingegeven_postcode = int(input("Geef een postcode op: "))
print(f"De provincie van de postcode {ingegeven_postcode} is {geef_provincie(ingegeven_postcode)}")
print(geef_aantallen_per_provincie(misses_2018))
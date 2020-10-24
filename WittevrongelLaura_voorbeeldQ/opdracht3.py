# Vul onderstaande functies aan. Vergeet de parameters niet aan te vullen (zie opgave)!!!
# Test onderaan alle functies voldoende uit
def geef_provincie(postcode):
    if postcode >= 8000 and postcode <= 8999:
        naam_provincie = "West-Vlaanderen"
        return naam_provincie
    elif postcode >= 9000 and postcode <= 9999:
        naam_provincie = "Oost-Vlaanderen"
        return naam_provincie
    elif postcode >= 2000 and postcode <= 2999:
        naam_provincie = "Antwerpen"
        return naam_provincie
    elif postcode >= 3500 and postcode <= 3999:
        naam_provincie = "Limburg"
        return naam_provincie
    elif (postcode >= 1500 and postcode <= 1999) or (postcode >= 3000 and postcode <= 3499):
        naam_provincie = "Vlaams-Brabant"
        return naam_provincie
    else:
        return "Geef een geldige postcode in"


def geef_aantallen_per_provincie(dict_missen):
    # per provincie het aantal missen tellen
    dict_aantal_per_provincie = {}
    for postcode in dict_missen.values():
        naam_provincie = geef_provincie(postcode)
        if naam_provincie in dict_aantal_per_provincie:
            # als key bestaat +1 doen
            dict_aantal_per_provincie[naam_provincie] += 1
        else:
            # key bestaat niet = key aanmaken en een value geven
            dict_aantal_per_provincie[naam_provincie] = 1

    return dict_aantal_per_provincie

def geef_aantal_van_een_provincie(dict_missen, provincienaam):
    dict_aantal_missen_per_provincie = {}
    for postcode in dict_missen.values():
        naam_provincie = geef_provincie(postcode)
        if naam_provincie in dict_aantal_missen_per_provincie:
            # als key bestaat +1 doen
            dict_aantal_missen_per_provincie[naam_provincie] += 1
        else:
            # key bestaat niet = key aanmaken en een value geven
            dict_aantal_missen_per_provincie[naam_provincie] = 1

    if provincienaam in dict_aantal_missen_per_provincie:
        return dict_aantal_missen_per_provincie[provincienaam]
    else: 
        return "Geen missen in deze provincie"

   


misses_2019 = {"Marieke": 8800, "Delfien": 8500, "Mieke": 8531, "Els": 9070, "Lola":  2500,
               "Dolly": 9999, "Marianne": 9000, "Claudine": 2800, "Lies": 3080, "Jacqueline": 3720, "Jozefien": 8700}
misses_2018 = {"Tine": 3700, "Anke": 8700, "Claudia": 8530, "Marijn": 9000,
               "Sofie":  2650, "Marie": 9870, "Leen": 9000, "Conny": 2800}

# Test hier bovenstaande functies uit (zie opgave voor meer detail)
#print(geef_aantallen_per_provincie(misses_2018))
#print(geef_aantallen_per_provincie(misses_2018))

provincie = input("Geef een provincie in: > ")
provincie = provincie
print(f"Aantal missen van provincie {provincie} uit 2018: {geef_aantal_van_een_provincie(misses_2019, provincie)}")
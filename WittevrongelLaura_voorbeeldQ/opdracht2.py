# Vul onderstaande functies aan. Vergeet de parameters niet aan te vullen (zie opgave)!!!
# Test onderaan alle functies voldoende uit

def filter_misses_postcode(dict_missen, postcode1, postcode2):
    missen_met_postcode = []
    for naam, postcode in dict_missen.items():
        if postcode >= postcode1 and postcode < postcode2:
            missen_met_postcode.append(naam)
            
    return missen_met_postcode


misses_2019 = {"Marieke": 8800, "Delfien": 8500, "Mieke": 8531, "Els": 9070, "Lola":  2500,
               "Dolly": 9999, "Marianne": 9000, "Claudine": 2800, "Lies": 3080, "Jacqueline": 3720, "Jozefien": 8700}
misses_2018 = {"Tine": 3700, "Anke": 8700, "Claudia": 8530, "Marijn": 9000,
               "Sofie":  2650, "Marie": 9870, "Leen": 9000, "Conny": 2800}

# Test hier bovenstaande functies uit (zie opgave voor meer detail)
kleinste_postcode = int(input("Geef kleinste postcode op: > "))
grootste_postcode = int(input("Geef grootste postcode op: > "))
print(f"Dit zijn de gevonden missen uit 2018: \n{filter_misses_postcode(misses_2018, kleinste_postcode, grootste_postcode)}")
print(f"Dit zijn de gevonden missen uit 2018: \n{filter_misses_postcode(misses_2019, kleinste_postcode, grootste_postcode)}")
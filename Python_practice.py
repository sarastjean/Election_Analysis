print("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

for county in counties_dict.keys():
    print(county)

for county, voters in counties_dict.items():
    print(county,voters)

rivers = {'nile':'egypt','orinoco':'venezuela','amazonas':'america del sur'}

print("\nRios del mundo:")
for river, country in rivers.items():
    print(f"\t The {river.title()} runs through {country.title()}")
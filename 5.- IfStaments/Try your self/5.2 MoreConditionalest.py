cars_list = ['fiat', 'bmw', 'audi', 'tesla', 'ferrari']
age_in = 20
age_out = 5

car_selected = 'fiat'

if car_selected == 'fiat':
    print(f"\nHaz seleccinado {car_selected.title()} uno de los auto mas economicos.")

if car_selected != 'ferrari':
    print(f"\nHaz elegido el auto marca {car_selected.title()}, mejor selecciona un {cars_list[4].title()}.")

car_selected = 'BMW'

if car_selected.lower() == cars_list[1]:
    print(f"\nHaz seleccionado {car_selected.title()}, uno de los mejores autos.")

if age_in < 21:
    print("\nSe cumple la condicion")

car_selected = 'TOYOTA'

if car_selected.lower() not in cars_list:
    print(f"\nEl auto {car_selected.title()}, no se encuentra dentro de la lista de autos")

car_selected = "FERRARI"

if car_selected.lower() in cars_list:
    print(f"El auto {car_selected.title()}, es uno de los autos mas costoso de la lista")


def print_models(unprinted_designs, completed_models):
    #Simulate printing each design, until none are left.
    #Move each design to completed_models after printing
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing Model: {current_design}")
        completed_models.append(current_design)
    
    

def show_models(completed_models):
    #Display all completed models.
    print(f"\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
    

#Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#como primer argumento tambien puedes pasar a la funcion una copia
#de la lista unprinted_designs usando la notacion [:]
#(unprinted_designs[:])
print_models(unprinted_designs, completed_models)
show_models(completed_models)




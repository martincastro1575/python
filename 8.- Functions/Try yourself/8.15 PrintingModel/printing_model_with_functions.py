from printing_functions import print_models
from printing_functions import show_models    

#Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#como primer argumento tambien puedes pasar a la funcion una copia
#de la lista unprinted_designs usando la notacion [:]
#(unprinted_designs[:])
print_models(unprinted_designs, completed_models)
show_models(completed_models)




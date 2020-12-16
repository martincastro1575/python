#Lee todo el contenido del archivo
with open('/home/martincas/Documentos/exfile.txt','r') as a_file:
    print(a_file.read())

#Lee la linea actual
with open('/home/martincas/Documentos/exfile.txt','r') as a_file:
    print(a_file.readline())

#Lee las lineas del archivo y las guarda en una lista
with open('/home/martincas/Documentos/exfile.txt','r') as a_file:
    print(a_file.readlines())

#Si usamos la funcion list() genera una lista de las lineas del archivo
with open('/home/martincas/Documentos/exfile.txt','r') as a_file:
    print(list(a_file))

#Recorre linea a linea del archivo
with open('/home/martincas/Documentos/exfile.txt','r') as a_file:
    for line in a_file:
        print(line)
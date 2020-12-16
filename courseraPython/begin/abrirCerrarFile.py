#Abrir archivo
a_file = open('/home/martincas/Documentos/libros Python/PracticaPyton/courseraPython/exfile.txt','r')

#Leer contenido de un archivo
a_file.read()

#Cerrar un archivo
a_file.close()

#Abrir un archivo con with o content manager. Esto cierra el archivo al salir del contexto, no es
#necesario que el programador lo cierre explicitamente.
with open('/home/martincas/Documentos/libros Python/PracticaPyton/courseraPython/exfile.txt','r') as a_file:
    a_file.read()
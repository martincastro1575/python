#Escribir en un archivo una linea de texto, sobre-escribiendo el contenido del archivo
with open('/home/martincas/Documentos/exfile.txt','w') as a_file:
    a_file.write('Hola Mundo')

#Escribir en un archivo varias lineas de texto a la vez, sobre-escribiendo el contenido del archivo
with open('/home/martincas/Documentos/exfile.txt','w') as a_file:
    a_file.writelines(['Linea1\n','Linea2\n','Linea3\n','Linea4\n'])

#Agregar conteido al final de un archivo 
with open('/home/martincas/Documentos/exfile.txt','a') as a_file:
    a_file.write('Hola Mundo')


import csv

#Leer un archivo csv
with open('/home/martincas/Documentos/libros Python/PracticaPyton/courseraPython/csv_example.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))


#Escribir en un archivo csv
with open('/home/martincas/Documentos/libros Python/PracticaPyton/courseraPython/csv_example.csv','a') as csvfile:
    writer = csv.writer(csvfile)
    a_list = ['pepapig@gmail.com','Pepa','696969696']
    writer.writerow(a_list)
import json

#serializar un objeto
json.dumps([1,2,3,4])

#deserializar un objeto
json.loads('[1,2,3,4]')

#Escribir como json directamente a un archivo
with open('/home/martincas/Documentos/jsonexample.txt','w') as a_file:
    json.dump([1,2,3,4], a_file)

#leer un json directamente desde un archivo
with open('/home/martincas/Documentos/jsonexample.txt','r') as a_file:
    a_list = json.load(a_file)